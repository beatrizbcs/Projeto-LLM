from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LLM_API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
LLM_API_KEY = ""

@app.route("/ask", methods=["POST"])
def ask_llm():
    data = request.get_json()
    question = data.get("question", "")
    payload = {"inputs": "Imagine que você é um sábio conselheiro falando para crianças. " + question}
    headers = {"Authorization": f"Bearer {LLM_API_KEY}"} if LLM_API_KEY else {}
    response = requests.post(LLM_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and result and "generated_text" in result[0]:
            return jsonify({"answer": result[0]["generated_text"]})
        return jsonify({"answer": result})
    return jsonify({"error": "Erro na consulta da API."}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)