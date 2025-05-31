# Medical Claim Processor API

A FastAPI-based service that processes medical insurance claims using AI-powered document analysis and validation.

## Features

- Multi-document processing (bills, discharge summaries, ID cards)
- AI-powered document classification
- Automated claim validation
- Rate limiting and caching
- Redis-based caching for improved performance

## Architecture

The project follows a modular architecture with the following components:

- **Routes**: API endpoints for claim processing
- **Services**: Core business logic for document processing
- **Agents**: AI-powered document analysis and classification
- **Models**: Data models and schemas
- **Middleware**: Rate limiting and caching

## AI Tools Usage

### ChatGPT
Used for initial project understanding and architecture design:
- Understanding folder structure and best practices
- Designing the modular architecture
- Planning the document processing flow

### Cursor
Used for code generation and implementation:
- Generating FastAPI route handlers
- Creating document processing services
- Implementing AI agents for document analysis
- Writing validation logic

## Example Prompts Used

### 1. Document Classification Prompt
```
You are an expert document classifier. Analyze the following medical document and classify it into one of these categories:
- bill
- discharge_summary
- id_card
- unknown

Consider these characteristics:
- Bills contain amounts, dates, and hospital details
- Discharge summaries contain patient history, diagnosis, and treatment details
- ID cards contain patient identification information

Document text:
{extracted_text}

Respond with a JSON object containing:
{
    "document_type": "category",
    "confidence": 0.95,
    "reasoning": "brief explanation"
}
```

### 2. Bill Processing Prompt
```
You are an expert medical bill analyzer. Extract the following information from this hospital bill:

Required fields:
- hospital_name
- total_amount
- date_of_service
- patient_name
- bill_number

Optional fields:
- room_charges
- medicine_charges
- procedure_charges
- insurance_details

Document text:
{extracted_text}

Respond with a JSON object containing the extracted information.
```

### 3. Claim Validation Prompt
```
You are an expert insurance claim validator. Analyze these documents for a claim:

Documents:
{processed_documents}

Check for:
1. Required document presence
2. Data consistency across documents
3. Date validations
4. Amount validations
5. Policy compliance

Respond with a JSON object containing:
{
    "validation": {
        "missing_documents": [],
        "discrepancies": []
    },
    "claim_decision": {
        "status": "approved/rejected",
        "reason": "detailed explanation"
    }
}
```

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Start Redis server (required for caching)

5. Run the application:
```bash
uvicorn main:app --reload
```

## API Endpoints

- `POST /process-claim`: Process multiple medical documents for claim validation
  - Accepts multiple PDF files
  - Returns structured claim analysis

## Rate Limiting

- 2 requests per minute per IP address
- Redis-based caching for processed documents (1-hour TTL)

## Error Handling

- Proper error responses for invalid documents
- Rate limit exceeded responses
- Validation error details
