# EduGenie Solution Requirements

## Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | The user can open the EduGenie homepage. |
| FR-02 | The user can ask an educational question. |
| FR-03 | The system can explain a concept according to the learner's level. |
| FR-04 | The system can generate a topic-specific quiz. |
| FR-05 | The system can summarize educational text. |
| FR-06 | The system can create a personalized learning roadmap. |
| FR-07 | The system validates user input. |
| FR-08 | The system displays useful error messages. |
| FR-09 | The system uses Google Gemini for AI generation. |
| FR-10 | The system displays results in the frontend. |

## Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-01 | The interface should be responsive on desktop and mobile screens. |
| NFR-02 | API keys must not be stored in frontend files. |
| NFR-03 | The application should use modular Python files. |
| NFR-04 | The backend should return appropriate HTTP status codes. |
| NFR-05 | User input should have length limits. |
| NFR-06 | The application should provide clear error messages. |
| NFR-07 | The application should be easy to maintain. |
| NFR-08 | The application should support future database integration. |
| NFR-09 | The application should run on a normal development laptop. |
| NFR-10 | The application should be documented and tested. |

## API Requirements

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Serve the frontend |
| GET | `/api/health` | Check application health |
| POST | `/api/ask` | Answer a question |
| POST | `/api/explain` | Explain a concept |
| POST | `/api/quiz` | Generate a quiz |
| POST | `/api/summarize` | Summarize text |
| POST | `/api/roadmap` | Create a learning roadmap |

## Validation Requirements

- Questions must contain at least three characters.
- Concepts must contain at least two characters.
- Summary text must contain at least fifty characters.
- Quiz question count must be between one and fifteen.
- Weekly study hours must be between one and sixty.