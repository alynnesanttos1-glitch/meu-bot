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
    return "Bot online 😈🔥 CRITICAL HIT"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("mensagem", "").lower()
    user_id = data.get("user_id", request.remote_addr)

    whatsapp = "https://wa.me/5521979027387"
    site = "https://fazendoarte.com"

    estado = usuarios.get(user_id, {"etapa": "inicio", "interesse": None})

    etapa = estado["etapa"]

    # 👋 INÍCIO
    if etapa == "inicio":
        usuarios[user_id] = {"etapa": "perfil", "interesse": None}
        return jsonify({
            "resposta": escolher([
                "Oi! 😊 Seja bem-vinda! Você já trabalha com laços ou tá começando agora?",
                "Olá 😍 você já faz laços ou quer começar? Tenho kits que ajudam MUITO 😉",
                "Oi oi 😊 você trabalha com artesanato ou tá iniciando agora?"
            ])
        })

    # 👩 PERFIL
    elif etapa == "perfil":
        if "começ" in msg or "iniciante" in msg:
            usuarios[user_id] = {"etapa": "kit", "interesse": "iniciante"}
            return jsonify({
                "resposta": escolher([
                    "Perfeito 😍 quem começa com kit aprende MUITO mais rápido! Quer que eu te recomende um kit pronto?",
                    "Boa escolha 😍 tenho kits completos que facilitam demais! Quer ver?",
                    "Top 😊 posso te indicar um kit que já vem com tudo pra começar! Quer?"
                ])
            })
        else:
            usuarios[user_id] = {"etapa": "tipo_fita", "interesse": "profissional"}
            return jsonify({
                "resposta": escolher([
                    "Que top 😍 você usa mais fita nº5 ou nº9? As duas estão vendendo MUITO!",
                    "Perfeito 😊 você trabalha mais com fita 5 ou 9? Posso te indicar as mais procuradas!",
                    "Boa 😍 qual você usa mais: nº5 ou nº9?"
                ])
            })

    # 🎁 KIT (COM PRESSÃO LEVE)
    elif etapa == "kit":
        if "sim" in msg:
            usuarios[user_id]["etapa"] = "finalizar"
            return jsonify({
                "resposta": escolher([
                    "Perfeito 😍 esse kit é o que mais ajuda iniciantes e tá saindo MUITO! Quer que eu já deixe pronto pra você finalizar?",
                    "Ótima escolha 😊 esse kit facilita MUITO no começo! Quer finalizar agora?",
                    "Esse kit é campeão de vendas 😍 quer garantir o seu agora?"
                ])
            })
        else:
            usuarios[user_id]["etapa"] = "tipo_fita"
            return jsonify({
                "resposta": escolher([
                    "Tranquilo 😊 então vamos nas fitas! Você prefere nº5 ou nº9?",
                    "Beleza 😄 vamos ver fitas então! Qual você usa mais?",
                    "Sem problema 😎 fita nº5 ou nº9?"
                ])
            })

    # 🎀 TIPO DE FITA
    elif etapa == "tipo_fita":
        if "5" in msg:
            usuarios[user_id]["etapa"] = "recomendar"
            usuarios[user_id]["interesse"] = "fita5"
            return jsonify({
                "resposta": escolher([
                    "Boa 😍 fita nº5 vende MUITO! Quer que eu te mostre as mais procuradas?",
                    "Excelente escolha 😊 nº5 é sucesso! Quer recomendações?",
                    "Top 😍 tenho umas nº5 lindas que saem rápido! Quer ver?"
                ])
            })
        elif "9" in msg:
            usuarios[user_id]["etapa"] = "recomendar"
            usuarios[user_id]["interesse"] = "fita9"
            return jsonify({
                "resposta": escolher([
                    "Perfeito 😍 nº9 é ótimo pra laços grandes! Quer recomendações?",
                    "Boa 😊 fita nº9 tá bombando! Quer sugestões?",
                    "Top 😍 quer ver as nº9 mais vendidas?"
                ])
            })
        else:
            return jsonify({"resposta": "Você prefere fita nº5 ou nº9? 😊"})

    # 💡 RECOMENDAÇÃO INTELIGENTE
    elif etapa == "recomendar":
        if "sim" in msg:
            usuarios[user_id]["etapa"] = "combo"
            return jsonify({
                "resposta": escolher([
                    "Recomendo gorgurão + estampadas 😍 combina muito! Quer que eu sugira um combo com cola também?",
                    "Essas estão vendendo MUITO 😍 quer aproveitar e ver um combo completo?",
                    "Top 😊 posso montar um kit com isso + cola pra você economizar! Quer?"
                ])
            })
        else:
            usuarios[user_id]["etapa"] = "outros"
            return jsonify({
                "resposta": escolher([
                    "Sem problema 😊 quer ver colas ou acessórios?",
                    "Tranquilo 😄 posso te mostrar outros materiais!",
                    "Beleza 😎 quer ver mais opções?"
                ])
            })

    # 💥 COMBO (CRITICAL HIT)
    elif etapa == "combo":
        if "sim" in msg:
            usuarios[user_id]["etapa"] = "finalizar"
            return jsonify({
                "resposta": escolher([
                    "Perfeito 😍 esse combo tá saindo MUITO e compensa demais! Quer finalizar agora?",
                    "Boa escolha 😊 você já sai com tudo pronto! Quer fechar o pedido?",
                    "Esse combo é sucesso total 😍 quer garantir o seu agora?"
                ])
            })
        else:
            usuarios[user_id]["etapa"] = "finalizar"
            return jsonify({
                "resposta": escolher([
                    "Sem problema 😊 mas recomendo pegar pelo menos fita + cola 😉 quer finalizar?",
                    "Tranquilo 😄 quer fechar com o que escolheu?",
                    "Beleza 😎 quer finalizar sua compra?"
                ])
            })

    # 🛒 FINALIZAÇÃO COM PRESSÃO LEVE
    elif etapa == "finalizar":
        if "sim" in msg or "quero" in msg:
            usuarios[user_id]["etapa"] = "fim"
            return jsonify({
                "resposta": escolher([
                    f"Perfeito 😍 finalize aqui: {site} 🛒\nSe precisar, chama no Whats: {whatsapp}",
                    f"Boa 😍 pode finalizar direto no site: {site} 🛒\nOu falar comigo no Whats: {whatsapp}",
                    f"Top 😊 finaliza rapidinho aqui: {site} 🛒\nQualquer dúvida: {whatsapp}"
                ])
            })
        else:
            return jsonify({
                "resposta": escolher([
                    "Quer ver mais alguma coisa antes? 😊",
                    "Posso te ajudar com mais produtos 😍",
                    "Quer que eu te sugira mais alguma coisa?"
                ])
            })

    return jsonify({"resposta": "Posso te ajudar com fitas, colas ou kits 😍"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
