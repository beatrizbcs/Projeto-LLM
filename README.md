# Projeto LLM com Flask

Este projeto é um backend simples construído com Flask que integra a API de um LLM gratuito (utilizando a API de inferência do Hugging Face com o modelo `distilgpt2`). Ele recebe uma requisição POST no endpoint `/ask` com uma pergunta em formato JSON, adiciona um contexto especial e envia essa informação para a API, retornando a resposta gerada.

## Requisitos

- Python 3.x
- Virtualenv (opcional, mas recomendado)
- Bibliotecas: Flask, requests

## Estrutura do Projeto

```
projeto_LLM/
├── env/           # Ambiente virtual (não modifique)
├── src/           # Código-fonte (contém o arquivo app.py)
└── README.md      # Este arquivo
```

## Instalação e Configuração

1. Clone ou copie o projeto para sua máquina.
2. Navegue até o diretório do projeto:
   ```bash
   cd "C:\Backup onedrive\projeto_LLM"
   ```
3. Crie o ambiente virtual:
   ```bash
   python -m venv env
   ```
4. Ative o ambiente virtual:
   - No Windows:
     ```bash
     .\env\Scripts\activate
     ```
5. Instale as dependências:
   ```bash
   pip install Flask requests
   ```
6. (Opcional) Se você possuir uma chave de API para o Hugging Face, edite o arquivo `src/app.py` e insira a chave na variável `LLM_API_KEY`.

## Execução

Com o ambiente virtual ativo, execute:
```bash
python src/app.py
```
O servidor Flask iniciará em `http://127.0.0.1:5000`.

## Testando o Endpoint

Envie uma requisição POST para o endpoint `/ask` com o seguinte JSON:
```json
{ "question": "Qual é a capital do Brasil?" }
```

### Exemplos

- **Usando curl (no Windows, via curl.exe):**
  ```bash
  curl.exe -X POST http://127.0.0.1:5000/ask -H "Content-Type: application/json" -d '{ "question": "Qual é a capital do Brasil?" }'
  ```

- **Usando PowerShell com Invoke-RestMethod:**
  ```powershell
  Invoke-RestMethod -Uri "http://127.0.0.1:5000/ask" -Method POST -ContentType "application/json" -Body '{ "question": "Qual é a capital do Brasil?" }'
  ```

## Notas

- Este projeto está configurado para desenvolvimento. Em produção, utilize um servidor WSGI apropriado.
- A resposta do endpoint dependerá do funcionamento da API do Hugging Face e da qualidade do modelo `distilgpt2`.