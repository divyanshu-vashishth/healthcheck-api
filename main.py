from fastapi import FastAPI
from routes.claims import router as claims_router

app = FastAPI(
    title="Medical Claim Processor", 
    description="Processes insurance claim PDFs with agentic AI", 
    version="1.0"
)

app.include_router(claims_router)

@app.get("/")
async def root():
    return {"message": "Medical Claim Processor API"}
