from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔥 ROTA PRINCIPAL (teste)
@app.route("/")
def home():
    return "Bot online 😈"

# 🤖 ROTA DO CHAT
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "mensagem" not in data:
            return jsonify({"resposta": "Erro: mensagem não enviada corretamente 😅"})

        msg = data.get("mensagem", "").lower()

        whatsapp = "https://wa.me/5521979027387"

        # 👋 SAUDAÇÃO
        if any(p in msg for p in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
            resposta = "Oi! 😊 Seja bem-vinda! Trabalhamos com materiais para laços e artesanato. O que você procura?"

        # 🛍️ PRODUTOS
        elif any(p in msg for p in ["o que vende", "tem o que", "produtos", "trabalha com o que"]):
            resposta = "Temos fitas (gorgurão, cetim, estampadas), colas, acessórios e materiais para artesanato 😍"

        # 🎀 FITAS
        elif "fita" in msg:
            if any(p in msg for p in ["5", "n5", "número 5"]):
                resposta = "Temos fita número 5 😊 ótima pra laços médios!"
            elif any(p in msg for p in ["9", "n9", "número 9"]):
                resposta = "Temos fita número 9 😍 perfeita pra laços grandes!"
            elif any(p in msg for p in ["2", "n2", "número 2"]):
                resposta = "Temos fita número 2 😊 ideal pra detalhes!"
            else:
                resposta = "Temos vários tipos de fita 😊 você quer algum número específico?"

        # 🎨 CORES
        elif any(p in msg for p in ["cor", "cores"]):
            resposta = "Temos muitas cores lindas 😍 lisas e estampadas!"

        # 🧴 COLAS
        elif "cola quente" in msg:
            resposta = "Temos cola quente 🔥 muito usada em artesanato!"

        elif "cola silicone" in msg:
            resposta = "Temos cola de silicone 😊 ótima pra acabamento!"

        elif "cola" in msg:
            resposta = "Temos vários tipos de cola 😊 qual você precisa?"

        # 🎀 LAÇOS
        elif "laço" in msg:
            resposta = "Temos tudo pra laços 😍 fitas, acessórios e muito mais!"

        # 💰 PREÇO
        elif any(p in msg for p in ["preço", "valor", "quanto custa"]):
            resposta = "Os valores variam 😊 me fala qual produto que te informo!"

        # 📦 ESTOQUE
        elif any(p in msg for p in ["tem disponível", "estoque", "tem isso"]):
            resposta = "Temos sim 😊 me diga qual produto pra confirmar certinho!"

        # 🚚 ENTREGA
        elif any(p in msg for p in ["entrega", "frete", "envio"]):
            resposta = "Fazemos entrega 🚚 me diga seu bairro que calculo pra você!"

        # 📍 LOCAL
        elif any(p in msg for p in ["onde fica", "endereço", "localização"]):
            resposta = "Somos do Rio de Janeiro 😊 posso te passar o endereço!"

        # ⏰ HORÁRIO
        elif any(p in msg for p in ["horário", "funcionamento", "abre"]):
            resposta = "Funcionamos em horário comercial 😊"

        # 🛒 COMPRA
        elif any(p in msg for p in ["quero comprar", "vou querer", "comprar"]):
            resposta = "Perfeito 😍 me fala o que você quer que eu te ajudo no pedido!"

        # 💳 FINALIZAÇÃO (aqui manda pro zap)
        elif any(p in msg for p in ["pix", "pagamento", "finalizar", "fechar"]):
            resposta = "Pra finalizar certinho 😊 me chama no WhatsApp: " + whatsapp

        # 🤔 DÚVIDA
        elif any(p in msg for p in ["não sei", "duvida", "dúvida"]):
            resposta = "Sem problema 😊 me fala melhor que eu te ajudo!"

        # 💬 FALLBACK
        else:
            resposta = "Não entendi muito bem 😅 pode explicar melhor?"

        return jsonify({"resposta": resposta})

    except Exception as e:
        return jsonify({"resposta": "Erro interno 😅 tenta novamente"})


# 🚀 OBRIGATÓRIO PRO RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
