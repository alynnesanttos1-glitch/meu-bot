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
        site = "https://fazendoarte.com"  # 👈 MUDA SE QUISER

        # 👋 SAUDAÇÃO + SUGESTÃO
        if any(p in msg for p in ["oi", "olá", "ola", "opa", "bom dia", "boa tarde", "boa noite"]):
            resposta = "Oi! 😊 Seja bem-vinda! Você trabalha com laços ou tá começando? Temos kits perfeitos pra começar 😍"

        # 👩‍🎨 PERFIL
        elif any(p in msg for p in ["iniciante", "começando"]):
            resposta = "Perfeito 😍 recomendo um kit com fitas + cola + acessórios! Quer que eu te sugira um kit básico?"

        elif any(p in msg for p in ["vendo", "trabalho com isso", "faço laços"]):
            resposta = "Que top 😍 você usa mais fita número 5 ou 9? Posso te indicar as mais vendidas!"

        # 🎀 FITAS + SUGESTÃO
        elif "fita" in msg:
            if "5" in msg:
                resposta = "Temos fita número 5 😊 ótima pra laços médios! As cores candy estão saindo MUITO 😍 quer ver?"
            elif "9" in msg:
                resposta = "Temos fita número 9 😍 perfeita pra laços grandes! As estampadas estão bombando 🔥 quer sugestões?"
            else:
                resposta = "Temos várias fitas 😍 recomendo gorgurão pra laços firmes! Quer ver opções?"

        # 🎨 CORES
        elif any(p in msg for p in ["cor", "cores", "estampa"]):
            resposta = "Temos muitas opções lindas 😍 infantil, luxo, temático… quer que eu te sugira algumas combinações?"

        # 🧴 COLAS + SUGESTÃO
        elif "cola quente" in msg:
            resposta = "Temos cola quente 🔥 recomendo bastão de boa qualidade pra não soltar! Você usa pistola grande ou pequena?"

        elif "cola silicone" in msg:
            resposta = "Temos cola de silicone 😊 perfeita pra acabamento! Quer que eu te sugira um combo com fitas?"

        elif "cola" in msg:
            resposta = "Temos vários tipos 😊 recomendo já pegar junto com fita pra economizar frete 😉"

        # 🎀 LAÇOS
        elif "laço" in msg:
            resposta = "Lindo 😍 você faz laços simples ou personalizados? Posso te sugerir materiais ideais!"

        # 💰 PREÇO
        elif any(p in msg for p in ["preço", "valor", "quanto"]):
            resposta = "Os valores variam 😊 me fala o produto que te passo certinho! Ou pode ver direto no site: " + site

        # 📦 DISPONIBILIDADE
        elif any(p in msg for p in ["tem", "disponível"]):
            resposta = "Temos sim 😊 chama o produto ou posso te sugerir opções parecidas!"

        # 🚚 ENVIO
        elif any(p in msg for p in ["entrega", "frete", "envia"]):
            resposta = "Enviamos para todo o Brasil 🇧🇷😊 você já quer montar seu pedido?"

        # 🛒 FINALIZAR COMPRA (SITE)
        elif any(p in msg for p in ["finalizar", "comprar", "fechar pedido"]):
            resposta = "Perfeito 😍 você pode finalizar direto pelo site: " + site + " 🛒✨\nSe precisar de ajuda, me chama no Whats: " + whatsapp

        # 📞 WHATSAPP
        elif any(p in msg for p in ["whatsapp", "zap", "atendente"]):
            resposta = "Pode chamar aqui 😊 " + whatsapp

        # 🙏
        elif any(p in msg for p in ["obrigado", "obg"]):
            resposta = "Imagina 😊 qualquer dúvida estou por aqui!"

        # 💡 SUGESTÃO AUTOMÁTICA (FALLBACK INTELIGENTE)
        else:
            resposta = "Posso te ajudar com fitas, colas ou kits completos 😍 quer que eu te sugira algo pra laços?"

        return jsonify({"resposta": resposta})

    except:
        return jsonify({"resposta": "Erro interno 😅 tenta novamente"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
