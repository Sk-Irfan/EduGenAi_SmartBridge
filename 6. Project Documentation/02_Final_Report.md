# EduGenie Final Project Report

## Abstract

EduGenie is a lightweight Google Gemini powered educational assistant developed using FastAPI, HTML, CSS, and JavaScript. The application helps students, self-learners, and educators answer questions, understand concepts, generate quizzes, summarize learning material, and create personalized learning roadmaps.

## 1. Introduction

Generative AI can support education by providing fast and personalized assistance. However, learners often need simple explanations, practice content, summaries, and structured learning plans in one place.

EduGenie was developed to provide these capabilities through a simple web interface.

## 2. Problem Statement

Students and self-learners often struggle to understand difficult topics, revise lengthy material, practice questions, and identify the correct learning sequence.

Educators also spend time preparing explanations and quizzes.

## 3. Objectives

The objectives of EduGenie are:

- Provide educational question answering.
- Explain concepts in simple language.
- Generate topic-specific quizzes.
- Summarize learning material.
- Create personalized learning roadmaps.
- Provide a responsive and user-friendly interface.
- Demonstrate practical Generative AI integration.

## 4. Proposed Solution

EduGenie uses a FastAPI backend to validate user requests and communicate with Google Gemini. A responsive HTML, CSS, and JavaScript frontend allows users to access all educational features.

## 5. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| AI Platform | Google Gemini |
| Frontend | HTML, CSS, JavaScript |
| Validation | Pydantic |
| Configuration | python-dotenv |
| Testing | Pytest |
| Version Control | Git and GitHub |
| Optional Deployment | Docker |

## 6. System Architecture

```text
User
 |
 v
HTML/CSS/JavaScript Frontend
 |
 v
FastAPI Backend
 |
 v
Pydantic Validation
 |
 v
EduGenie AI Service
 |
 v
Google Gemini API
 |
 v
Generated Educational Response