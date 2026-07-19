# EduGenie Data Flow Diagram and User Stories

## Data Flow Diagram

```text
+----------------+
|      User      |
+-------+--------+
        |
        v
+-------------------------+
| HTML/CSS/JS Frontend    |
+-----------+-------------+
            |
            v
+-------------------------+
| FastAPI Backend         |
| Request Validation      |
+-----------+-------------+
            |
            v
+-------------------------+
| EduGenie AI Service     |
+-----------+-------------+
            |
            v
+-------------------------+
| Google Gemini API       |
+-----------+-------------+
            |
            v
+-------------------------+
| AI Generated Response   |
+-----------+-------------+
            |
            v
+-------------------------+
| Result Displayed        |
| in the Frontend         |
+-------------------------+