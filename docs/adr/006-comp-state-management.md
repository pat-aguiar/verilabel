# ADR-006: Component State Management

**Status:** Accepted

## Context
The MVP has a simple one-way data flow (Upload -> Results).

## Decision
Use React useState instead of Redux or React Query for the first iteration. This minimizes boilerplate. We will move to React Query if we add a "History" view where we need to cache multiple reports.