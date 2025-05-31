from typing import Dict, Any, List
from gemini_client import ask_gemini

class DocumentProcessor:
    @staticmethod
    async def process_bill(text: str) -> Dict[str, Any]:
        prompt = f"""
        Extract information from this medical bill in JSON format:
        {{
            "type": "bill",
            "hospital_name": "string",
            "total_amount": number,
            "date_of_service": "YYYY-MM-DD",
            "patient_name": "string",
            "insurance_provider": "string",
            "claim_number": "string"
        }}

        Document content:
        {text}
        """
        return ask_gemini(prompt)

    @staticmethod
    async def process_discharge_summary(text: str) -> Dict[str, Any]:
        prompt = f"""
        Extract information from this discharge summary in JSON format:
        {{
            "type": "discharge_summary",
            "patient_name": "string",
            "diagnosis": "string",
            "admission_date": "YYYY-MM-DD",
            "discharge_date": "YYYY-MM-DD",
            "treatments": ["string"],
            "medications": ["string"]
        }}

        Document content:
        {text}
        """
        return ask_gemini(prompt)

    @staticmethod
    async def process_id_card(text: str) -> Dict[str, Any]:
        prompt = f"""
        Extract information from this insurance ID card in JSON format:
        {{
            "type": "id_card",
            "patient_name": "string",
            "member_id": "string",
            "group_number": "string",
            "insurance_provider": "string",
            "coverage_type": "string",
            "effective_date": "YYYY-MM-DD"
        }}

        Document content:
        {text}
        """
        return ask_gemini(prompt) 