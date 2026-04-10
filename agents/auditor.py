import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from prompts.audit_prompt import build_prompt
import json


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


def scrape_page(url: str) -> dict:
    try:
        response = requests.get(url, headers=HEADERS, timeout=15, verify=True)
        response.raise_for_status()
    except requests.exceptions.SSLError:
        response = requests.get(url, headers=HEADERS, timeout=15, verify=False)
    except requests.exceptions.ConnectionError:
        raise ValueError(f"Could not connect to {url}. Check the URL and try again.")
    except requests.exceptions.Timeout:
        raise ValueError(f"Request timed out for {url}.")
    except requests.exceptions.HTTPError as e:
        raise ValueError(f"HTTP error {e.response.status_code} for {url}.")

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else ""
    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_desc = meta_tag.get("content", "").strip()

    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
    h2s = [h.get_text(strip=True) for h in soup.find_all("h2")][:8]
    h3s = [h.get_text(strip=True) for h in soup.find_all("h3")][:6]
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True)) > 30]
    body_text = " ".join(paragraphs)[:3000]
    buttons = [b.get_text(strip=True) for b in soup.find_all(["button", "a"]) if b.get_text(strip=True)]
    cta_candidates = [b for b in buttons if 2 < len(b) < 60][:15]
    images = soup.find_all("img")
    images_without_alt = sum(1 for img in images if not img.get("alt"))
    total_images = len(images)
    total_links = len(soup.find_all("a", href=True))
    social_keywords = ["review", "testimonial", "rated", "stars", "customer", "client", "trust", "award", "certified"]
    social_proof_count = sum(1 for kw in social_keywords if kw in response.text.lower())
    forms = len(soup.find_all("form"))

    return {
        "url": url,
        "title": title,
        "meta_description": meta_desc,
        "h1": h1s,
        "h2": h2s,
        "h3": h3s,
        "body_text_sample": body_text,
        "cta_candidates": cta_candidates,
        "total_images": total_images,
        "images_without_alt": images_without_alt,
        "total_links": total_links,
        "social_proof_signals": social_proof_count,
        "forms": forms,
    }


def run_audit(url: str) -> dict:
    from dotenv import load_dotenv
    load_dotenv()
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    page_data = scrape_page(url)
    prompt = build_prompt(page_data)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert website conversion analyst and copywriter. "
                    "Return structured JSON analysis only. Never return markdown. Return only valid JSON."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )
    audit_result = json.loads(response.choices[0].message.content)
    categories = audit_result.get("categories", {})
    scores = [v.get("score", 0) for v in categories.values() if isinstance(v, dict)]
    overall = round(sum(scores) / len(scores)) if scores else 0
    return {
        "url": url,
        "overall_score": overall,
        "grade": score_to_grade(overall),
        "summary": audit_result.get("summary", ""),
        "categories": audit_result.get("categories", {}),
        "top_priorities": audit_result.get("top_priorities", []),
        "metadata": {
            "title": page_data["title"],
            "meta_description": page_data["meta_description"],
            "total_images": page_data["total_images"],
            "images_without_alt": page_data["images_without_alt"],
            "forms_detected": page_data["forms"],
            "social_proof_signals": page_data["social_proof_signals"],
        },
    }


def score_to_grade(score: int) -> str:
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"