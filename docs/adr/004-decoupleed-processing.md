# ADR-004: Decoupled Processing

**Status:** Accepted

## Context
AI extraction can take 5–10 seconds.

## Decision
For the MVP, we are using a Synchronous API (awaiting the response). As we scale to "Phase 2," we should move this to a background task (Celery or FastAPI's BackgroundTasks) and use WebSockets or Polling for the frontend. For a 0-to-1 MVP, keeping it synchronous simplifies the initial React implementation.