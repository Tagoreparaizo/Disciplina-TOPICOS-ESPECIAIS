import telebot
import os

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(token)

print('Digite o seu nome:')
nome = input()
print('Digite a sua idade:')
idade = input()
print('Digite o seu CPF')
n_cpf = input()


def send_telegram_msg(nome, idade, n_cpf):
    msg_final = ('''
                Confirmação de cadastro,
                Usuário: %s
                Nome: %s
                CPF: %s
                Obrigado por criar o seu cadastro!
                '''%(nome, idade, n_cpf))
    sent_msg = bot.send_message(id, msg_final, parse_mode="Markdown")

send_telegram_msg(nome, idade, n_cpf)