🔍 Website Audit Agent
=======================

An autonomous AI agent that scrapes any website and returns a scored audit report across 5 dimensions — powered by GPT-4o.

🌐 Portfolio: [https://hansstewart.lovable.app](https://hansstewart.lovable.app)
🗺 Architecture: [https://hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture)



🚀 Live Endpoint
-----------------

POST [https://website-audit-agent-559169459241.us-east1.run.app/audit](https://website-audit-agent-559169459241.us-east1.run.app/audit)



📦 Overview
------------

The Website Audit Agent accepts any public URL, scrapes the page content using BeautifulSoup4, and sends the extracted data to GPT-4o for a structured analysis. It returns a scored report across five audit dimensions — giving businesses an instant, AI-powered assessment of their website's effectiveness without any manual review.



✨ Features
-----------

- Accepts any public URL as input
- Scrapes full page content including headings, body text, meta tags, and links
- Analyzes content across five scored dimensions using GPT-4o
- Returns a structured JSON report with scores and written recommendations per dimension
- Fast single-endpoint API — no setup required for the end user
- Containerized with Docker and deployed on Google Cloud Run
- Health check endpoint for uptime monitoring



📊 Audit Dimensions
--------------------

Each audit scores the website across five dimensions:

- Clarity — How clearly the site communicates its value proposition
- Credibility — Trust signals, social proof, and professionalism
- Conversion — Call to action strength and lead generation effectiveness
- Content Quality — Writing quality, structure, and relevance
- SEO Fundamentals — Meta tags, headings, keyword usage, and page structure



🛠 Tech Stack
--------------

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Web Framework | Flask 3.0 |
| Web Scraping | BeautifulSoup4 |
| AI Engine | OpenAI GPT-4o |
| Production Server | Gunicorn |
| Containerization | Docker (python:3.11-slim) |
| Cloud | Google Cloud Run — us-east1 |



📁 Project Structure
---------------------

```
website-audit-agent/
├── app.py                  Flask app — audit route and response handler
├── scraper.py              BeautifulSoup4 scraper — extracts page content
├── auditor.py              GPT-4o analysis engine — scores and evaluates content
├── requirements.txt        Python dependencies
├── Dockerfile              Container configuration
├── .dockerignore           Files excluded from Docker build
├── .env                    Local environment variables (never committed)
├── .env.example            Environment variable template for contributors
└── .gitignore              Git exclusions
```



🔌 API Reference
-----------------

GET /

Health check.

POST /audit

Scrapes a URL and returns a full scored audit report.

Example Request:

```bash
curl -X POST https://website-audit-agent-559169459241.us-east1.run.app/audit \
  -H "Content-Type: application/json" \
  -d '{"url": "https://yoursite.com"}'
```

Request Body:

```json
{
  "url": "https://yoursite.com"
}
```

Response:

```json
{
  "success": true,
  "url": "https://yoursite.com",
  "audit": {
    "clarity": {
      "score": 82,
      "summary": "The value proposition is clear above the fold but weakens in the middle sections.",
      "recommendations": ["Tighten the hero headline", "Remove redundant subheadings"]
    },
    "credibility": {
      "score": 74,
      "summary": "Some trust signals present but no visible testimonials or case studies.",
      "recommendations": ["Add client logos", "Include a testimonials section"]
    },
    "conversion": {
      "score": 68,
      "summary": "CTA exists but appears only once and lacks urgency.",
      "recommendations": ["Add a sticky CTA bar", "Use action-oriented button copy"]
    },
    "content_quality": {
      "score": 79,
      "summary": "Writing is professional but some sections are too long.",
      "recommendations": ["Break up long paragraphs", "Add more scannable bullet points"]
    },
    "seo_fundamentals": {
      "score": 71,
      "summary": "Meta description is missing. H1 tag is present but not optimized.",
      "recommendations": ["Add a meta description", "Include target keyword in H1"]
    },
    "overall_score": 75,
    "overall_summary": "Solid foundation with clear opportunities to improve conversion and SEO."
  }
}
```



⚙️ Local Development
---------------------

1. Clone the Repository

```bash
git clone https://github.com/HansStewart/website-audit-agent.git
cd website-audit-agent
```

2. Create a Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
source venv/bin/activate        # macOS / Linux
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` and set your values:

```
OPENAI_API_KEY=your_openai_api_key_here
```

5. Run the Agent

```bash
python app.py
```

The server will start at:

```
http://localhost:8080
```



🐳 Running with Docker
-----------------------

```bash
docker build -t website-audit-agent .
docker run -p 8080:8080 --env-file .env website-audit-agent
```



☁️ Deploying to Google Cloud Run
----------------------------------

Deploy from Source:

```bash
gcloud run deploy website-audit-agent \
  --source . \
  --region us-east1 \
  --platform managed \
  --allow-unauthenticated \
  --timeout 120
```

Set Environment Variables:

```bash
gcloud run services update website-audit-agent \
  --region us-east1 \
  --set-env-vars OPENAI_API_KEY=your_key_here
```



🔐 Security Notes
------------------

- Never commit your .env file — it is excluded via .gitignore
- Use Google Cloud Secret Manager for production-grade secret management
- Cloud Run services can be restricted to authenticated access by removing --allow-unauthenticated
- The agent only reads publicly accessible URLs — it does not interact with or modify any website



🗺 Roadmap
-----------

- Add PDF export of the full audit report
- Add side-by-side competitor comparison audits
- Add a web UI for non-technical users to submit URLs
- Add historical audit tracking to monitor site improvements over time
- Integrate with HubSpot to log audit results as CRM contact activities



👤 Author
----------

Hans Stewart

[GitHub](https://github.com/HansStewart)



Built with Python, BeautifulSoup4, OpenAI GPT-4o, and Google Cloud Run.