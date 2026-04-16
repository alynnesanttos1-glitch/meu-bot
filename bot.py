from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

usuarios = {}

def escolher(lista):
    return random.choice(lista)

def limpar(msg):
    return msg.lower().strip()

def tem(msg, palavras):
    return any(p in msg for p in palavras)

SIM = ["sim", "quero", "claro", "pode", "ok", "ss", "s", "aham", "isso"]
NAO = ["não", "nao", "n", "depois", "agora não", "nem"]

# 🔥 PALAVRAS CHAVE MAIS COMPLETAS
PALAVRAS_PRODUTOS = {
    "fita5": ["fita 5", "n5", "nº5", "numero 5"],
    "fita9": ["fita 9", "n9", "nº9", "numero 9"],
    "cola": ["cola", "cola quente", "silicone"],
    "acrilico": ["acrílico", "acrilico", "nome acrílico", "personalizado"],
}

@app.route("/")
def home():
    return "BOT 200%+ ONLINE 🔥"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = limpar(data.get("mensagem", ""))
        user_id = data.get("user_id", request.remote_addr)

        whatsapp = "https://wa.me/5521979027387"

        if user_id not in usuarios:
            usuarios[user_id] = {
                "estado": "inicio",
                "esperando": None,
                "topico": None
            }

        user = usuarios[user_id]

        # 🔁 SAUDAÇÃO
        if tem(msg, ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "opa"]):
            user["esperando"] = "ajuda"
            return jsonify({"resposta": escolher([
                "Oi 😊 posso te ajudar com materiais!",
                "Olá 😄 quer ver produtos ou recomendações?",
                "Oi oi 😍 tá procurando algo específico?"
            ])})

        # 🔎 DETECÇÃO DE PRODUTO
        for produto, palavras in PALAVRAS_PRODUTOS.items():
            if tem(msg, palavras):
                user["topico"] = produto

                if produto == "fita5":
                    user["esperando"] = "cores"
                    return jsonify({"resposta": escolher([
                        "Temos fita nº5 sim 😊 quer sugestão de cores?",
                        "Sim 😍 fita nº5 disponível! quer combinações?",
                        "Tem sim 😄 quer ajuda pra escolher cores?"
                    ])})

                if produto == "fita9":
                    user["esperando"] = "sugestao"
                    return jsonify({"resposta": escolher([
                        "Sim 😊 fita nº9 disponível!",
                        "Temos sim 😍 ótima pra laços grandes!",
                        "Sim 😄 quer ideias pra usar?"
                    ])})

                if produto == "cola":
                    user["esperando"] = "dica"
                    return jsonify({"resposta": escolher([
                        "Sim 😊 temos cola quente!",
                        "Temos sim 😍 ajuda muito no acabamento!",
                        "Sim 😄 quer dica de uso?"
                    ])})

                if produto == "acrilico":
                    user["esperando"] = "detalhes"
                    return jsonify({"resposta": escolher([
                        "Sim 😊 fazemos nome em acrílico!",
                        "Temos sim 😍 personalizado!",
                        "Sim 😄 quer ver como funciona?"
                    ])})

        # 🔥 RECOMENDAÇÃO
        if tem(msg, ["recomenda", "sugere", "indica", "o que comprar"]):
            user["esperando"] = "perfil"
            return jsonify({"resposta": escolher([
                "Claro 😊 você tá começando?",
                "Posso ajudar 😄 quer algo básico ou completo?",
                "Boa 😍 você já trabalha com isso?"
            ])})

        # 🧠 SIM INTELIGENTE
        if tem(msg, SIM):

            if user["esperando"] == "cores":
                return jsonify({"resposta": escolher([
                    "Rosa com branco vende muito 😍",
                    "Preto com dourado fica lindo 😊",
                    "Estampado + liso combina bastante 😄"
                ])})

            if user["esperando"] == "dica":
                return jsonify({"resposta": escolher([
                    "Use pouca cola pra não manchar 😊",
                    "Cola quente ajuda na durabilidade 😄",
                    "Evite excesso pra acabamento perfeito 😍"
                ])})

            if user["esperando"] == "perfil":
                user["esperando"] = "nivel"
                return jsonify({"resposta": escolher([
                    "Você é iniciante ou já vende? 😊",
                    "Quer algo simples ou mais completo? 😄",
                    "Me fala seu nível 😊"
                ])})

            if user["esperando"] == "nivel":
                return jsonify({"resposta": escolher([
                    "Recomendo fita nº5 + cola 😊",
                    "Kit básico é ótimo pra começar 😍",
                    "Começa com fitas e acessórios 😄"
                ])})

            return jsonify({"resposta": escolher([
                "Perfeito 😊 quer mais alguma coisa?",
                "Boa 😄 posso te ajudar em algo mais?",
                "Top 😍 quer ver mais produtos?"
            ])})

        # ❌ NÃO
        if tem(msg, NAO):
            user["esperando"] = None
            return jsonify({"resposta": escolher([
                "Sem problema 😊 posso ajudar com outra coisa!",
                "Tranquilo 😄 só chamar!",
                "Beleza 😊 qualquer coisa estou aqui!"
            ])})

        # 💰 PREÇO
        if tem(msg, ["preço", "valor", "quanto custa"]):
            return jsonify({"resposta": escolher([
                "Posso te passar os valores 😊 qual produto você quer?",
                "Os preços variam 😄 me fala o produto!",
                "Me diz o que você quer que te passo o valor 😊"
            ])})

        # 📦 ENTREGA
        if tem(msg, ["entrega", "frete", "envio"]):
            return jsonify({"resposta": escolher([
                "Enviamos pra todo o Brasil 🇧🇷😊",
                "Entrega nacional disponível 😄",
                "Sim 😊 enviamos pra todo o país!"
            ])})

        # 🛒 FINALIZAR
        if tem(msg, ["comprar", "finalizar", "pedido"]):
            return jsonify({"resposta": escolher([
                f"Você pode finalizar direto no site 😊 ou chamar aqui {whatsapp}",
                f"Pode finalizar no site ou falar comigo no Whats 😊 {whatsapp}",
                f"Se quiser ajuda pode chamar no Whats 😊 {whatsapp}"
            ])})

        # 📞 WHATS
        if tem(msg, ["whatsapp", "contato"]):
            return jsonify({"resposta": f"Pode chamar aqui 😊 {whatsapp}"})

        # 💬 FALLBACK TOP
        return jsonify({"resposta": escolher([
            "Posso te ajudar com fitas, cola ou acrílico 😊",
            "Quer recomendação ou tá procurando algo específico? 😄",
            "Me fala o que você precisa 😊",
            "Posso te sugerir produtos se quiser 😍",
            "Tá procurando material ou quer ideias? 😊"
        ])})

    except:
        return jsonify({"resposta": "Deu um errinho 😅 pode tentar de novo?"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
