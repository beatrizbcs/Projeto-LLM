from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CONTEXT = "Este contexto é sobre história mundial. Use informações históricas para responder a pergunta."
API_KEY = "AIzaSyCTFv-8lSHTWfdLgCK9ihMTne8CMiq5t7s"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    user_question = data.get("pergunta", "")
    prompt = f"{CONTEXT}\nPergunta: {user_question}\nResposta:"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}
    
    response_api = requests.post(API_URL, headers=headers, json=payload)
    try:
        result = response_api.json()
        if "candidates" in result and isinstance(result["candidates"], list) and result["candidates"]:
            candidate = result["candidates"][0]
            generated_text = candidate.get("output") or candidate.get("content") or "Resposta não encontrada."
        else:
            generated_text = "Resposta não encontrada."
    except Exception as e:
        generated_text = f"Erro: {str(e)}"
        
    return jsonify({"resposta": generated_text})

if __name__ == '__main__':
    app.run(debug=True)