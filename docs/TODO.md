# VeriLabel Product Roadmap & TODO

This document tracks the technical roadmap and feature evolution of VeriLabel from the current MVP to a production-ready V1.0 commercial launch.

## 🟥 Phase 1: High Priority MVP Hardening
*These items address technical debt and stability issues before onboarding beta users.*

- [ ] **Asynchronous Processing:** Migrate AI extraction to `FastAPI BackgroundTasks` or `Celery` to prevent request timeouts on large PDFs. Implement WebSocket or polling on the frontend to display progress.
- [ ] **Strict Data Validation:** Implement robust Pydantic validators for the AI-extracted JSON to ensure data types (e.g., forcing floats) and schemas are strictly enforced before saving to the database.
- [ ] **Enhanced Error Handling UI:** Implement "Toast" notifications in React for failed uploads, network timeouts, or AI parsing errors to improve user experience.
- [ ] **Testing Suite:** Set up `pytest` for backend API endpoints and `Vitest`/`React Testing Library` for frontend components. Create mock PDF data for automated testing.
- [x] **Environment Security:** Move CORS origins from `*` to specific allowed domains via `.env` variables. *(Completed)*

## 🟦 Phase 2: V1.0 Core Feature Set
*Features required for a complete, marketable product offering.*

- [ ] **Embeddable Badge Infrastructure:** Develop the CDN-hosted `badge.js` script (as per ADR-007) that allows CPG brands to easily embed the React Shadow DOM component on Shopify/Webflow storefronts.
- [ ] **History & Dashboard:** 
  - [ ] Build backend endpoints to fetch, paginate, and filter past `LabReport` entries for a specific brand.
  - [ ] Implement frontend Search and Filter functionality (by date, status, or chemical).
- [ ] **Trend Analysis:** Visualize chemical concentration changes over time for specific products using charts (e.g., Recharts or Chart.js).
- [ ] **Multi-Regulation Engine:** Allow users to toggle between or simultaneously check against Prop 65, EU REACH, and FDA standards.
- [ ] **Multi-Page PDF Support:** Optimize AI prompt context windows for long-form, multi-page laboratory documentation (e.g., chunking text or using Vision models for complex tables).

## 🟩 Phase 3: SaaS Infrastructure & Commercialization
*Monetization, security, and multi-tenant architecture.*

- [ ] **Authentication & Authorization:**
  - [ ] Integrate secure Login/Signup via Auth0, Clerk, or Supabase Auth.
  - [ ] Implement Role-Based Access Control (Admin vs. Brand Manager).
- [ ] **Multi-Tenancy & Privacy:** Enforce strict row-level security or tenant IDs to ensure Brand A cannot access Brand B's proprietary lab reports. Implement auto-deletion of raw PDFs after extraction to reduce liability.
- [ ] **User & Brand Profiles:** Store brand metadata, custom logos (for white-labeled badges), and contact info.
- [ ] **Billing & Payments:**
  - [ ] Integrate Stripe for "Pay-per-report" or tiered Subscription plans.
  - [ ] Implement usage tracking to monitor LLM token costs versus user billing revenue.
- [ ] **Enterprise API Access:** Generate user-specific API keys so enterprise clients can programmatically submit lab reports in bulk.

## 🟨 Phase 4: DevOps, Monitoring & Deployment
*Scaling, reliability, and continuous delivery.*

- [ ] **Dockerization:** Containerize the Backend, Frontend, and PostgreSQL database for consistent local development and cloud deployment.
- [ ] **CI/CD Pipelines:** Configure GitHub Actions to run automated testing, linting, and type-checking on every push or Pull Request.
- [ ] **Cloud Hosting Infrastructure:** Deploy to scalable infrastructure such as AWS (ECS/RDS), GCP (Cloud Run/Cloud SQL), or Vercel/Render.
- [ ] **Observability & Logging:** Integrate Sentry or Datadog for error tracking, specifically monitoring AI parsing failure rates and API latency.
- [ ] **SSL/TLS & Custom Domains:** Secure all endpoints via HTTPS and configure custom domains for the CDN badge script.