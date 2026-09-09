from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("chatbot.config","r",encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message","")
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {msg}"
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
