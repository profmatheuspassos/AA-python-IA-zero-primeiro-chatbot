from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq

_ = load_dotenv(find_dotenv())

chat = ChatGroq(model='llama-3.1-70b-versatile')
pergunta = input("O que você quer perguntar para o chatbot? --> ")
resposta = chat.invoke(pergunta)
print(resposta.content)


