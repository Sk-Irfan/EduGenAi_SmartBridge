from fastapi import FastAPI, HTTPException

from .ai_service import AIService
from .schemas import AskRequest


app = FastAPI(
    title="EduGenie API",
    description="Google Gemini powered educational assistant",
    version="1.0.0"
)


try:
    ai_service = AIService()
except Exception as error:
    ai_service = None
    startup_error = str(error)


@app.get("/")
def home():
    return {
        "message": "EduGenie backend is running"
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "EduGenie",
        "gemini_configured": ai_service is not None
    }


@app.post("/api/ask")
def ask_question(request: AskRequest):
    if ai_service is None:
        raise HTTPException(
            status_code=503,
            detail="Gemini is not configured. Check the .env file."
        )

    try:
        return ai_service.answer_question(
            question=request.question,
            level=request.level,
            subject=request.subject
        )

    except Exception as error:
        print(f"Gemini error: {error}")

        raise HTTPException(
            status_code=502,
            detail="Gemini could not generate an answer."
        ) from error