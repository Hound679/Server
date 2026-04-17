from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# 🔐 Get API key from Render environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "BotilyOS AI Running"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        messages = data.get("messages", [])

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return jsonify({
            "response": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({
            "response": f"Error: {str(e)}"
        })
