from fastapi import FastAPI, Request
from routes.claims import router as claims_router
from middleware.rate_limiter import limiter, rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)

app = FastAPI(
    title="Medical Claim Processor", 
    description="Processes insurance claim PDFs with agentic AI", 
    version="1.0"
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

app.state.redis = redis_client

app.include_router(claims_router)

@app.get("/")
@limiter.limit("5/minute")
async def root(request: Request):
    return {"message": "Medical Claim Processor API"}
