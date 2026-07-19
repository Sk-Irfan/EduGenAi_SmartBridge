import pytest
from pydantic import ValidationError

from app.schemas import (
    AskRequest,
    ExplainRequest,
    QuizRequest,
    RoadmapRequest,
    SummarizeRequest
)


def test_valid_question_request():
    request = AskRequest(
        question="Which is the largest ocean?",
        level="beginner"
    )

    assert request.level == "beginner"


def test_empty_question_is_rejected():
    with pytest.raises(ValidationError):
        AskRequest(question="")


def test_valid_explanation_request():
    request = ExplainRequest(
        concept="Pythagoras Theorem"
    )

    assert request.concept == "Pythagoras Theorem"


def test_quiz_count_limit():
    with pytest.raises(ValidationError):
        QuizRequest(
            topic="SQL",
            count=20
        )


def test_summary_text_minimum_length():
    with pytest.raises(ValidationError):
        SummarizeRequest(
            text="Too short"
        )


def test_valid_roadmap_request():
    request = RoadmapRequest(
        topic="SQL",
        hours_per_week=5,
        goal="Become job-ready"
    )

    assert request.hours_per_week == 5