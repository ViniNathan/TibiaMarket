from src.depotActions import *
from src.marketActions import *
import json
import threading


def main():
    # Criar instância da classe DPactions e marketActions
    depot = DPactions()
    market = actionsMarket()

    # Criar threads para executar depotActions e marketActions
    depot_thread = threading.Thread(target=depot.run)
    market_thread = threading.Thread(target=market.run)

    # Iniciar a execução da thread depotActions
    depot_thread.start()
    # Aguardar a conclusão da thread depotActions antes de iniciar a thread marketActions
    depot_thread.join()
    # Iniciar a execução da thread marketActions
    market_thread.start()

if __name__ == "__main__":
    sleep(4)
    print("Iniciando o programa . . .")
    main()