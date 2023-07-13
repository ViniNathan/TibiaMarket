from src.depotActions import *
from src.marketActions import *
from src.record import *
from src.npcActions import *
from src.searchItems import *
import threading

def start_keyboard():
        with Listener(on_press=target_key) as listener:
            listener.join()

def target_key(key):
        if key == keyboard.Key.esc:
            return False
        if key == keyboard.Key.delete:
            threading.Thread(target= main).start()

def main():
    # Solicitar ao usuário que escolha o NPC
    escolha_npc = input("Escolha o NPC (greenDjinn, blueDjinn ou rashid): ")

    # Verificar a escolha do usuário e atribuir à variável self.npc
    if escolha_npc == "greenDjinn" or escolha_npc == "blueDjinn" or escolha_npc == "rashid":
        depot = DPactions()
        market = actionsMarket(escolha_npc)
        items = SearchBoughtItems(escolha_npc)
    else:
        print("NPC inválido!")

    sleep(3)
    # Criar threads para executar depotActions e marketActions
    depot_thread = threading.Thread(target=depot.run)
    market_thread = threading.Thread(target=market.run)
    items_thread = threading.Thread(target=items.run)
    # Iniciar a execução da thread depotActions
    depot_thread.start()
    # Aguardar a conclusão da thread depotActions antes de iniciar a thread marketActions
    depot_thread.join()
    # Iniciar a execução da thread marketActions
    market_thread.start()
    # Aguardar a conclusão da thread marketActions antes de iniciar a thread SearchBoughtItems
    market_thread.join()
    # # Iniciar a execução da thread SearchBoughtItems
    items_thread.start()

if __name__ == "__main__":
    print("Iniciando o programa . . .")
    start_keyboard()