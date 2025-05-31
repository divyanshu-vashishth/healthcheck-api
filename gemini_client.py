import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

def ask_gemini(prompt: str) -> dict:
    response = model.generate_content(prompt)
    try:
        text_response = response.text.strip()
        
        if text_response.startswith("```json"):
            text_response = text_response[7:]
        if text_response.endswith("```"):
            text_response = text_response[:-3]
        text_response = text_response.strip()
        
        json_response = json.loads(text_response)
        
        return json_response
    except Exception as e:
        return {"error": str(e)}
