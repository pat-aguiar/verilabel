# ADR-007: Embeddable Architecture

**Status:** Accepted

## Context
CPG brands need to display these results on their own Shopify/Webflow sites.

## Decision
Use a Script-based Injection strategy. For the MVP, we are just providing the UI code. For the "V1" release, we would build a dedicated CDN-hosted script (badge.js) that fetches the status from our /api/v1/reports/{id} endpoint and renders the React component as a Shadow DOM element.