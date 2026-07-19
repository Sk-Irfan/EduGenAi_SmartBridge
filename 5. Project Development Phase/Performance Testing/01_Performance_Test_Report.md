# EduGenie Performance Test Report

## Purpose

The purpose of performance testing is to measure the responsiveness and stability of the EduGenie application.

## Test Environment

| Item | Details |
|---|---|
| Operating system | Windows |
| Python version | Python 3.11 |
| Backend | FastAPI |
| AI provider | Google Gemini |
| Browser | Microsoft Edge or Google Chrome |
| Network | Record network used during testing |
| Test date | Add date |

## Test Cases

| Test ID | Test | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| PT-01 | Open homepage | Homepage loads successfully | Add result | Pending |
| PT-02 | Open health endpoint | Response is returned quickly | Add result | Pending |
| PT-03 | Ask a question | AI answer is returned | Add result | Pending |
| PT-04 | Explain a concept | Explanation is returned | Add result | Pending |
| PT-05 | Generate a quiz | Quiz is returned | Add result | Pending |
| PT-06 | Summarize text | Summary is returned | Add result | Pending |
| PT-07 | Generate roadmap | Roadmap is returned | Add result | Pending |

## Measurements

Record the actual results after testing.

| Endpoint | First Request | Second Request | Third Request | Average |
|---|---:|---:|---:|---:|
| `/api/health` |  |  |  |  |
| `/api/ask` |  |  |  |  |
| `/api/explain` |  |  |  |  |
| `/api/quiz` |  |  |  |  |
| `/api/summarize` |  |  |  |  |
| `/api/roadmap` |  |  |  |  |

## Performance Observations

Record:

- Whether the homepage loads correctly.
- Whether API responses are delayed.
- Whether Gemini quota errors occur.
- Whether the application remains usable during testing.
- Whether the interface works on a smaller screen.

## Conclusion

The performance results should be completed only after the actual tests are run. Do not mark a test as passed without recording the result.