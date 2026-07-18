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
You are EduGenie, a safe and accurate educational assistant.

Answer the learner's question clearly and accurately.

Question: {question}
Learner level: {level}
Subject: {subject or "General education"}

Rules:
- Give a direct answer first.
- Use language suitable for the learner's level.
- Add a short educational explanation.
- Include a simple example when useful.
- Do not invent facts.
- If you are uncertain, clearly say so.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return {
            "question": question,
            "level": level,
            "answer": response.text or ""
        }

    def explain_concept(
        self,
        concept: str,
        level: str,
        style: str
    ) -> dict:
        prompt = f"""
You are EduGenie, a safe and accurate educational assistant.

Explain the following concept clearly.

Concept: {concept}
Learner level: {level}
Preferred style: {style}

Rules:
- Start with a simple definition.
- Use easy educational language.
- Give a helpful analogy.
- Include one example.
- End with important key points.
- Do not invent facts.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return {
            "concept": concept,
            "level": level,
            "explanation": response.text or ""
        }

    def generate_quiz(
        self,
        topic: str,
        level: str,
        difficulty: str,
        count: int
    ) -> dict:
        prompt = f"""
You are EduGenie, an educational quiz creator.

Create a quiz for the learner.

Topic: {topic}
Learner level: {level}
Difficulty: {difficulty}
Number of questions: {count}

Rules:
- Create exactly {count} questions.
- Use multiple-choice questions.
- Give four options for every question.
- Clearly identify the correct answer.
- Give a short explanation for every answer.
- Use accurate educational content.
- Format the quiz clearly.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return {
            "topic": topic,
            "level": level,
            "difficulty": difficulty,
            "question_count": count,
            "quiz": response.text or ""
        }

    def summarize_text(
        self,
        text: str,
        length: str
    ) -> dict:
        prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following learning material.

Requested summary length: {length}

Learning material:
{text}

Rules:
- Create a clear educational summary.
- Keep the important facts.
- Use simple language.
- List the main points.
- List important keywords.
- Do not invent information.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return {
            "summary_length": length,
            "summary": response.text or ""
        }