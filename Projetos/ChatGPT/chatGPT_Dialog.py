import openai

# Define sua chave de API
openai.api_key = 'sua_chave_de_api'


# Define o histórico de diálogo
historico = [
    {'role': 'system', 'content': 'Você é um assistente de atendimento ao cliente.'},
    {'role': 'user', 'content': 'Quero fazer uma reserva de hotel.'}
]

# Chama a função 'openai.Completion.create' para obter a resposta do modelo
resposta = openai.Completion.create(
    engine='text-davinci-003',
    prompt='ChatGPT',
    messages=historico,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Obtém a resposta gerada pelo modelo
resposta_modelo = resposta.choices[0].message['content']

# Imprime a resposta
print(resposta_modelo)