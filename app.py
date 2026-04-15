import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from agents.auditor import run_audit
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return send_from_directory(".", "index.html")

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