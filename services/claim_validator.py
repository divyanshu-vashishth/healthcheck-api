from typing import Dict, Any, List
from gemini_client import ask_gemini

class ClaimValidator:
    @staticmethod
    async def validate_claim(documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        docs_str = "\n".join([str(doc) for doc in documents])
        
        prompt = f"""
        Validate these medical claim documents and check for:
        1. Missing required documents
        2. Data consistency across documents
        3. Date validity
        4. Amount consistency
        5. Insurance coverage validity

        Documents:
        {docs_str}

        Respond in JSON format:
        {{
            "validation": {{
                "missing_documents": ["list of missing document types"],
                "discrepancies": [
                    {{
                        "type": "string",
                        "description": "string",
                        "severity": "high/medium/low"
                    }}
                ],
                "data_quality": {{
                    "completeness": 0.95,
                    "consistency": 0.95
                }}
            }},
            "claim_decision": {{
                "status": "approved/rejected/pending",
                "reason": "detailed explanation",
                "required_actions": ["list of required actions"]
            }}
        }}
        """
        
        return ask_gemini(prompt) 