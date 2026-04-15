from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()

WHATSAPP = "https://wa.me/5521979027387"

@app.route("/")
def home():
    return """
    <h2>Atendimento 🤖</h2>

    <input id="msg" placeholder="Digite sua mensagem" style="width:200px;">
    <button onclick="enviar()">Enviar</button>

    <p id="resposta"></p>

    <script>
    async function enviar() {
        let msg = document.getElementById("msg").value;

        if (!msg) return;

        try {
            let res = await fetch("https://meu-bot-9brl.onrender.com/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ mensagem: msg })
            });

            let data = await res.json();

            document.getElementById("resposta").innerText = data.resposta;

        } catch (erro) {
            document.getElementById("resposta").innerText = "Erro ao conectar com o servidor 😢";
            console.error(erro);
        }
    }
    </script>
    """

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("mensagem", "")

        resposta = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": msg}
            ]
        )

        texto = resposta.choices[0].message.content

        return jsonify({"resposta": texto})

    except Exception as e:
        return jsonify({"resposta": str(e)})
    data = request.get_json()
    msg = data.get("mensagem", "")

    try:
        resposta = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Você é um atendente humano, simpático e profissional.

REGRAS:
- Fale como uma pessoa real
- Seja educado e direto
- Ajude o cliente
- Incentive a compra de forma leve

IMPORTANTE:
- Se o cliente quiser comprar ou demonstrar interesse, envie esse link:
{WHATSAPP}

- Nunca diga que é um robô
"""
                },
                {"role": "user", "content": msg}
            ]
        )

        texto = resposta.choices[0].message.content

        return jsonify({"resposta": texto})

    except Exception as e:
        return jsonify({"resposta": "Deu um erro aqui 😢 tenta de novo"})


app.run(host="0.0.0.0", port=10000)
