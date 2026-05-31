import requests

token = '8935226070:AAHdIGnp7M2zf5t69r9tVBBP7QmU9u4KzpU'
chat_id = '1203313447'
mensagem = "Teste de envio via GET"

# Esta é a URL do Request GET
url_requisicao = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}"

# O comando que executa o request
resposta = requests.get(url_requisicao)

print(f"Código de Status: {resposta.status_code}") # Se aparecer 200, deu certo!