from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

usuarios = {}

def escolher(lista):
    return random.choice(lista)

@app.route("/")
def home():
    return "Bot online 😈"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("mensagem", "").lower()
    user_id = data.get("user_id", request.remote_addr)

    whatsapp = "https://wa.me/5521979027387"
    site = "https://fazendoarte.com"

    estado = usuarios.get(user_id, "inicio")

    # 👋 INÍCIO
    if estado == "inicio":
        usuarios[user_id] = "perfil"
        return jsonify({
            "resposta": escolher([
                "Oi! 😊 Seja bem-vinda! Você trabalha com laços ou tá começando agora?",
                "Olá 😍 você já faz laços ou quer começar agora?",
                "Oi oi 😊 você já trabalha com artesanato ou tá iniciando?"
            ])
        })

    # 👩 PERFIL
    elif estado == "perfil":
        if "começ" in msg or "iniciante" in msg:
            usuarios[user_id] = "kit"
            return jsonify({
                "resposta": escolher([
                    "Que legal 😍 quer que eu te recomende um kit completo pra começar?",
                    "Perfeito 😊 posso te indicar um kit pronto com tudo que precisa!",
                    "Top 😍 quer uma sugestão de kit pra iniciantes?"
                ])
            })
        else:
            usuarios[user_id] = "tipo_fita"
            return jsonify({
                "resposta": escolher([
                    "Perfeito 😍 você usa mais fita número 5 ou 9?",
                    "Show 😊 trabalha mais com fita nº5 ou nº9?",
                    "Boa 😍 qual tamanho você usa mais: 5 ou 9?"
                ])
            })

    # 🎁 KIT
    elif estado == "kit":
        if "sim" in msg:
            usuarios[user_id] = "finalizar"
            return jsonify({
                "resposta": escolher([
                    "Recomendo um kit com fita nº5 + cola quente + acessórios 😍 quer finalizar a compra?",
                    "Kit perfeito seria fita + cola + básicos 😊 quer fechar o pedido agora?",
                    "Tenho um kit ótimo pra você começar 😍 quer finalizar já?"
                ])
            })
        else:
            usuarios[user_id] = "tipo_fita"
            return jsonify({
                "resposta": escolher([
                    "Sem problema 😊 então quer ver fitas separadas?",
                    "Beleza 😄 vamos ver fitas então! Você prefere nº5 ou nº9?",
                    "Tranquilo 😎 vamos escolher fitas! Qual tamanho você quer?"
                ])
            })

    # 🎀 TIPO DE FITA
    elif estado == "tipo_fita":
        if "5" in msg:
            usuarios[user_id] = "recomendar_fita"
            return jsonify({
                "resposta": escolher([
                    "Fita nº5 é ótima 😍 quer que eu te recomende algumas que estão vendendo muito?",
                    "Boa escolha 😊 quer sugestões de fita nº5?",
                    "Top 😍 tenho várias nº5 lindas! Quer recomendações?"
                ])
            })
        elif "9" in msg:
            usuarios[user_id] = "recomendar_fita"
            return jsonify({
                "resposta": escolher([
                    "Fita nº9 é perfeita 😍 quer ver recomendações?",
                    "Excelente 😊 nº9 vende muito! Quer sugestões?",
                    "Boa 😍 quer ideias de fita nº9?"
                ])
            })
        else:
            return jsonify({
                "resposta": "Você prefere fita nº5 ou nº9? 😊"
            })

    # 💡 RECOMENDAÇÃO
    elif estado == "recomendar_fita":
        if "sim" in msg:
            usuarios[user_id] = "finalizar"
            return jsonify({
                "resposta": escolher([
                    "Recomendo gorgurão candy + estampadas 😍 quer finalizar?",
                    "Sugiro fitas lisas + temáticas 😊 quer fechar o pedido?",
                    "Essas estão vendendo muito 😍 quer finalizar agora?"
                ])
            })
        else:
            usuarios[user_id] = "outros"
            return jsonify({
                "resposta": escolher([
                    "Beleza 😊 quer ver cola ou outros materiais?",
                    "Tranquilo 😄 posso te mostrar colas ou acessórios!",
                    "Sem problema 😎 quer ver outros produtos?"
                ])
            })

    # 🧴 OUTROS
    elif estado == "outros":
        if "cola" in msg:
            usuarios[user_id] = "finalizar"
            return jsonify({
                "resposta": escolher([
                    "Temos cola quente ótima 🔥 quer adicionar e finalizar?",
                    "Cola de qualidade faz diferença 😍 quer incluir no pedido?",
                    "Recomendo cola boa 😊 quer fechar o pedido?"
                ])
            })
        else:
            return jsonify({
                "resposta": escolher([
                    "Posso te ajudar com fitas, colas ou kits 😍",
                    "Quer ver mais produtos? 😊",
                    "Me fala o que você precisa 😄"
                ])
            })

    # 🛒 FINAL
    elif estado == "finalizar":
        if "sim" in msg or "quero" in msg:
            usuarios[user_id] = "fim"
            return jsonify({
                "resposta": escolher([
                    f"Perfeito 😍 finalize pelo site: {site} 🛒 ou chama no Whats: {whatsapp}",
                    f"Top 😊 pode finalizar aqui: {site} ou falar comigo no Whats: {whatsapp}",
                    f"Compra fácil 😍 finalize no site: {site} ou no Whats: {whatsapp}"
                ])
            })
        else:
            return jsonify({
                "resposta": escolher([
                    "Sem problema 😊 quer ver mais produtos?",
                    "Tranquilo 😄 posso te mostrar outras opções!",
                    "Beleza 😎 quer continuar olhando?"
                ])
            })

    return jsonify({"resposta": "Não entendi 😅 quer ver fitas, colas ou kits?"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
