━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  WEBSITE AUDIT AGENT
  Single-call audit service — scrape, evaluate, score, recommend.
  by Hans Stewart · hansstewart.dev

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Architecture    →   hansstewart.github.io/ai-architecture
  Portfolio       →   hansstewart.dev
  GitHub          →   github.com/HansStewart/website-audit-agent

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IT DOES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  A single-call audit service. Submit a live URL, receive a fully scored
  audit report with actionable recommendations — no setup, no manual
  review required.

  The agent fetches the target page, extracts its structural and copy
  elements using BeautifulSoup4, and runs a consistent multi-dimension
  audit rubric through GPT-4o. The result is a stable structured JSON
  response containing scores, narrative commentary, prioritized
  recommendations, and page metadata — ready for dashboards, client
  reports, or direct operational use.

  Use cases: fast prospect audits, internal website QA, and automated
  conversion reviews at scale.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BACKEND WORKFLOW — 4 STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step 01 — Request gateway
    Receives a public URL from a REST request to the audit endpoint.
    Validates the input format and confirms the URL can be processed.
    Creates a request context with identifiers for traceability and logging.
    → Input: Public website URL

  Step 02 — Extraction pipeline
    Fetches the target page and handles redirects or fetch failures.
    Uses BeautifulSoup4 to extract title, headings, body content,
    metadata, and links.
    Normalizes the page into a clean, analysis-ready object.
    → Intermediate: Structured page snapshot

  Step 03 — Audit reasoning layer
    Sends the structured snapshot to GPT-4o with the scoring framework.
    Evaluates five audit dimensions and generates detailed commentary
    for each.
    Produces business-facing recommendations tied to specific findings.
    → Processing: Scoring + recommendations

  Step 04 — Response assembly
    Maps model output into a structured JSON response format.
    Includes scores, narrative reasoning, and output-ready recommendations.
    Returns a final payload suitable for dashboards, forms, and reports.
    → Output: Scored audit JSON


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FIVE AUDIT DIMENSIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌──────────────────────────────┬────────────────────────────────────────────┐
  │ Dimension                    │ What is evaluated                          │
  ├──────────────────────────────┼────────────────────────────────────────────┤
  │ Messaging Clarity            │ Headline strength, value proposition,      │
  │                              │ above-the-fold communication quality       │
  ├──────────────────────────────┼────────────────────────────────────────────┤
  │ CTA Effectiveness            │ Button copy, placement, conversion         │
  │                              │ intent, friction in the user flow          │
  ├──────────────────────────────┼────────────────────────────────────────────┤
  │ SEO Fundamentals             │ Title tag, meta description, heading       │
  │                              │ structure, alt text coverage               │
  ├──────────────────────────────┼────────────────────────────────────────────┤
  │ Copy Quality                 │ Readability, specificity, benefit-driven   │
  │                              │ language, voice consistency                │
  ├──────────────────────────────┼────────────────────────────────────────────┤
  │ Conversion Optimization      │ Trust signals, social proof, objection     │
  │                              │ handling, layout friction                  │
  └──────────────────────────────┴────────────────────────────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
API REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  POST /audit
  Content-Type: application/json

  Request
  ───────
  {
    "url": "https://yourwebsite.com"
  }

  Response
  ────────
  {
    "overall_score": 74,
    "grade": "C",
    "summary": "...",
    "categories": {
      "messaging_clarity": {
        "score": 80,
        "verdict": "...",
        "findings": [ "..." ],
        "recommendations": [ "..." ]
      }
    },
    "top_priorities": [ "...", "...", "..." ],
    "metadata": {
      "title": "...",
      "meta_description": "...",
      "total_images": 12,
      "images_without_alt": 4,
      "forms_detected": 1
    }
  }

  GET /
  ─────
  Returns the frontend UI. A 200 confirms the container and Gunicorn
  are operational.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBSERVABILITY AND FAILURE HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Failure handling     Clear response paths for fetch, scrape, and parse
                       failures. No raw exceptions returned to the client.
  Observability        Request IDs, response timing, and audit version
                       metadata included in every response envelope.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Language        Python 3.11
  Framework       Flask
  Server          Gunicorn
  AI Model        OpenAI GPT-4o
  Scraping        BeautifulSoup4, Requests
  Deployment      Google Cloud Run — us-east1
  Container       Docker (auto-built via Cloud Run source deploy)
  Frontend        Vanilla HTML / CSS / JavaScript


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOCAL DEVELOPMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  git clone https://github.com/HansStewart/website-audit-agent.git
  cd website-audit-agent
  pip install -r requirements.txt
  cp .env.example .env
  → Add OPENAI_API_KEY to .env
  python main.py
  → Open http://localhost:8080


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DEPLOY TO GOOGLE CLOUD RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  gcloud run deploy website-audit-agent \
    --source . \
    --region us-east1 \
    --allow-unauthenticated

  Set OPENAI_API_KEY in Cloud Run → Edit & Deploy New Revision
  → Variables & Secrets.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  website-audit-agent/
  ├── main.py                    Flask entry point
  ├── app/
  │   ├── __init__.py            App factory
  │   ├── routes.py              /audit and / route handlers
  │   └── agent.py               GPT-4o audit logic and prompt engineering
  ├── index.html                 Frontend UI
  ├── requirements.txt
  ├── Procfile
  └── .env.example               OPENAI_API_KEY=


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FULL AGENT ECOSYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  AI Content Pipeline       →   github.com/HansStewart/ai-content-pipeline
  Voice-to-CRM Agent        →   github.com/HansStewart/voice-to-crm
  Pipeline Intelligence     →   github.com/HansStewart/pipeline-intelligence-agent
  CRM Automation Agent      →   github.com/HansStewart/crm-agent
  Multi-Agent BI System     →   github.com/HansStewart/multi-agent
  AI Data Agent             →   github.com/HansStewart/ai-data-agent
  RAG Document Intelligence →   github.com/HansStewart/rag-agent
  AI Architecture           →   hansstewart.github.io/ai-architecture

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Hans Stewart · Marketing Automation Engineer · hansstewart.dev
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━