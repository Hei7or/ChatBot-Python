import openai

chave_api = "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"

openai.api_key = chave_api

def enviar_mensagem(mensagem, Lista_mensagens=[]):
    Lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = Lista_mensagens,
    )
    return resposta["choices"] [0] ["mequemssage"]

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem:")
    if texto =="sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("ChatBot:",resposta["content"])
