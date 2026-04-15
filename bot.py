from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Bot online 😈"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensagem = data.get("mensagem")

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um vendedor simpático de uma loja de laços."},
            {"role": "user", "content": mensagem}
        ]
    )

    return jsonify({
        "resposta": resposta.choices[0].message.content
    })

app.run(host="0.0.0.0", port=5000)
