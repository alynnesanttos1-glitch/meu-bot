from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

usuarios = {}

def escolher(lista):
    return random.choice(lista)

def tem(msg, lista):
    return any(p in msg for p in lista)

def tem_sim(msg):
    return any(p in msg for p in ["sim", "quero", "claro", "pode", "ok", "quero sim", "ss"])

def tem_nao(msg):
    return any(p in msg for p in ["não", "nao", "depois", "agora não", "n"])

@app.route("/")
def home():
    return "Bot 200% melhorado 🔥"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("mensagem", "").lower()
    user_id = data.get("user_id", request.remote_addr)

    whatsapp = "https://wa.me/5521979027387"

    if user_id not in usuarios:
        usuarios[user_id] = {
            "etapa": "inicio",
            "ultima_pergunta": None
        }

    estado = usuarios[user_id]

    # 🔁 SAUDAÇÃO
    if tem(msg, ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
        estado["ultima_pergunta"] = "inicio"
        return jsonify({"resposta": escolher([
            "Oi 😊 quer ajuda pra escolher materiais ou kits?",
            "Olá 😍 posso te recomendar produtos!",
            "Oi oi 😊 tá procurando algo ou quer sugestões?"
        ])})

    # 🔎 PRODUTOS (AGORA MUITO MELHOR)
    if tem(msg, ["fita", "n5", "nº5", "numero 5", "fita 5"]):
        estado["ultima_pergunta"] = "produto"
        return jsonify({"resposta": escolher([
            "Sim 😊 temos fita nº5 sim! Quer sugestão de cores?",
            "Temos sim 😍 fita nº5 é uma das mais usadas! Quer ver combinações?",
            "Sim 😄 fita nº5 disponível! Quer que eu te recomende cores?"
        ])})

    if tem(msg, ["n9", "nº9", "numero 9", "fita 9"]):
        estado["ultima_pergunta"] = "produto"
        return jsonify({"resposta": escolher([
            "Sim 😊 temos fita nº9! ótima pra laços grandes!",
            "Temos sim 😍 nº9 vende muito!",
            "Sim 😄 fita nº9 disponível! quer sugestões?"
        ])})

    if tem(msg, ["cola", "cola quente", "silicone"]):
        estado["ultima_pergunta"] = "produto"
        return jsonify({"resposta": escolher([
            "Sim 😊 temos cola quente sim! ajuda MUITO no acabamento!",
            "Temos sim 😍 cola é essencial!",
            "Sim 😄 cola disponível! quer dica de uso?"
        ])})

    if tem(msg, ["acrílico", "nome acrílico", "nome personalizado"]):
        estado["ultima_pergunta"] = "produto"
        return jsonify({"resposta": escolher([
            "Sim 😊 fazemos nome em acrílico sim! quer saber mais?",
            "Temos sim 😍 nome acrílico personalizado!",
            "Sim 😄 fazemos nomes em acrílico! quer detalhes?"
        ])})

    # 🔥 RECOMENDAÇÃO INTELIGENTE
    if tem(msg, ["recomenda", "sugere", "o que comprar", "o que você indica"]):
        estado["ultima_pergunta"] = "recomendacao"
        return jsonify({"resposta": escolher([
            "Posso te recomendar sim 😊 você tá começando?",
            "Claro 😍 você quer algo básico ou completo?",
            "Boa 😄 você já trabalha com isso ou tá começando?"
        ])})

    # 🧠 RESPOSTA INTELIGENTE PRA SIM
    if tem_sim(msg):

        if estado["ultima_pergunta"] == "produto":
            return jsonify({"resposta": escolher([
                "Perfeito 😊 quer ajuda pra escolher cores ou quantidades?",
                "Boa 😄 quer sugestão pra combinar melhor?",
                "Top 😍 posso te ajudar a montar seu pedido!"
            ])})

        if estado["ultima_pergunta"] == "recomendacao":
            estado["ultima_pergunta"] = "perfil"
            return jsonify({"resposta": escolher([
                "Você tá começando ou já vende? 😊",
                "Você quer algo simples ou mais completo? 😄",
                "Me fala se você é iniciante ou já trabalha com isso 😊"
            ])})

        if estado["ultima_pergunta"] == "perfil":
            return jsonify({"resposta": escolher([
                "Recomendo fita nº5 + cola + acessórios 😊",
                "Kit básico é uma ótima escolha 😍",
                "Você pode começar com fitas e cola 😄"
            ])})

    # ❌ RESPOSTA PRA NÃO
    if tem_nao(msg):
        return jsonify({"resposta": escolher([
            "Sem problema 😊 posso te ajudar com outra coisa!",
            "Tranquilo 😄 quer ver outro produto?",
            "Beleza 😊 se precisar é só falar!"
        ])})

    # 📦 ENTREGA
    if tem(msg, ["entrega", "frete", "envio"]):
        return jsonify({"resposta": escolher([
            "Enviamos pra todo o Brasil 🇧🇷😊",
            "Fazemos envio nacional 😄",
            "Sim 😊 entregamos em todo o país!"
        ])})

    # 📞 WHATS
    if tem(msg, ["whatsapp", "contato", "falar com alguém"]):
        return jsonify({"resposta": f"Pode chamar aqui 😊 {whatsapp}"})

    # 💬 FALLBACK MELHORADO
    return jsonify({"resposta": escolher([
        "Posso te ajudar com fitas, cola ou acrílico 😊",
        "Quer recomendação ou tá procurando algo específico? 😄",
        "Me fala o que você precisa 😊",
        "Posso te sugerir produtos se quiser 😍"
    ])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
