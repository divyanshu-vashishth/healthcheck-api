from gemini_client import ask_gemini
from typing import Dict, Any

class DocumentClassifier:
    @staticmethod
    async def classify_document(text: str, filename: str) -> Dict[str, Any]:
        prompt = f"""
        Analyze this document and classify it into one of these types:
        - bill
        - discharge_summary
        - id_card
        - other

        Document filename: {filename}
        Document content:
        {text}

        Respond in JSON format:
        {{
            "document_type": "type",
            "confidence": 0.95,
            "reasoning": "brief explanation"
        }}
        """
        
        response = ask_gemini(prompt)
        return response 