import asyncio
import random

class CentralConsenso:
    def __init__(self):
        self.leituras = {}
        self.lock = asyncio.Lock()
        self.evento_atualizacao = asyncio.Event()

    async def receber_leitura(self, sensor_nome: str, temp: int):
        async with self.lock:
            self.leituras[sensor_nome] = temp
            

            if len(self.leituras) == 3:
                self.evento_atualizacao.set()

    async def processar_media(self):
        while True:
            await self.evento_atualizacao.wait()
            
            async with self.lock:
                media = sum(self.leituras.values()) / 3
                print(f"\n[!] Atualização - Últimos Dados: {self.leituras}")
                print(f"[*] Nova Temperatura Média: {media:.2f}°C\n")
                

                self.evento_atualizacao.clear()

class Sensor:
    def __init__(self, nome: str, timer: int, qtd: int, central: CentralConsenso):
        self.nome = nome
        self.timer = timer
        self.qtd = qtd
        self.central = central

    async def iniciar_sensor(self):
        for _ in range(self.qtd):
            await asyncio.sleep(self.timer)
            temperatura = random.randint(20, 40)
            
            print(f"{self.nome} mediu {temperatura}°C")
            await self.central.receber_leitura(self.nome, temperatura)

async def main():
    central = CentralConsenso()
    
    tarefas = [
        asyncio.create_task(Sensor("Sensor A", 2, 5, central).iniciar_sensor()),
        asyncio.create_task(Sensor("Sensor B", 3, 5, central).iniciar_sensor()),
        asyncio.create_task(Sensor("Sensor C", 4, 5, central).iniciar_sensor())
    ]
    
    monitor = asyncio.create_task(central.processar_media())
    
    await asyncio.gather(*tarefas)
    monitor.cancel()

if __name__ == '__main__':
    print("--- Iniciando Rede de Sensores (Monitoramento Contínuo) ---")
    asyncio.run(main())