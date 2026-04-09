def build_prompt(page_data: dict) -> str:
    return f"""
Audit this website and return a JSON object with the structure below.
Be specific, direct, and actionable. Score each category 0-100.

WEBSITE DATA:
URL: {page_data['url']}
Page Title: {page_data['title']}
Meta Description: {page_data['meta_description']}
H1 Tags: {page_data['h1']}
H2 Tags: {page_data['h2']}
H3 Tags: {page_data['h3']}
Body Text Sample: {page_data['body_text_sample']}
CTA/Button Text Found: {page_data['cta_candidates']}
Total Images: {page_data['total_images']}
Images Without Alt Text: {page_data['images_without_alt']}
Total Links: {page_data['total_links']}
Social Proof Signals Detected: {page_data['social_proof_signals']}
Forms Detected: {page_data['forms']}

Return ONLY this JSON structure:

{{
  "summary": "2-3 sentence executive summary of the overall performance",
  "categories": {{
    "messaging_clarity": {{
      "score": 0,
      "verdict": "one sentence verdict",
      "findings": ["finding 1", "finding 2", "finding 3"],
      "recommendations": ["specific action 1", "specific action 2"]
    }},
    "cta_effectiveness": {{
      "score": 0,
      "verdict": "one sentence verdict",
      "findings": ["finding 1", "finding 2", "finding 3"],
      "recommendations": ["specific action 1", "specific action 2"]
    }},
    "seo_fundamentals": {{
      "score": 0,
      "verdict": "one sentence verdict",
      "findings": ["finding 1", "finding 2", "finding 3"],
      "recommendations": ["specific action 1", "specific action 2"]
    }},
    "copy_quality": {{
      "score": 0,
      "verdict": "one sentence verdict",
      "findings": ["finding 1", "finding 2", "finding 3"],
      "recommendations": ["specific action 1", "specific action 2"]
    }},
    "conversion_optimization": {{
      "score": 0,
      "verdict": "one sentence verdict",
      "findings": ["finding 1", "finding 2", "finding 3"],
      "recommendations": ["specific action 1", "specific action 2"]
    }}
  }},
  "top_priorities": [
    "Most important fix and why",
    "Second most important fix",
    "Third most important fix"
  ]
}}
"""