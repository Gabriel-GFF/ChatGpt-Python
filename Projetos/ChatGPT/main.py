import openai
from time import sleep
import dados

while True:
    # Define a mensagem que você deseja enviar para o ChatGPT
    dados.Dados.menssagem = str(input("[Sair = XXX] Qual a sua pergunta?: "))
    if dados.Dados.menssagem.upper() in "XXX":
        print("Finalizando", end='')
        for x in range(0, 3):
            sleep(0.7)
            print('.', end='')
        break
    YOUR_API_KEY = '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'

    # Define sua chave de API
    openai.api_key = YOUR_API_KEY

    # Chama a função 'openai.Completion.create' para obter a resposta do modelo
    resposta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=dados.Dados.menssagem,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Obtém a resposta gerada pelo modelo
    resposta_modelo = resposta.choices[0].text.strip()

    # Imprime a resposta
    print(resposta_modelo)
