from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot online 😈"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("mensagem", "").lower()

    whatsapp = "https://wa.me/5521979027387"

    # 👋 SAUDAÇÃO
    if any(p in msg for p in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]):
        resposta = "Oi! 😊 Seja bem-vinda! Trabalhamos com materiais para laços e artesanato. O que você está procurando?"

    # 🛍️ PRODUTOS
    elif any(p in msg for p in ["o que vende", "tem o que", "trabalha com o que"]):
        resposta = "Temos fitas (gorgurão, cetim, estampadas), colas, acessórios para laços e vários materiais de artesanato 😍"

    # 🎀 FITAS
    elif "fita" in msg:
        resposta = "Temos vários tipos de fitas 😊 gorgurão, cetim, estampadas... você quer algum número específico?"

    elif any(p in msg for p in ["fita 5", "número 5", "n5"]):
        resposta = "Temos sim fita número 5 😊 muito usada para laços médios!"

    elif any(p in msg for p in ["fita 9", "número 9", "n9"]):
        resposta = "Temos fita número 9 também 😍 ótima pra laços grandes!"

    elif any(p in msg for p in ["fita 2", "número 2", "n2"]):
        resposta = "Temos fita número 2 sim 😊 perfeita para detalhes!"

    # 🎨 CORES
    elif "cor" in msg or "cores" in msg:
        resposta = "Temos muitas cores lindas 😍 lisas e estampadas!"

    # 🧴 COLAS
    elif "cola quente" in msg:
        resposta = "Temos cola quente sim 🔥 perfeita para artesanato!"

    elif "cola silicone" in msg:
        resposta = "Temos cola de silicone 😊 ótima para acabamento!"

    elif "cola" in msg:
        resposta = "Temos vários tipos de cola 😊 qual você precisa?"

    # 🎀 LAÇOS
    elif "laço" in msg:
        resposta = "Temos tudo para laços 😍 fitas, acessórios e mais!"

    # 🧵 MATERIAIS
    elif any(p in msg for p in ["material", "acessório", "produto"]):
        resposta = "Temos vários materiais de artesanato 😊 me fala o que você precisa!"

    # 💰 PREÇO
    elif any(p in msg for p in ["preço", "valor", "quanto custa"]):
        resposta = "Os valores variam 😊 me fala qual produto você quer que te informo!"

    # 📦 ESTOQUE
    elif any(p in msg for p in ["tem disponível", "estoque"]):
        resposta = "Temos sim 😊 me diga qual produto pra confirmar certinho!"

    # 🚚 ENTREGA
    elif any(p in msg for p in ["entrega", "frete", "envio"]):
        resposta = "Fazemos entrega 🚚 me diga seu bairro para calcular!"

    # 📍 LOCALIZAÇÃO
    elif any(p in msg for p in ["onde fica", "endereço"]):
        resposta = "Somos do Rio de Janeiro 😊 posso te passar o endereço certinho!"

    # ⏰ HORÁRIO
    elif any(p in msg for p in ["horário", "funcionamento"]):
        resposta = "Funcionamos em horário comercial 😊"

    # 🛒 COMPRA
    elif any(p in msg for p in ["quero comprar", "vou querer", "como comprar"]):
        resposta = "Perfeito 😍 me diga o que você quer que eu te ajudo a montar o pedido!"

    # 💳 FINALIZAÇÃO
    elif any(p in msg for p in ["pix", "pagamento", "finalizar", "fechar pedido"]):
        resposta = "Perfeito 😊 para finalizar te passo tudo no WhatsApp: " + whatsapp

    # 🤔 DÚVIDA
    elif any(p in msg for p in ["não sei", "dúvida"]):
        resposta = "Sem problema 😊 me explica melhor que eu te ajudo!"

    # 💬 FALLBACK
    else:
        resposta = "Não entendi muito bem 😅 pode explicar melhor?"

    return jsonify({"resposta": resposta})


# 🚀 ESSENCIAL PRA RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
