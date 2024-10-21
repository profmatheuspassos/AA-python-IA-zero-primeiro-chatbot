from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'Você é um modelo amigável chamado Asimo.')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

print("Bem-vindo ao AsimoBot!")
mensagens = []
while True:
    pergunta = input("Mande sua mensagem para o Assistente: ")
    if pergunta.lower() == "x":
        break
    mensagens.append(("user", pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(("assistant", resposta))
    print(f"Bot: {resposta}")

print("Muito obrigado por usar o AsimoBot!")
# print("mensagens")