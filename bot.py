from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔥 LIBERA CONEXÃO COM O SITE

@app.route("/")
def home():
    return "Bot online 😈"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("mensagem", "").lower()

        whatsapp = "https://wa.me/5521979027387"

        # 👋 SAUDAÇÃO
        if any(p in msg for p in ["oi", "olá", "ola", "opa", "bom dia", "boa tarde", "boa noite"]):
            resposta = "Oi! 😊 Seja bem-vinda! Trabalhamos com fitas, colas e materiais para laços. O que você procura?"

        # 🛍️ PRODUTOS
        elif any(p in msg for p in ["produtos", "o que vende", "tem o que"]):
            resposta = "Temos fitas (gorgurão, cetim, estampadas), colas, acessórios e tudo para artesanato 😍"

        # 🎀 FITAS
        elif "fita" in msg:
            if "5" in msg:
                resposta = "Temos fita número 5 😊 perfeita pra laços médios!"
            elif "9" in msg:
                resposta = "Temos fita número 9 😍 ideal pra laços grandes!"
            elif "2" in msg:
                resposta = "Temos fita número 2 😊 ótima pra acabamento!"
            elif "38" in msg:
                resposta = "Temos fita 38mm 😍 muito usada!"
            else:
                resposta = "Temos várias fitas 😍 gorgurão, cetim e estampadas! Quer algum tamanho?"

        # 🎨 CORES
        elif any(p in msg for p in ["cor", "cores"]):
            resposta = "Temos muitas cores lindas 😍 lisas e estampadas!"

        # 🧴 COLAS
        elif "cola quente" in msg:
            resposta = "Temos cola quente 🔥 muito usada no artesanato!"
        elif "cola silicone" in msg:
            resposta = "Temos cola de silicone 😊 ótima pra acabamento!"
        elif "cola" in msg:
            resposta = "Temos vários tipos de cola 😊 qual você precisa?"

        # 🎀 LAÇOS
        elif any(p in msg for p in ["laço", "lacinho"]):
            resposta = "Temos tudo pra laços 😍 materiais completos!"

        # 💰 PREÇO
        elif any(p in msg for p in ["preço", "valor", "quanto custa"]):
            resposta = "Os valores variam 😊 me fala o produto que te informo certinho!"

        # 📦 ESTOQUE
        elif any(p in msg for p in ["tem", "disponível", "estoque"]):
            resposta = "Provavelmente temos sim 😊 qual produto você quer?"

        # 🚚 ENTREGA
        elif any(p in msg for p in ["entrega", "frete"]):
            resposta = "Fazemos entrega 🚚 me diga seu bairro!"

        # 📍 LOCAL
        elif any(p in msg for p in ["endereço", "onde fica"]):
            resposta = "Somos do Rio de Janeiro 😊 posso te passar o endereço!"

        # ⏰ HORÁRIO
        elif any(p in msg for p in ["horário", "funcionamento"]):
            resposta = "Funcionamos em horário comercial 😊"

        # 🛒 COMPRA
        elif any(p in msg for p in ["quero", "comprar", "pedido"]):
            resposta = "Perfeito 😍 me fala o que você quer!"

        # 💳 PAGAMENTO
        elif any(p in msg for p in ["pix", "pagamento", "finalizar"]):
            resposta = "Pra finalizar 😊 me chama no WhatsApp: " + whatsapp

        # 📞 WHATSAPP
        elif any(p in msg for p in ["whatsapp", "zap", "contato"]):
            resposta = "Pode falar com a gente aqui 😊 " + whatsapp

        # ❌ FALLBACK
        else:
            resposta = "Hmm 🤔 não entendi muito bem. Posso te ajudar com fitas, colas e artesanato 😊"

        return jsonify({"resposta": resposta})

    except Exception as e:
        return jsonify({"resposta": "Erro interno 😅 tenta novamente"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
