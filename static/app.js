async function callApi(endpoint, data) {
    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    if (!response.ok) {
        throw new Error(
            result.detail || "The request failed."
        );
    }

    return result;
}


function showLoading(elementId) {
    document.getElementById(elementId).textContent =
        "EduGenie is thinking...";
}


function showResult(elementId, result) {
    document.getElementById(elementId).textContent =
        JSON.stringify(result, null, 2);
}


function showError(elementId, error) {
    document.getElementById(elementId).textContent =
        `Error: ${error.message}`;
}


// Ask a question
document
    .getElementById("ask-form")
    .addEventListener("submit", async function(event) {
        event.preventDefault();

        const outputId = "ask-result";
        showLoading(outputId);

        const data = {
            question: document.getElementById("question").value,
            level: document.getElementById("ask-level").value,
            subject: document.getElementById("subject").value
        };

        try {
            const result = await callApi(
                "/api/ask",
                data
            );

            showResult(outputId, result);
        } catch (error) {
            showError(outputId, error);
        }
    });


// Explain a concept
document
    .getElementById("explain-form")
    .addEventListener("submit", async function(event) {
        event.preventDefault();

        const outputId = "explain-result";
        showLoading(outputId);

        const data = {
            concept: document.getElementById("concept").value,
            level: document.getElementById("explain-level").value,
            style: document.getElementById("style").value
        };

        try {
            const result = await callApi(
                "/api/explain",
                data
            );

            showResult(outputId, result);
        } catch (error) {
            showError(outputId, error);
        }
    });


// Generate a quiz
document
    .getElementById("quiz-form")
    .addEventListener("submit", async function(event) {
        event.preventDefault();

        const outputId = "quiz-result";
        showLoading(outputId);

        const data = {
            topic: document.getElementById("quiz-topic").value,
            level: document.getElementById("quiz-level").value,
            difficulty: document.getElementById("difficulty").value,
            count: Number(
                document.getElementById("question-count").value
            )
        };

        try {
            const result = await callApi(
                "/api/quiz",
                data
            );

            showResult(outputId, result);
        } catch (error) {
            showError(outputId, error);
        }
    });


// Summarize text
document
    .getElementById("summary-form")
    .addEventListener("submit", async function(event) {
        event.preventDefault();

        const outputId = "summary-result";
        const text = document.getElementById("summary-text").value;

        if (text.trim().length < 50) {
            document.getElementById(outputId).textContent =
                "Please enter at least 50 characters of learning material.";
            return;
        }

        showLoading(outputId);

        const data = {
            text: text,
            length: document.getElementById("summary-length").value
        };

        try {
            const result = await callApi(
                "/api/summarize",
                data
            );

            showResult(outputId, result);
        } catch (error) {
            showError(outputId, error);
        }
    });


// Create learning roadmap
document
    .getElementById("roadmap-form")
    .addEventListener("submit", async function(event) {
        event.preventDefault();

        const outputId = "roadmap-result";
        showLoading(outputId);

        const data = {
            topic: document.getElementById("roadmap-topic").value,
            level: document.getElementById("roadmap-level").value,
            hours_per_week: Number(
                document.getElementById("hours-per-week").value
            ),
            goal: document.getElementById("learning-goal").value
        };

        try {
            const result = await callApi(
                "/api/roadmap",
                data
            );

            showResult(outputId, result);
        } catch (error) {
            showError(outputId, error);
        }
    });