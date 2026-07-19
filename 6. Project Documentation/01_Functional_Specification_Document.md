# EduGenie Functional Specification Document

## 1. Project Information

| Item | Details |
|---|---|
| Project Name | EduGenie Google Gemini Powered Learning Assistant |
| Version | 1.0.0 |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| AI Provider | Google Gemini |
| Repository | EduGenAi_SmartBridge |
| Target Users | Students, self-learners, and educators |

## 2. Project Objective

The objective of EduGenie is to provide a lightweight AI-powered educational assistant that helps users understand concepts, answer questions, generate quizzes, summarize learning material, and create personalized learning roadmaps.

## 3. Scope

### Included

- Educational question answering
- Simplified concept explanation
- Quiz generation
- Educational text summarization
- Personalized learning roadmap
- Responsive frontend
- REST API
- Gemini integration
- Input validation
- Error handling

### Not Included in Version 1.0

- User login
- Database storage
- Saved user history
- PDF file upload
- Voice interaction
- Automatic progress tracking
- Teacher administration panel

## 4. Functional Features

### 4.1 Question Answering

The user submits a question, learning level, and optional subject. EduGenie sends the request to Gemini and displays an educational answer.

Endpoint:

```text
POST /api/ask