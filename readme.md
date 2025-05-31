# Medical Claim Processor

FastAPI backend that processes medical insurance claim documents using AI.

## Features
- PDF text extraction
- Document classification using Gemini
- Multi-document processing
- Rate limiting (2/min for claims, 5/min for root)
- Redis caching
- Docker support

## AI Tools Usage

### Development Process
1. Used ChatGPT to understand folder structure and architecture
2. Used Cursor for generating and implementing code files
3. Used Gemini for document processing and validation

### Example Prompts Used

1. Architecture Planning (ChatGPT):
```
Help me design a folder structure , code for a FastAPI application that processes medical claims using AI. The app should handle PDF processing, document classification, and claim validation. {context} of the assignment
```

2. Code Generation (Cursor):
```
integrate docker in this project , implement ratelimiting if you can , you can integrate database it is up to you , keep the changes minimal
```

## Setup

### Using Docker (Recommended)

1. Set environment variables:
```bash
export GEMINI_API_KEY=your_api_key_here
or write it to .env file
```

2. Run with Docker:
```bash
docker-compose up --build
```

API will be available at http://localhost:8000

### Manual Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
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

## API Endpoint

### POST /process-claim
Process multiple PDF files (bills, discharge summaries, ID cards)

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