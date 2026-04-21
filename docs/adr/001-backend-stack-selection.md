# ADR 001: Backend Tech Stack Selection

**Status:** Accepted

## Context
Need a high-performance, type-safe backend to handle heavy PDF processing and LLM calls.

## Decision
Use FastAPI for asynchronous support (crucial for I/O bound AI calls) and SQLModel (which combines SQLAlchemy and Pydantic) to reduce boilerplate code between DB models and API schemas.