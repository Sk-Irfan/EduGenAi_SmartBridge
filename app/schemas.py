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