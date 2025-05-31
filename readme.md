# Medical Claim Processor

A FastAPI-based backend system that processes medical insurance claim documents using AI tools and agent orchestration.

## Architecture

The system follows a modular architecture with the following components:

### Services
1. **PDF Service**: Handles PDF text extraction using PyMuPDF
2. **Document Classifier**: Uses Gemini to classify document types
3. **Document Processor**: Processes different document types (bills, discharge summaries, ID cards)
4. **Claim Validator**: Validates extracted information and makes claim decisions

### Infrastructure
1. **Redis**: Used for caching and rate limiting
2. **Docker**: Containerized deployment
3. **Rate Limiting**: 2 requests per minute for claim processing, 5 requests per minute for root endpoint

### Flow
1. Upload multiple PDF files
2. Extract text from each PDF
3. Classify each document
4. Process each document based on its type
5. Validate all documents together
6. Return structured response with validation and decision

## AI Tools Used

### Cursor.ai
- Used for code scaffolding and implementation
- Helped with code organization and modularity
- Assisted in implementing FastAPI best practices

### Gemini
- Document classification
- Information extraction from different document types
- Validation and decision making

### Example Prompts

1. Document Classification:
```
Analyze this document and classify it into one of these types:
- bill
- discharge_summary
- id_card
- other

Document filename: {filename}
Document content:
{text}
```

2. Bill Processing:
```
Extract information from this medical bill in JSON format:
{
    "type": "bill",
    "hospital_name": "string",
    "total_amount": number,
    "date_of_service": "YYYY-MM-DD",
    "patient_name": "string",
    "insurance_provider": "string",
    "claim_number": "string"
}
```

3. Claim Validation:
```
Validate these medical claim documents and check for:
1. Missing required documents
2. Data consistency across documents
3. Date validity
4. Amount consistency
5. Insurance coverage validity
```

## Setup

### Using Docker (Recommended)

1. Set up environment variables:
```bash
export GEMINI_API_KEY=your_api_key_here
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

The application will be available at http://localhost:8000

### Manual Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export GEMINI_API_KEY=your_api_key_here
export REDIS_HOST=localhost
export REDIS_PORT=6379
```

3. Start Redis:
```bash
docker run -d -p 6379:6379 redis:alpine
```

4. Run the server:
```bash
uvicorn main:app --reload
```

## API Endpoints

### POST /process-claim
Accepts multiple PDF files and returns processed claim information.

Request:
- Content-Type: multipart/form-data
- Files: Multiple PDF files (bills, discharge summaries, ID cards)

Response:
```json
{
  "documents": [
    {
      "type": "bill",
      "hospital_name": "string",
      "total_amount": number,
      "date_of_service": "YYYY-MM-DD"
    }
  ],
  "validation": {
    "missing_documents": [],
    "discrepancies": []
  },
  "claim_decision": {
    "status": "approved/rejected/pending",
    "reason": "string"
  }
}
```

## Rate Limits
- Root endpoint (/): 5 requests per minute
- Process claim endpoint (/process-claim): 2 requests per minute

## Future Improvements

1. Add PostgreSQL database for claim history
2. Add authentication and authorization
3. Add more comprehensive error handling
4. Add unit tests and integration tests