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

SIM = ["sim", "quero", "claro", "pode", "ok", "ss", "s"]
NAO = ["não", "nao", "n", "depois", "agora não"]

@app.route("/")
def home():
    return "Bot inteligente rodando 🔥"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = limpar(data.get("mensagem", ""))
        user_id = data.get("user_id", request.remote_addr)

        whatsapp = "https://wa.me/5521979027387"

        # cria usuário
        if user_id not in usuarios:
            usuarios[user_id] = {
                "estado": "inicio",
                "topico": None,
                "esperando": None
            }

        user = usuarios[user_id]

        # 🔁 SAUDAÇÃO
        if tem(msg, ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
            user["estado"] = "inicio"
            user["esperando"] = "ajuda"
            return jsonify({"resposta": escolher([
                "Oi 😊 posso te ajudar a escolher produtos!",
                "Olá 😄 quer recomendação de materiais?",
                "Oi oi 😍 tá procurando algo específico?"
            ])})

        # 🛍️ PRODUTOS ESPECÍFICOS
        if tem(msg, ["fita 5", "n5", "nº5", "numero 5"]):
            user["topico"] = "fita5"
            user["esperando"] = "quer_cores"
            return jsonify({"resposta": escolher([
                "Sim 😊 temos fita nº5! Quer sugestões de cores?",
                "Temos sim 😍 fita nº5 é muito usada! Quer ideias?",
                "Sim 😄 fita nº5 disponível! Quer combinações?"
            ])})

        if tem(msg, ["fita 9", "n9", "nº9"]):
            user["topico"] = "fita9"
            user["esperando"] = "sugestao"
            return jsonify({"resposta": escolher([
                "Sim 😊 temos fita nº9!",
                "Temos sim 😍 ótima pra laços grandes!",
                "Sim 😄 disponível! Quer sugestões?"
            ])})

        if tem(msg, ["cola"]):
            user["topico"] = "cola"
            user["esperando"] = "dica"
            return jsonify({"resposta": escolher([
                "Sim 😊 temos cola quente! Quer dica de uso?",
                "Temos sim 😍 essencial pra acabamento!",
                "Sim 😄 cola disponível! Quer ajuda?"
            ])})

        if tem(msg, ["acrílico", "nome acrílico"]):
            user["topico"] = "acrilico"
            user["esperando"] = "detalhes"
            return jsonify({"resposta": escolher([
                "Sim 😊 fazemos nome em acrílico! Quer saber mais?",
                "Temos sim 😍 personalizado!",
                "Sim 😄 fazemos sob medida! Quer detalhes?"
            ])})

        # 🔥 RECOMENDAÇÃO
        if tem(msg, ["recomenda", "sugere", "o que comprar"]):
            user["estado"] = "recomendando"
            user["esperando"] = "perfil"
            return jsonify({"resposta": escolher([
                "Claro 😊 você tá começando?",
                "Posso ajudar 😄 quer algo básico ou completo?",
                "Boa 😍 você já trabalha com isso?"
            ])})

        # ✅ RESPOSTA PRA SIM (INTELIGENTE MESMO)
        if tem(msg, SIM):

            if user["esperando"] == "quer_cores":
                user["esperando"] = None
                return jsonify({"resposta": escolher([
                    "Rosa com branco vende muito 😍",
                    "Dourado com nude fica lindo 😊",
                    "Estampado + liso combina bastante 😄"
                ])})

            if user["esperando"] == "dica":
                return jsonify({"resposta": escolher([
                    "Use cola em pouca quantidade pra não marcar 😊",
                    "Dica: cola quente ajuda muito na durabilidade 😄",
                    "Evite excesso pra não manchar 😍"
                ])})

            if user["esperando"] == "perfil":
                user["esperando"] = "nivel"
                return jsonify({"resposta": escolher([
                    "Você é iniciante ou já vende? 😊",
                    "Quer algo simples ou mais completo? 😄",
                    "Me fala seu nível pra indicar melhor 😊"
                ])})

            if user["esperando"] == "nivel":
                return jsonify({"resposta": escolher([
                    "Recomendo fita nº5 + cola + acessórios 😊",
                    "Kit básico já resolve muita coisa 😍",
                    "Começa com fitas e cola 😄"
                ])})

            # fallback de SIM
            return jsonify({"resposta": escolher([
                "Perfeito 😊 quer ajuda com mais algo?",
                "Boa 😄 posso te ajudar em mais alguma coisa?",
                "Top 😍 quer ver mais produtos?"
            ])})

        # ❌ NÃO
        if tem(msg, NAO):
            user["esperando"] = None
            return jsonify({"resposta": escolher([
                "Sem problema 😊 posso te ajudar com outra coisa!",
                "Tranquilo 😄 se precisar é só falar!",
                "Beleza 😊 quer ver outro produto?"
            ])})

        # 🚚 ENTREGA
        if tem(msg, ["entrega", "frete", "envio"]):
            return jsonify({"resposta": escolher([
                "Enviamos pra todo o Brasil 🇧🇷😊",
                "Entrega nacional disponível 😄",
                "Sim 😊 enviamos pra todo o país!"
            ])})

        # 📞 WHATS
        if tem(msg, ["whatsapp", "contato"]):
            return jsonify({"resposta": f"Pode chamar aqui 😊 {whatsapp}"})

        # 💬 FALLBACK INTELIGENTE
        return jsonify({"resposta": escolher([
            "Posso te ajudar com fitas, cola ou acrílico 😊",
            "Quer recomendação ou tá procurando algo específico? 😄",
            "Me fala o que você precisa 😊",
            "Posso te sugerir produtos se quiser 😍"
        ])})

    except:
        return jsonify({"resposta": "Deu um errinho aqui 😅 pode tentar de novo?"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
