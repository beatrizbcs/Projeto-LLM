# Projeto Backend de Consulta a API LLM Gemini

Este projeto é um backend simples desenvolvido com Flask, que consulta a API do Gemini (Google AI Studio) para gerar respostas a perguntas com base em um contexto pré-definido – neste caso, sobre **história mundial**. O backend recebe uma pergunta via requisição POST, envia o prompt (que inclui o contexto e a pergunta) para a API do Gemini e retorna a resposta gerada em formato JSON.

## Funcionalidades

- **Contextualização**: O projeto utiliza um contexto específico para moldar as respostas.
- **Integração com API**: Consulta a API do Gemini utilizando a API key fornecida.
- **Resposta em JSON**: Processa e extrai o texto gerado da resposta da API, retornando-o ao cliente.

## Pré-requisitos

- **Python 3.x**  
  Certifique-se de ter o Python instalado. [Download Python](https://www.python.org/downloads/)
  
- **Pip**  
  O gerenciador de pacotes do Python para instalar as dependências.

- **Conta e API Key para o Gemini**  
  Este projeto utiliza uma API key que já está incluída no código para testes. Em um ambiente real, recomenda-se que a chave seja armazenada de forma segura (por exemplo, em variáveis de ambiente).

## Estrutura do Projeto

- **app.py**: contém o código do servidor Flask que trata das requisições e integra com a API do Gemini.
- **requirements.txt**: lista as dependências necessárias (Flask e requests).
- **README.md**: este arquivo que documenta o projeto, instruções de configuração e testes.