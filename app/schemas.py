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


class ExplainRequest(BaseModel):
    concept: str = Field(
        min_length=2,
        max_length=1000
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )

    style: str = Field(
        default="simple explanation with an example",
        max_length=200
    )


class QuizRequest(BaseModel):
    topic: str = Field(
        min_length=2,
        max_length=200
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )

    difficulty: str = Field(
        default="easy",
        max_length=30
    )

    count: int = Field(
        default=5,
        ge=1,
        le=15
    )


class SummarizeRequest(BaseModel):
    text: str = Field(
        min_length=50,
        max_length=15000
    )

    length: str = Field(
        default="medium",
        max_length=30
    )