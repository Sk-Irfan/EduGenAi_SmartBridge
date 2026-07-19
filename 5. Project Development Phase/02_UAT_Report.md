# EduGenie User Acceptance Test Report

## Project Details

| Item | Details |
|---|---|
| Project | EduGenie Google Gemini Powered Learning Assistant |
| Tester | Shaik Irfan |
| Environment | Windows 10/11 development laptop |
| Python Version | Python 3.11.9 |
| Backend | FastAPI |
| AI Provider | Google Gemini |
| Test Date | 19 July 2026 |

## Test Results

| Test ID | Test Scenario | Actual Result | Status |
|---|---|---|---|
| UAT-01 | Open homepage | EduGenie homepage loaded successfully | PASS |
| UAT-02 | Check health endpoint | Endpoint returned HTTP 200 | PASS |
| UAT-03 | Ask which is the largest ocean | Response identified the Pacific Ocean | PASS |
| UAT-04 | Explain Pythagoras Theorem | Concept explanation was generated | PASS |
| UAT-05 | Generate a quiz | Gemini returned a free-tier quota error | BLOCKED BY QUOTA |
| UAT-06 | Summarize learning material | Test after Gemini quota resets | PENDING |
| UAT-07 | Create SQL learning roadmap | Test after Gemini quota resets | PENDING |
| UAT-08 | Submit an empty question | Input validation rejects invalid input | PASS |
| UAT-09 | Submit short summary text | Input validation rejects short text | PASS |
| UAT-10 | Open homepage on smaller screen | Responsive layout should be verified | PENDING |
| UAT-11 | Open Swagger API documentation | Swagger page opened successfully | PASS |
| UAT-12 | Handle Gemini provider error | Backend returned a controlled error response | PASS |

## Automated Test Results

The schema validation tests were executed using Pytest.

```text
6 tests passed in 7.02 seconds