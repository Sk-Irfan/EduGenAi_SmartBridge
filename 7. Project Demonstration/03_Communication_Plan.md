# EduGenie Communication Plan

## One-Minute Project Explanation

EduGenie is a lightweight Google Gemini powered educational assistant. It helps students, self-learners, and educators answer questions, understand difficult concepts, generate quizzes, summarize study material, and create personalized learning roadmaps through one responsive web application.

## Problem Explanation

Learners often use several disconnected websites to find explanations, practice questions, summaries, and learning plans. EduGenie combines these capabilities into one simple platform.

## Solution Explanation

The user interacts with the HTML, CSS, and JavaScript frontend. FastAPI receives and validates the request. The AI service creates an educational prompt and sends it to Google Gemini. The generated response is returned to the frontend.

## Technology Explanation

### Python

Used for backend development.

### FastAPI

Used to create REST API endpoints.

### Google Gemini

Used to generate educational content.

### Pydantic

Used to validate user input.

### HTML, CSS, and JavaScript

Used to create the responsive frontend.

### GitHub

Used to store and manage the source code.

## Demonstration Roles

| Role | Responsibility |
|---|---|
| Presenter | Introduces the problem and solution |
| Demonstrator | Shows the application features |
| Technical Speaker | Explains the architecture |
| Tester | Explains testing and results |
| Conclusion Speaker | Explains limitations and future scope |

## Questions and Answers

### What is EduGenie?

EduGenie is an AI-powered educational assistant.

### Which AI service is used?

Google Gemini is used for content generation.

### Why is FastAPI used?

FastAPI is lightweight, fast, and provides automatic API documentation.

### Is the API key stored in the frontend?

No. The API key is stored in `.env` on the backend.

### What happens if Gemini quota is exhausted?

The backend returns an error message, and the user can retry after the quota becomes available.

### Can EduGenie be expanded?

Yes. It can later include authentication, databases, document uploads, progress tracking, and multilingual support.