# VeriLabel: AI-Powered CPG Compliance Engine

VeriLabel is an automated SaaS platform designed to help Consumer Packaged Goods (CPG) brands ensure regulatory compliance. The platform automates the extraction of chemical data from raw laboratory reports (PDFs) and validates findings against global regulatory thresholds (e.g., California Prop 65).

## 🚀 Overview

- **The Problem:** CPG brands manually review hundreds of lab reports, a process prone to human error, delays, and significant regulatory risk.
- **The Solution:** An AI-driven pipeline that ingests messy PDF reports, structures chemical data, runs compliance checks against a database of regulations, and generates an embeddable "Transparency Badge" for consumer-facing trust.

## ✨ Key Features

- **AI PDF Ingestion:** Uses OpenAI GPT-4o and PyMuPDF to parse unstructured, multi-column lab reports into structured JSON.
- **Automated Compliance Engine:** Compares extracted chemical thresholds (PPM) against a seeded database of safety regulations.
- **Dynamic Transparency Badge:** Generates an embeddable UI component that brands can place on their storefronts to prove product safety to consumers.
- **Modern Dashboard:** A clean, responsive React interface built with Tailwind CSS v4.

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python), SQLModel (SQLAlchemy + Pydantic)
- **AI Layer:** OpenAI GPT-4o (JSON-mode extraction)
- **Database:** SQLite (Local Dev) / PostgreSQL (Production)
- **Frontend:** React (TypeScript), Tailwind CSS v4, Vite, Lucide-React
- **PDF Processing:** PyMuPDF (`fitz`)

## 📂 Project Structure

```text
verilabel/
├── verilabel-backend/         # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API Routes & Endpoints
│   │   ├── core/              # Database & Configuration settings
│   │   ├── models/            # SQLModel DB Definitions
│   │   ├── schemas/           # Pydantic Schemas for validation
│   │   └── services/          # Business Logic (AI & Compliance Engine)
│   └── scripts/               # Database Seeding & Verification Scripts
├── verilabel-frontend/        # React Dashboard & Components
│   └── src/                   # Vite React Application
└── docs/                      # ADRs (Architecture Decision Records)
```

## 🏁 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 18+
- An OpenAI API Key

### 1. Backend Setup
Navigate to the backend directory and install dependencies:
```bash
cd verilabel-backend
pip install -r requirements.txt
```

Set up your environment variables in the `.env` file:
```bash
export OPENAI_API_KEY="sk-your-api-key"
```

Seed the database with initial Prop 65 regulatory thresholds:
```bash
python3 -m scripts.seed_regulations
```

Start the FastAPI server:
```bash
python3 -m uvicorn app.main:app --reload
```
*The backend will be available at `http://localhost:8000`. You can view the auto-generated Swagger UI docs at `http://localhost:8000/docs`.*

### 2. Frontend Setup
Open a new terminal window, navigate to the frontend directory, and install dependencies:
```bash
cd verilabel-frontend
npm install
```

Start the Vite development server:
```bash
npm run dev
```
*The dashboard will be available at `http://localhost:5173`.*

## 🧪 Testing the API

We provide a script to quickly test the AI extraction without using the frontend. Place a sample PDF named `test_lab_report.pdf` in the `verilabel-backend/scripts/` folder, ensure your backend server is running, and execute:

```bash
cd verilabel-backend/scripts
python3 test_extraction.py
```

## 📄 License
This project is proprietary. All rights reserved.