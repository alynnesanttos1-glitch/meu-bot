from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("mensagem", "").lower()

    whatsapp = "https://wa.me/5521979027387"

    # 👋 SAUDAÇÃO
    if any(p in msg for p in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]):
        resposta = "Oi! 😊 Seja bem-vinda! Trabalho com materiais para laços e artesanato. O que você está procurando hoje?"

    # 🛍️ O QUE VENDE
    elif any(p in msg for p in ["o que você vende", "tem o que", "trabalha com o que"]):
        resposta = "Temos fitas (gorgurão, cetim, estampadas), colas, acessórios para laços e vários materiais de artesanato 😍"

    # 🎀 FITAS
    elif "fita" in msg:
        resposta = "Temos vários tipos de fita 😊 gorgurão, cetim, estampadas... você procura algum número específico?"

    elif any(p in msg for p in ["fita 5", "número 5", "n5"]):
        resposta = "Temos sim fita número 5 😊 é uma das mais usadas pra laços médios! Quer saber as cores disponíveis?"

    elif any(p in msg for p in ["fita 9", "número 9", "n9"]):
        resposta = "Temos fita número 9 também 😍 ótima pra laços grandes e chamativos!"

    elif "fita 2" in msg or "número 2" in msg:
        resposta = "Temos fita número 2 sim 😊 perfeita pra detalhes menores!"

    # 🎨 CORES
    elif "cores" in msg:
        resposta = "Temos muitas cores lindas 😍 lisas e estampadas! Se quiser te mostro algumas opções 😊"

    # 🧴 COLAS
    elif "cola" in msg:
        resposta = "Temos cola de silicone, cola quente e outras específicas pra artesanato 😊 qual você precisa?"

    elif "cola quente" in msg:
        resposta = "Temos sim cola quente 🔥 muito usada pra laços e artesanato!"

    elif "cola silicone" in msg:
        resposta = "Temos cola de silicone também 😊 ótima pra acabamento mais delicado!"

    # 🎀 LAÇOS
    elif "laço" in msg:
        resposta = "Você faz laços? 😍 Temos tudo que você precisa pra montar, desde fitas até acessórios!"

    # 🧵 MATERIAIS
    elif any(p in msg for p in ["material", "acessórios", "itens", "produtos"]):
        resposta = "Temos vários materiais pra artesanato 😊 me fala o que você precisa que eu te ajudo!"

    # 💰 PREÇOS (SEM mandar direto pro zap)
    elif any(p in msg for p in ["preço", "valor", "quanto custa"]):
        resposta = "Os valores variam dependendo do produto 😊 me fala qual item você quer que eu te passo o valor!"

    # 📦 ESTOQUE
    elif any(p in msg for p in ["tem disponível", "tem estoque", "tem isso"]):
        resposta = "Temos sim 😊 mas me fala exatamente qual produto pra eu confirmar certinho!"

    # 🚚 ENTREGA
    elif any(p in msg for p in ["entrega", "envio", "frete"]):
        resposta = "Fazemos entrega sim 🚚 o valor depende da região! Quer me informar seu bairro?"

    # 📍 LOCAL
    elif any(p in msg for p in ["onde fica", "endereço", "localização"]):
        resposta = "Somos do Rio de Janeiro 😊 se quiser te passo o endereço certinho!"

    # ⏰ HORÁRIO
    elif any(p in msg for p in ["horário", "funcionamento", "abre que horas"]):
        resposta = "Funcionamos em horário comercial 😊 se quiser te confirmo direitinho!"

    # 🛒 COMPRA
    elif any(p in msg for p in ["quero comprar", "como comprar", "vou querer"]):
        resposta = "Perfeito! 😍 Me fala o que você quer que eu já te ajudo com o pedido!"

    # ❗ FINALIZAÇÃO → AQUI SIM manda pro zap
    elif any(p in msg for p in ["fechar pedido", "finalizar", "pagamento", "pix"]):
        resposta = "Perfeito 😊 pra finalizar certinho e te passar pagamento, me chama no WhatsApp: " + whatsapp

    # 🤔 INDECISO
    elif any(p in msg for p in ["não sei", "tô na dúvida"]):
        resposta = "Sem problema 😊 me fala o que você quer fazer que eu te ajudo a escolher!"

    # 💬 FALLBACK INTELIGENTE
    else:
        resposta = "Hmm 🤔 não entendi muito bem, mas quero te ajudar! Me explica melhor o que você precisa 😊"

    return jsonify({"resposta": resposta})
