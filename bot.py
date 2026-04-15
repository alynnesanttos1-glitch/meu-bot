from openai import OpenAI

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def responder_cliente(mensagem):
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um vendedor simpático de uma loja de materiais para fazer laços. Sempre sugira produtos e seja educado."},
            {"role": "user", "content": mensagem}
        ]
    )
    
    return resposta.choices[0].message.content


# simulação de cliente
while True:
    msg = input("Olá! no que posso ajudar? ")
    if msg.lower() == "sair":
        break
    
    resposta = responder_cliente(msg)
    print("Bot:", resposta)
