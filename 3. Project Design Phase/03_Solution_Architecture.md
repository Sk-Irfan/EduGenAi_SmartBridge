# EduGenie Solution Architecture

## High-Level Architecture

```text
+-----------------------------+
|           User              |
|        Web Browser          |
+--------------+--------------+
               |
               v
+-----------------------------+
|       Frontend Layer        |
| HTML + CSS + JavaScript     |
+--------------+--------------+
               |
               v
+-----------------------------+
|       FastAPI Backend       |
| REST API Routes             |
+--------------+--------------+
               |
               v
+-----------------------------+
|    Pydantic Validation      |
| Request and Input Checking  |
+--------------+--------------+
               |
               v
+-----------------------------+
|      AI Service Layer       |
| Prompt Creation             |
| Gemini Communication        |
+--------------+--------------+
               |
               v
+-----------------------------+
|       Google Gemini API     |
| Generative AI Model         |
+--------------+--------------+
               |
               v
+-----------------------------+
|       JSON Response         |
| Answer, Quiz, Summary,      |
| Explanation, or Roadmap     |
+-----------------------------+