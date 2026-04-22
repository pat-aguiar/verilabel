# ADR 002: Schema Design

**Status:** Accepted

## Context
Chemical data varies wildly by lab. Hard-coding every possible chemical as a table column is brittle.

## Decision
Use a JSONB (JSON) column for extracted_data. This allows the AI to extract whatever it finds, while our Compliance Engine logic handles the mapping to the Regulation table.