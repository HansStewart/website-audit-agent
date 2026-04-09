# Website Audit Agent

> Portfolio: https://hansstewart.lovable.app
> Architecture: https://hansstewart.github.io/ai-architecture

An autonomous AI agent that scrapes any website and returns a scored audit 
report across 5 dimensions powered by GPT-4o.

## Live Endpoint
POST https://website-audit-agent-559169459241.us-east1.run.app/audit

## Example Request
curl -X POST https://website-audit-agent-559169459241.us-east1.run.app/audit \
  -H "Content-Type: application/json" \
  -d '{"url": "https://yoursite.com"}'

## Tech Stack
Python 3.11 · Flask 3.0 · BeautifulSoup4 · OpenAI GPT-4o · Docker · GCP Cloud Run

## Local Development
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py