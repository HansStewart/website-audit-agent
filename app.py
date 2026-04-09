import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from agents.auditor import run_audit
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "online", "agent": "website-audit-agent", "version": "1.0.0"})

@app.route("/audit", methods=["POST"])
def audit():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing required field: url"}), 400
    url = data["url"].strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        result = run_audit(url)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 422
    except Exception as e:
        return jsonify({"error": "Audit failed", "detail": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)