from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()

WHATSAPP = "https://wa.me/5521979027387"

@app.route("/")
def home():
    return """
    <h2>Atendimento 🤖</h2>
    <input id='msg' placeholder='Digite sua mensagem'>
    <button onclick='enviar()'>Enviar</button>
    <p id='resposta'></p>

    <script>
    async function enviar() {
        let msg = document.getElementById('msg').value;

        let res = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({mensagem: msg})
        });

        let data = await res.json();

        document.getElementById('resposta').innerHTML = data.resposta;
    }
    </script>
    """

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("mensagem", "")

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
Você é um atendente humano, simpático e profissional de uma loja.

REGRAS:
- Responda de forma natural, como uma pessoa real
- Seja educado e prestativo
- Tente ajudar o cliente e entender o que ele quer
- Se perceber intenção de compra, incentive suavemente

IMPORTANTE:
- Se o cliente quiser comprar, responda e inclua esse link:
{WHATSAPP}

- Nunca diga que é um robô
- Seja direto e amigável
"""
            },
            {"role": "user", "content": msg}
        ]
    )

    texto = resposta.choices[0].message.content

    return jsonify({"resposta": texto})

app.run(host="0.0.0.0", port=10000)
