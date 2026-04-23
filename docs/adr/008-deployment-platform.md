# ADR-008: Deployment Platform

**Status:** Accepted

## Context
Need a zero-cost, low-config environment for the MVP.

## Decision
Use Render over AWS/GCP to avoid "Identity and Access Management" (IAM) complexity and unexpected costs. Render provides an integrated environment where the DB and Backend share a private network.