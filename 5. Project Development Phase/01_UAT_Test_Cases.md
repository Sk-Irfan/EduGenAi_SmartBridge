# EduGenie User Acceptance Test Cases

## Purpose

User Acceptance Testing verifies that EduGenie satisfies the expected user requirements.

## Test Scenarios

| ID | Scenario | Input | Expected Result |
|---|---|---|---|
| UAT-01 | Open homepage | Open `/` | EduGenie homepage is displayed |
| UAT-02 | Check health | Open `/api/health` | Status is OK |
| UAT-03 | Ask a question | Which is the largest ocean? | Answer mentions Pacific Ocean |
| UAT-04 | Explain a concept | Pythagoras Theorem | Simple explanation is displayed |
| UAT-05 | Generate quiz | Pythagoras Theorem, five questions | Quiz questions are displayed |
| UAT-06 | Summarize material | Paste study text | Summary is displayed |
| UAT-07 | Create roadmap | SQL, beginner, five hours | Learning roadmap is displayed |
| UAT-08 | Submit empty question | Empty input | Validation message is displayed |
| UAT-09 | Submit short summary | Text under fifty characters | Validation message is displayed |
| UAT-10 | Open on mobile width | Resize browser | Layout changes to one column |
| UAT-11 | Open API documentation | Open `/docs` | Swagger documentation is displayed |
| UAT-12 | Gemini unavailable | Invalid or unavailable provider | Friendly error is displayed |

## UAT-01: Homepage

### Steps

1. Start FastAPI.
2. Open `http://127.0.0.1:8000/`.
3. Check the user interface.

### Expected Result

The EduGenie homepage displays all five learning features.

## UAT-02: Question Answering

### Steps

1. Open the Ask a Question card.
2. Enter:

```text
Which is the largest ocean?