import telebot
import requests
import os
from dotenv import load_dotenv
load_dotenv()
# Replace ‘YOUR_API_TOKEN’ with the API token you received from the BotFather
API_TOKEN = os.getenv("TELEGRAM_TOKEN")
NIFI_URL = os.getenv("URL")

bot = telebot.TeleBot(API_TOKEN)

# Define a command handler
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    texto_recebido = message.text
    
    # Validação básica do padrão: Nome;Documento;Demanda
    if ';' in texto_recebido and texto_recebido.count(';') == 2:
        try:
            # Enviando para o NiFi via POST (Simulando o CURL)
            response = requests.post(NIFI_URL, data=texto_recebido.encode('utf-8'))
            
            if response.status_code == 200 or response.status_code == 201:
                bot.reply_to(message, "✅ Chamado enviado ao NiFi com sucesso!")
            else:
                bot.reply_to(message, f"⚠️ NiFi recebeu, mas retornou status: {response.status_code}")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro ao conectar no NiFi: {e}")
    else:
        bot.reply_to(message, "Formato inválido! Use: Nome;CPF;Demanda")




# Start the bot
bot.polling()