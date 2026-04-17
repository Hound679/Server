from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "BotilyOS AI Server Running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    user_msg = messages[-1]["content"] if messages else ""

    return jsonify({
        "response": f"Botily AI (Render): {user_msg}"
    })
