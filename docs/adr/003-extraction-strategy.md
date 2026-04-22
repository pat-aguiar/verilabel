# ADR-003: Extraction Strategy

**Status:** Accepted

## Context
PDFs are notoriously messy (tables, multi-columns).

## Decision
Use PyMuPDF for speed and GPT-4o’s JSON mode for structure. While Vision models (GPT-4o-vision) are an option for complex layouts, text-based extraction is significantly cheaper and faster for a 0-to-1 MVP.