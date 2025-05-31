from fastapi import APIRouter, File, UploadFile, HTTPException, Request
import os
import uuid
import json
from typing import List, Dict, Any
from services.pdf_service import extract_text_from_pdf
from services.document_classifier import DocumentClassifier
from services.document_processor import DocumentProcessor
from services.claim_validator import ClaimValidator
from middleware.rate_limiter import limiter

router = APIRouter()

@router.post("/process-claim")
@limiter.limit("2/minute")
async def process_claim(request: Request, files: List[UploadFile] = File(...)):
    temp_files = []
    processed_documents = []
    
    try:
        for file in files:
            temp_file_path = f"temp_{uuid.uuid4()}.pdf"
            temp_files.append(temp_file_path)
            
            with open(temp_file_path, "wb") as f:
                f.write(await file.read())
            
            cache_key = f"claim_{file.filename}"
            cached_result = request.app.state.redis.get(cache_key)
            
            if cached_result:
                processed_documents.append(json.loads(cached_result))
                continue
            
            extracted_text = extract_text_from_pdf(temp_file_path)
            
            classification = await DocumentClassifier.classify_document(extracted_text, file.filename)
            
            if classification["document_type"] == "bill":
                doc_data = await DocumentProcessor.process_bill(extracted_text)
            elif classification["document_type"] == "discharge_summary":
                doc_data = await DocumentProcessor.process_discharge_summary(extracted_text)
            elif classification["document_type"] == "id_card":
                doc_data = await DocumentProcessor.process_id_card(extracted_text)
            else:
                continue 
            
            request.app.state.redis.setex(
                cache_key,
                3600,  # Cache for 1 hour
                json.dumps(doc_data)
            )
            
            processed_documents.append(doc_data)
        
        validation_result = await ClaimValidator.validate_claim(processed_documents)
        
        response = {
            "documents": processed_documents,
            "validation": validation_result["validation"],
            "claim_decision": validation_result["claim_decision"]
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)