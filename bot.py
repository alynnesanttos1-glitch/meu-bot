from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Bot online 😈"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("mensagem", "").lower()

        # 📞 WHATSAPP CORRIGIDO
        whatsapp = "https://wa.me/5521979027387"

        # 👋 SAUDAÇÃO
        if any(p in msg for p in ["oi", "olá", "ola", "opa", "bom dia", "boa tarde", "boa noite"]):
            resposta = "Oi! 😊 Seja bem-vinda! Você trabalha com laços ou tá começando agora?"

        # 👩‍🎨 PERFIL
        elif any(p in msg for p in ["começando", "iniciante"]):
            resposta = "Que legal 😍 você já tem material ou quer montar um kit completo?"

        elif any(p in msg for p in ["vendo", "faço laços", "trabalho com isso"]):
            resposta = "Perfeito 😍 você usa mais fita número 5 ou 9?"

        # 🎀 FITAS
        elif "fita" in msg:
            if "5" in msg:
                resposta = "Temos fita número 5 😊 perfeita pra laços médios! Você prefere lisa ou estampada?"
            elif "9" in msg:
                resposta = "Temos fita número 9 😍 ideal pra laços grandes! Quer ver cores ou estampas?"
            elif "gorgurão" in msg:
                resposta = "Temos gorgurão 😍 você vai usar pra laço infantil ou adulto?"
            elif "cetim" in msg:
                resposta = "Temos cetim ✨ vai usar pra qual tipo de peça?"
            else:
                resposta = "Temos vários tipos de fitas 😍 você procura algum tamanho específico?"

        # 🎨 CORES
        elif any(p in msg for p in ["cor", "cores", "estampa"]):
            resposta = "Temos muitas opções lindas 😍 você quer algo mais infantil, elegante ou temático?"

        # 🧴 COLAS
        elif "cola quente" in msg:
            resposta = "Temos cola quente 🔥 você usa pistola grande ou pequena?"
        elif "cola silicone" in msg:
            resposta = "Temos cola de silicone 😊 você usa mais pra acabamento?"
        elif "cola" in msg:
            resposta = "Temos vários tipos de cola 😊 qual você costuma usar?"

        # 🎀 LAÇOS
        elif any(p in msg for p in ["laço", "lacinho"]):
            resposta = "Que lindo 😍 você faz laços simples ou personalizados?"

        # 💰 PREÇO
        elif any(p in msg for p in ["preço", "valor", "quanto custa"]):
            resposta = "Os valores variam 😊 qual produto você quer saber?"

        # 📦 DISPONIBILIDADE
        elif any(p in msg for p in ["tem", "disponível"]):
            resposta = "Provavelmente temos sim 😊 qual produto exatamente?"

        # 🚚 ENVIO
        elif any(p in msg for p in ["entrega", "frete", "envia"]):
            resposta = "Enviamos para todo o Brasil 🇧🇷😊 você já sabe o que vai querer comprar?"

        # 📍 LOCAL
        elif any(p in msg for p in ["endereço", "onde fica"]):
            resposta = "Somos do Rio de Janeiro 😊 prefere comprar online?"

        # 🛒 COMPRA
        elif any(p in msg for p in ["quero", "comprar", "pedido"]):
            resposta = "Perfeito 😍 me fala tudo que você quer!"

        # 💳 PAGAMENTO
        elif any(p in msg for p in ["pix", "pagamento", "finalizar"]):
            resposta = "Pra finalizar rapidinho 😊 chama no WhatsApp: " + whatsapp

        # 📞 WHATSAPP
        elif any(p in msg for p in ["whatsapp", "zap", "contato"]):
            resposta = "Pode chamar aqui 😊 " + whatsapp

        # 🙏
        elif any(p in msg for p in ["obrigado", "obg"]):
            resposta = "Imagina 😊 qualquer dúvida estou por aqui!"

        # ❌ FALLBACK
        else:
            resposta = "Hmm 🤔 não entendi... você tá procurando fitas, colas ou materiais pra laços?"

        return jsonify({"resposta": resposta})

    except:
        return jsonify({"resposta": "Erro interno 😅 tenta novamente"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
