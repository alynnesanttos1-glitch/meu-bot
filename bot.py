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

        whatsapp = "https://wa.me/5521979027387"

        # 👋 SAUDAÇÃO
        if any(p in msg for p in ["oi", "olá", "ola", "opa", "bom dia", "boa tarde", "boa noite"]):
            resposta = "Oi! 😊 Seja bem-vinda! Trabalhamos com fitas, colas e materiais para laços. O que você procura?"

        # 🛍️ PRODUTOS
        elif any(p in msg for p in ["produtos", "o que vende", "tem o que", "catálogo"]):
            resposta = "Temos fitas (gorgurão, cetim, estampadas), colas, acessórios e tudo para artesanato 😍"

        # 🎀 FITAS (bem completo)
        elif "fita" in msg:
            if "5" in msg:
                resposta = "Temos fita número 5 😊 perfeita pra laços médios!"
            elif "9" in msg:
                resposta = "Temos fita número 9 😍 ideal pra laços grandes!"
            elif "2" in msg:
                resposta = "Temos fita número 2 😊 ótima pra acabamento!"
            elif "38" in msg:
                resposta = "Temos fita 38mm 😍 muito usada!"
            elif "gorgurão" in msg:
                resposta = "Temos fita gorgurão 😍 super resistente e linda!"
            elif "cetim" in msg:
                resposta = "Temos fita de cetim ✨ perfeita pra acabamento delicado!"
            else:
                resposta = "Temos vários tipos de fitas 😍 gorgurão, cetim e estampadas! Quer algum tamanho específico?"

        # 🎨 CORES
        elif any(p in msg for p in ["cor", "cores", "colorido"]):
            resposta = "Temos muitas cores lindas 😍 lisas, estampadas e temáticas!"

        # 🧴 COLAS
        elif "cola quente" in msg:
            resposta = "Temos cola quente 🔥 ideal pra artesanato!"
        elif "cola silicone" in msg:
            resposta = "Temos cola de silicone 😊 ótima pra acabamento!"
        elif "cola pano" in msg:
            resposta = "Temos cola para tecido 😊 perfeita pra laços!"
        elif "cola" in msg:
            resposta = "Temos vários tipos de cola 😊 qual você precisa?"

        # 🎀 LAÇOS
        elif any(p in msg for p in ["laço", "lacinho", "lacinhos"]):
            resposta = "Temos todos os materiais pra laços 😍 você faz ou quer montar kits?"

        # 🧵 MATERIAIS
        elif any(p in msg for p in ["material", "acessórios", "kit"]):
            resposta = "Temos kits e materiais completos 😍 me fala o que você precisa!"

        # 💰 PREÇO
        elif any(p in msg for p in ["preço", "valor", "quanto custa"]):
            resposta = "Os valores variam 😊 me fala qual produto que te passo certinho!"

        # 📦 DISPONIBILIDADE
        elif any(p in msg for p in ["tem", "disponível", "estoque"]):
            resposta = "Provavelmente temos sim 😊 qual produto você quer?"

        # 🚚 ENTREGA (AJUSTADO COMO TU PEDIU)
        elif any(p in msg for p in ["entrega", "frete", "envia"]):
            resposta = "Enviamos para todo o Brasil 🇧🇷😊 Pra combinar envio e valores, chama no WhatsApp: " + whatsapp

        # 📍 LOCAL
        elif any(p in msg for p in ["endereço", "onde fica", "localização"]):
            resposta = "Somos do Rio de Janeiro 😊 se quiser mais detalhes é só chamar no WhatsApp: " + whatsapp

        # ⏰ HORÁRIO
        elif any(p in msg for p in ["horário", "funcionamento", "abre"]):
            resposta = "Funcionamos em horário comercial 😊 se quiser atendimento mais rápido, chama no WhatsApp!"

        # 🛒 COMPRA
        elif any(p in msg for p in ["quero", "comprar", "pedido", "vou levar"]):
            resposta = "Perfeito 😍 me chama no WhatsApp pra gente finalizar rapidinho: " + whatsapp

        # 💳 PAGAMENTO
        elif any(p in msg for p in ["pix", "pagamento", "cartão", "dinheiro"]):
            resposta = "Pra pagamento e finalização 😊 chama no WhatsApp: " + whatsapp

        # 📞 WHATSAPP
        elif any(p in msg for p in ["whatsapp", "zap", "contato", "falar com alguém"]):
            resposta = "Pode falar direto aqui 😊 " + whatsapp

        # 🙏 AGRADECIMENTO
        elif any(p in msg for p in ["obrigado", "obg", "valeu"]):
            resposta = "Imagina 😊 qualquer coisa estou por aqui!"

        # ❌ FALLBACK (mais humano)
        else:
            resposta = "Hmm 🤔 não entendi muito bem... mas posso te ajudar com fitas, colas e materiais pra artesanato 😍"

        return jsonify({"resposta": resposta})

    except:
        return jsonify({"resposta": "Erro interno 😅 tenta novamente"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
