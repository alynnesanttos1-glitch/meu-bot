from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Chat 🤖</h2>
    <input id='msg' placeholder='Digite aqui'>
    <button onclick='enviar()'>Enviar</button>
    <p id='resposta'></p>

    <script>
    async function enviar() {
        let msg = document.getElementById('msg').value;

        let res = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({mensagem: msg})
        });

        let data = await res.json();
        document.getElementById('resposta').innerText = data.resposta;
    }
    </script>
    """

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data["mensagem"]

    resposta = f"Você disse: {msg}"

    return jsonify({"resposta": resposta})

app.run(host="0.0.0.0", port=10000)
