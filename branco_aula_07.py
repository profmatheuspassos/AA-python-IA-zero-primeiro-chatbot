from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

_ = load_dotenv(find_dotenv())

chat = ChatGroq(model='llama-3.1-70b-versatile')

loader = WebBaseLoader('https://dponapratica.com.br/2023/05/a-nova-abnt-nbr-iso-iec-27005-2023/') # O loader do LangChain sempre retorna uma lista

lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
    documento += doc.page_content

template = ChatPromptTemplate.from_messages({
    ('system', 'Você é um assistente amigável chamado Asimo e tem acesso às seguintes informações para dar as suas respostas: {documentos_informados}'),
    ('user', '{input}')
})

chain = template | chat

resposta = chain.invoke({'documentos_informados': documento, 'input': 'Quais as principais características da ISO 27005?'})

print(resposta.content)