from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

usuarios = {}

def escolher(lista):
    return random.choice(lista)

def normalizar(msg):
    return msg.lower().strip()

def tem(msg, palavras):
    return any(p in msg for p in palavras)

SIM = ["sim", "quero", "claro", "pode", "ok", "ss", "s"]
NAO = ["não", "nao", "n", "depois", "agora não"]

@app.route("/")
def home():
    return "Bot profissional ON 🔥"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = normalizar(data.get("mensagem", ""))
        user_id = data.get("user_id", request.remote_addr)

        whatsapp = "https://wa.me/5521979027387"

        if user_id not in usuarios:
            usuarios[user_id] = {
                "ultima_intencao": None,
                "contexto": None
            }

        estado = usuarios[user_id]

        # 🔁 SAUDAÇÃO
        if tem(msg, ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
            estado["ultima_intencao"] = "inicio"
            return jsonify({"resposta": escolher([
                "Oi 😊 posso te ajudar a escolher produtos!",
                "Olá 😍 quer ajuda com fitas, cola ou acrílico?",
                "Oi oi 😄 tá procurando algo específico?"
            ])})

        # 🛍️ PRODUTOS
        if tem(msg, ["fita", "n5", "nº5", "numero 5"]):
            estado["ultima_intencao"] = "produto_fita5"
            return jsonify({"resposta": escolher([
                "Sim 😊 temos fita nº5! Quer sugestões de cores?",
                "Temos sim 😍 fita nº5 vende muito!",
                "Sim 😄 fita nº5 disponível! quer ajuda pra escolher?"
            ])})

        if tem(msg, ["n9", "nº9", "numero 9"]):
            estado["ultima_intencao"] = "produto_fita9"
            return jsonify({"resposta": escolher([
                "Sim 😊 temos fita nº9!",
                "Temos sim 😍 ótima pra laços grandes!",
                "Sim 😄 fita nº9 disponível!"
            ])})

        if tem(msg, ["cola", "silicone"]):
            estado["ultima_intencao"] = "produto_cola"
            return jsonify({"resposta": escolher([
                "Sim 😊 temos cola quente!",
                "Temos sim 😍 cola é essencial!",
                "Sim 😄 cola disponível!"
            ])})

        if tem(msg, ["acrílico", "nome acrílico", "personalizado"]):
            estado["ultima_intencao"] = "produto_acrilico"
            return jsonify({"resposta": escolher([
                "Sim 😊 fazemos nomes em acrílico!",
                "Temos sim 😍 personalizado!",
                "Sim 😄 fazemos sob medida!"
            ])})

        # 🔥 RECOMENDAÇÃO
        if tem(msg, ["recomenda", "sugere", "o que comprar", "indica"]):
            estado["ultima_intencao"] = "recomendacao"
            return jsonify({"resposta": escolher([
                "Posso te recomendar 😊 você tá começando?",
                "Claro 😄 quer algo simples ou completo?",
                "Boa 😍 você já trabalha com isso?"
            ])})

        # ✅ SIM (INTELIGENTE)
        if tem(msg, SIM):
            if estado["ultima_intencao"] == "produto_fita5":
                return jsonify({"resposta": escolher([
                    "Temos várias cores lindas 😊 quer sugestão?",
                    "Quer ajuda pra combinar cores? 😄",
                    "Posso te indicar cores que vendem bem 😍"
                ])})

            if estado["ultima_intencao"] == "produto_cola":
                return jsonify({"resposta": escolher([
                    "Cola ajuda muito no acabamento 😊",
                    "Boa escolha 😄 quer dica de uso?",
                    "É essencial mesmo 😍"
                ])})

            if estado["ultima_intencao"] == "recomendacao":
                estado["contexto"] = "perfil"
                return jsonify({"resposta": escolher([
                    "Você tá começando ou já vende? 😊",
                    "Você quer algo básico ou completo? 😄",
                    "Me fala seu nível pra eu te indicar melhor 😊"
                ])})

            if estado["contexto"] == "perfil":
                return jsonify({"resposta": escolher([
                    "Recomendo fita nº5 + cola + acessórios 😊",
                    "Kit básico já resolve muita coisa 😍",
                    "Começa com fitas e cola 😄"
                ])})

        # ❌ NÃO
        if tem(msg, NAO):
            return jsonify({"resposta": escolher([
                "Sem problema 😊 posso te ajudar com outra coisa!",
                "Tranquilo 😄 quer ver outro produto?",
                "Beleza 😊 qualquer coisa estou aqui!"
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

        # 🔚 FALLBACK
        return jsonify({"resposta": escolher([
            "Posso te ajudar com produtos 😊",
            "Quer sugestão ou tá procurando algo? 😄",
            "Me fala o que você precisa 😊",
            "Quer que eu te recomende algo? 😍"
        ])})

    except Exception as e:
        return jsonify({"resposta": "Ops 😅 deu um erro aqui, pode tentar de novo?"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
