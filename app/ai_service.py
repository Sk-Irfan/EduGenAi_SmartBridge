import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class AIService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.5-flash"
        )

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing in the .env file"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = model

    def answer_question(
        self,
        question: str,
        level: str,
        subject: str | None = None
    ) -> dict:
        prompt = f"""
You are EduGenie, an educational assistant.

Answer the learner's question clearly and accurately.

Learner level: {level}
Subject: {subject or "General education"}
Question: {question}

Rules:
- Use language appropriate for the learner's level.
- Give a direct answer first.
- Add a short educational explanation.
- Include one simple example when useful.
- Do not invent facts.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return {
            "question": question,
            "level": level,
            "answer": response.text
        }