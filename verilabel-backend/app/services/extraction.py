import fitz  # PyMuPDF
import json
from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class ExtractionService:
    @staticmethod
    def extract_text_from_pdf(file_bytes: bytes) -> str:
        """Extracts raw text from PDF bytes."""
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    @staticmethod
    def parse_with_ai(raw_text: str) -> dict:
        """Uses GPT-4o to turn messy PDF text into structured JSON."""
        system_prompt = (
            "You are a specialized chemistry assistant for CPG compliance. "
            "Extract chemical test results from the provided lab report text. "
            "Return ONLY a valid JSON object where keys are chemical names (lowercase) "
            "and values are float numbers representing PPM (parts per million). "
            "Example: {'lead': 0.05, 'mercury': 0.01}. "
            "If a value is 'Not Detected', use 0.0."
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Lab Report Text: \n\n{raw_text}"}
            ],
            response_format={"type": "json_object"} # Ensures valid JSON
        )

        return json.loads(response.choices[0].message.content)