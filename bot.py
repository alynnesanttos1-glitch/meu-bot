from flask import Flask, request, jsonify

app = Flask(__name__)

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
    msg = data.get("mensagem", "").lower()

    # 👋 saudação
    if any(p in msg for p in ["oi", "olá", "opa", "bom dia", "boa tarde", "boa noite"]):
        resposta = "👋 Olá! Bem-vindo! Posso te ajudar com preços, produtos ou pedidos 😊"

    # 💰 preço
    elif any(p in msg for p in ["preço", "valor", "quanto custa"]):
        resposta = "💰 Me fala qual produto você quer que eu te passo o preço 😉"

    # 🛍️ compra (AQUI ENTRA O WHATSAPP)
    elif any(p in msg for p in ["comprar", "quero", "pedido", "pegar", "adquirir"]):
        resposta = f"""🛒 Perfeito! Vou te ajudar com isso 😈<br><br>
👉 Clique aqui para falar direto no WhatsApp:<br>
<a href="{WHATSAPP}" target="_blank">📲 Falar no WhatsApp</a>
"""

    # 🚚 entrega
    elif any(p in msg for p in ["entrega", "frete", "envio"]):
        resposta = "🚚 Fazemos entregas! Me fala seu CEP 😊"

    # 📦 produtos
    elif any(p in msg for p in ["produto", "tem", "estoque"]):
        resposta = "📦 Temos vários produtos! Quer ver os mais vendidos? 😈"

    # fallback
    else:
        resposta = f"""🤖 Não entendi muito bem 😅<br><br>
Posso te ajudar com:<br>
✔️ preços<br>
✔️ produtos<br>
✔️ pedidos<br><br>
Ou você pode falar direto no WhatsApp 👇<br>
<a href="{WHATSAPP}" target="_blank">📲 Clique aqui</a>
"""

    return jsonify({"resposta": resposta})

app.run(host="0.0.0.0", port=10000)
