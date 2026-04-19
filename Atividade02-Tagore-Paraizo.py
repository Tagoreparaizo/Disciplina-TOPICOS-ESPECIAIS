from machine import Pin
import time

led_vermelho = Pin(15, Pin.OUT)
led_verde = Pin(14, Pin.OUT)

btn_vermelho = Pin(16, Pin.IN, Pin.PULL_DOWN)
btn_verde = Pin(17, Pin.IN, Pin.PULL_DOWN)

print("Sistema iniciado. Aguardando interação...")

while True:
    if btn_vermelho.value() == 1:
        led_vermelho.value(1)
    else:
        led_vermelho.value(0)
        
    if btn_verde.value() == 1:
        led_verde.value(1)
    else:
        led_verde.value(0)
        
    time.sleep(0.05)