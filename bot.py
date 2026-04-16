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
    return tem(msg, ["sim", "quero", "claro", "pode", "ok", "bora"])

def tem_nao(msg):
    return tem(msg, ["não", "nao", "depois", "agora não"])

@app.route("/")
def home():
    return "Bot INSANO rodando 😈🔥"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("mensagem", "").lower()
    user_id = data.get("user_id", request.remote_addr)

    whatsapp = "https://wa.me/5521979027387"

    estado = usuarios.get(user_id, {
        "etapa": "inicio",
        "perfil": None,
        "interesse": None
    })

    etapa = estado["etapa"]

    # 🔁 RESPOSTAS UNIVERSAIS

    if tem(msg, ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
        return jsonify({"resposta": escolher([
            "Oi 😊 posso te ajudar a escolher materiais ou kits!",
            "Olá 😍 quer ajuda pra escolher produtos?",
            "Oi oi 😊 tá procurando algo específico ou quer sugestões?"
        ])})

    if tem(msg, ["whatsapp", "contato", "falar com alguém", "atendente"]):
        return jsonify({"resposta": f"Se preferir falar direto 😊 {whatsapp}"})

    if tem(msg, ["entrega", "frete", "envio"]):
        return jsonify({"resposta": escolher([
            "Enviamos para todo o Brasil 🇧🇷😊",
            "Fazemos envio para todo o país 😊",
            "Sim 😄 enviamos pra todo o Brasil!"
        ])})

    if tem(msg, ["obrigado", "valeu", "obg"]):
        return jsonify({"resposta": escolher([
            "Por nada 😊 qualquer coisa estou aqui!",
            "Imagina 😄 se precisar é só chamar!",
            "De nada 😊 quer ajuda com mais algo?"
        ])})

    # 🔎 PEDIDO DE RECOMENDAÇÃO (CORE DO BOT)
    if tem(msg, ["recomenda", "o que comprar", "sugestão", "sugere", "o que você indica"]):
        usuarios[user_id]["etapa"] = "recomendar"
        return jsonify({"resposta": escolher([
            "Claro 😊 você tá começando ou já trabalha com isso?",
            "Posso te ajudar 😄 você quer algo pra iniciar ou já vende?",
            "Perfeito 😍 você prefere kit pronto ou escolher materiais?",
            "Boa 😊 quer algo mais básico ou completo?"
        ])})

    # 👤 PERFIL AUTOMÁTICO
    if tem(msg, ["iniciante", "começando", "nunca fiz"]):
        usuarios[user_id]["perfil"] = "iniciante"
        usuarios[user_id]["etapa"] = "sugestao"
    
    if tem(msg, ["já vendo", "experiência", "trabalho com isso"]):
        usuarios[user_id]["perfil"] = "profissional"
        usuarios[user_id]["etapa"] = "sugestao"

    # 💡 SUGESTÕES INTELIGENTES
    if etapa == "sugestao":

        if estado["perfil"] == "iniciante":
            usuarios[user_id]["etapa"] = "detalhar"
            return jsonify({"resposta": escolher([
                "Pra começar bem 😊 recomendo fita nº5 + cola quente + acessórios básicos. Quer que eu te sugira combinações de cores?",
                "Kit básico seria perfeito 😍 fita nº5, cola e alguns acessórios. Quer ideias de cores?",
                "Começo ideal 😄 fita nº5 + cola + enfeites. Quer sugestões mais detalhadas?"
            ])})

        elif estado["perfil"] == "profissional":
            usuarios[user_id]["etapa"] = "detalhar"
            return jsonify({"resposta": escolher([
                "Como você já trabalha com isso 😊 recomendo fita nº5 e nº9 + cola profissional. Quer sugestões de combinações?",
                "Pra vender mais 😍 fita nº5 + nº9 + cores que estão em alta. Quer ideias?",
                "Boa 😄 recomendo materiais variados pra diversificar. Quer sugestões específicas?"
            ])})

    # 🎨 DETALHAMENTO
    if etapa == "detalhar":
        if tem_sim(msg):
            usuarios[user_id]["etapa"] = "finalizar"
            return jsonify({"resposta": escolher([
                "Sugestão: combina rosa + branco + dourado 😍 vende muito!",
                "Cores infantis tipo rosa e azul claro são ótimas 😊",
                "Estampadas + lisas combinam muito 😄"
            ]) + "\n\nSe quiser ajuda pra montar pedido 😊 " + whatsapp})

        elif tem_nao(msg):
            usuarios[user_id]["etapa"] = "finalizar"
            return jsonify({"resposta": escolher([
                "Sem problema 😊 posso te ajudar com mais alguma coisa!",
                "Tranquilo 😄 se precisar de ajuda é só falar!",
                "Beleza 😊 quer ver mais produtos?"
            ])})

        else:
            return jsonify({"resposta": escolher([
                "Quer sugestões de cores? 😊",
                "Posso te indicar combinações 😄",
                "Quer ideias pra montar produtos?"
            ])})

    # 🧴 PRODUTOS DIRETOS
    if tem(msg, ["cola"]):
        return jsonify({"resposta": escolher([
            "Cola quente é essencial 😊 recomendo sempre ter!",
            "Boa 😍 cola faz muita diferença no acabamento!",
            "Sim 😄 cola de qualidade ajuda muito!"
        ])})

    if tem(msg, ["fita"]):
        return jsonify({"resposta": escolher([
            "Fita nº5 e nº9 são as mais usadas 😊",
            "Boa 😍 fitas são a base de tudo!",
            "Top 😄 quer ajuda pra escolher cores?"
        ])})

    # 🛒 FINALIZAÇÃO SUAVE
    if etapa == "finalizar":
        if tem(msg, ["como comprar", "finalizar", "comprar"]):
            return jsonify({"resposta": escolher([
                "Você pode finalizar direto aqui no site 😊",
                "É só adicionar no carrinho e finalizar 😄",
                "Compra é feita aqui mesmo no site 😊"
            ])})

    # 🔚 FALLBACK INTELIGENTE
    return jsonify({"resposta": escolher([
        "Posso te ajudar a escolher materiais 😊",
        "Quer sugestões ou tá procurando algo específico? 😄",
        "Me fala o que você precisa 😊",
        "Quer ajuda pra montar seu pedido? 😍"
    ])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
