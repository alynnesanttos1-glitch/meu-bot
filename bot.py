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

@app.route("/")
def home():
    return "Bot automático ON 🔥"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("mensagem", "").lower()
    user_id = data.get("user_id", request.remote_addr)

    whatsapp = "https://wa.me/5521979027387"
    site = "https://fazendoarte.com"

    estado = usuarios.get(user_id, {"etapa": "inicio"})
    etapa = estado["etapa"]

    # 🔁 RESPOSTAS UNIVERSAIS (FUNCIONA EM QUALQUER ETAPA)
    if tem(msg, ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
        return jsonify({"resposta": escolher([
            "Oi 😊 tudo bem? Você já trabalha com laços ou tá começando?",
            "Olá 😍 seja bem-vinda! Posso te ajudar com fitas, kits ou materiais!",
            "Oi oi 😊 quer ajuda com laços ou materiais?"
        ])})

    if tem(msg, ["entrega", "frete", "envio"]):
        return jsonify({"resposta": escolher([
            f"Enviamos pra todo o Brasil 🇧🇷😊 você pode finalizar no site: {site} ou falar no Whats: {whatsapp}",
            f"Fazemos envio para todo o país 😊 finalize no site ou chama no Whats: {whatsapp}",
            f"Sim 😄 enviamos pra todo o Brasil! Pode finalizar aqui: {site}"
        ])})

    if tem(msg, ["whatsapp", "contato", "numero"]):
        return jsonify({"resposta": f"Pode chamar aqui 😊 {whatsapp}"})

    if tem(msg, ["site", "comprar", "pedido"]):
        return jsonify({"resposta": f"Você pode ver e finalizar tudo aqui 🛒 {site}"})

    if tem(msg, ["obrigado", "obg", "valeu"]):
        return jsonify({"resposta": escolher([
            "De nada 😊 qualquer coisa estou por aqui!",
            "Imagina 😄 se precisar é só chamar!",
            "Por nada 😊 posso te ajudar com mais algo?"
        ])})

    # 👤 PERFIL
    if tem(msg, ["iniciante", "começando", "nunca fiz"]):
        usuarios[user_id]["etapa"] = "iniciante"
        return jsonify({"resposta": escolher([
            "Perfeito 😍 recomendo começar com um kit completo! Quer ver?",
            "Boa 😊 kit inicial ajuda MUITO! Quer recomendação?",
            "Top 😄 tenho kits ideais pra quem tá começando! Quer?"
        ])})

    if tem(msg, ["já vendo", "experiência", "trabalho com isso"]):
        usuarios[user_id]["etapa"] = "profissional"
        return jsonify({"resposta": escolher([
            "Que top 😍 você usa mais fita nº5 ou nº9?",
            "Boa 😊 trabalha mais com fita 5 ou 9?",
            "Perfeito 😄 prefere nº5 ou nº9?"
        ])})

    # 🎁 KIT
    if etapa == "iniciante":
        if tem(msg, ["sim", "quero", "pode"]):
            usuarios[user_id]["etapa"] = "finalizar"
            return jsonify({"resposta": escolher([
                f"Perfeito 😍 você pode pegar um kit completo aqui: {site} 🛒",
                f"Boa 😊 kit completo já resolve tudo! finalize aqui: {site}",
                f"Ótima escolha 😄 finalize pelo site: {site}"
            ])})
        elif tem(msg, ["não", "depois"]):
            usuarios[user_id]["etapa"] = "livre"
            return jsonify({"resposta": "Sem problema 😊 quer ver fitas ou outros materiais?"})

    # 🎀 FITAS
    if tem(msg, ["fita", "n5", "nº5", "5"]):
        usuarios[user_id]["etapa"] = "fita5"
        return jsonify({"resposta": escolher([
            "Fita nº5 é ótima 😊 quer ver opções no site?",
            f"Boa 😍 nº5 vende muito! olha aqui: {site}",
            "Top 😄 quer recomendações de cores?"
        ])})

    if tem(msg, ["n9", "nº9", "9"]):
        usuarios[user_id]["etapa"] = "fita9"
        return jsonify({"resposta": escolher([
            "Fita nº9 é perfeita pra laços grandes 😊 quer ver?",
            f"Boa 😍 nº9 tá saindo muito! olha aqui: {site}",
            "Top 😄 quer sugestões de cores?"
        ])})

    # 🎨 CORES
    if tem(msg, ["cor", "cores", "rosa", "azul", "preto"]):
        return jsonify({"resposta": escolher([
            "Temos várias cores lindas 😍 quer ver no site?",
            f"Tem muitas opções 😊 dá uma olhada aqui: {site}",
            "Cores estão muito bonitas 😄 quer sugestão de combinação?"
        ])})

    # 🧴 COLA / ACESSÓRIOS
    if tem(msg, ["cola", "silicone", "acessório"]):
        return jsonify({"resposta": escolher([
            "Temos cola quente ótima 😊 quer ver no site?",
            f"Boa 😍 cola ajuda muito! olha aqui: {site}",
            "Tem vários acessórios úteis 😄 quer ver?"
        ])})

    # 💬 INDECISÃO
    if tem(msg, ["não sei", "talvez", "vendo ainda"]):
        return jsonify({"resposta": escolher([
            "Sem problema 😊 posso te ajudar a escolher!",
            "Tranquilo 😄 quer que eu te sugira algo?",
            "Posso te recomendar algo baseado no que você quer 😊"
        ])})

    # 🛒 FINALIZAÇÃO
    if tem(msg, ["finalizar", "comprar", "fechar"]):
        return jsonify({"resposta": escolher([
            f"Perfeito 😊 finalize aqui: {site} 🛒",
            f"Boa 😍 pode finalizar direto no site: {site}",
            f"Qualquer dúvida chama no Whats: {whatsapp}"
        ])})

    # 🔚 FALLBACK INTELIGENTE
    return jsonify({"resposta": escolher([
        "Posso te ajudar com kits, fitas ou acessórios 😊",
        "Quer ver produtos ou tirar alguma dúvida? 😄",
        "Estou aqui pra te ajudar 😊 o que você procura?"
    ])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
