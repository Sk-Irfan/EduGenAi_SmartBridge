from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=3000
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )

    subject: str | None = Field(
        default=None,
        max_length=100
    )