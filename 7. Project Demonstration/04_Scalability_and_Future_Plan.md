# EduGenie Scalability and Future Plan

## Current MVP Limitations

- No user authentication.
- No database storage.
- No saved learning history.
- No quiz score tracking.
- No PDF or DOCX upload.
- No voice assistant.
- No teacher dashboard.
- Gemini free-tier quotas may limit usage.

## Short-Term Improvements

### 1. Database Integration

Add SQLite or PostgreSQL to store:

- Users
- Questions
- Quiz attempts
- Learning roadmaps
- Progress history

### 2. Authentication

Add:

- User registration
- Login
- Password protection
- User profiles

### 3. Quiz Scoring

Add:

- Answer selection
- Automatic scoring
- Score history
- Correct answer review

### 4. Document Upload

Support:

- PDF files
- Word documents
- Text files

The uploaded content can be extracted and summarized.

### 5. Learning Progress

Add:

- Completed topics
- Quiz scores
- Study streaks
- Progress charts
- Recommended next topics

## Medium-Term Improvements

- Multilingual learning support
- Voice-based questions
- Teacher dashboard
- Course creation
- Collaborative study groups
- Personalized notifications
- Source citations
- Retrieval-augmented generation

## Deployment Plan

The application can be packaged using Docker.

Possible deployment targets:

- Cloud application hosting
- Virtual private server
- Container platform
- Educational institution server

## Scalability Architecture

```text
Users
  |
  v
Load Balancer
  |
  v
Multiple FastAPI Instances
  |
  +------------+
  |            |
  v            v
Database    Gemini API
  |
  v
Learning History and Progress