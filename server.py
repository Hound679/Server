from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    # SIMPLE TEST RESPONSE (replace later with real AI)
    user_msg = messages[-1]["content"] if messages else ""

    return jsonify({
        "response": f"Echo from Render: {user_msg}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)