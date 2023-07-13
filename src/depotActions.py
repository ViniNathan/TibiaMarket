import threading
from src.screen import *
from src.mouseActions import Actions
from time import sleep
from pynput.keyboard import Listener
from pynput import keyboard


class DPactions():
    def __init__(self):
        self.WindowName = "Projetor em tela cheia (prévia)"
        self.actions = Actions()
        
    def depotTileFinder(self):
        # Encontra um depot vazio (sem player)
        depotTilePath = "images/depotImages/depotTile.png"
        depotTileLocation = LocateImageCenter(depotTilePath, self.WindowName)

        if depotTileLocation is not None:
            print("O DP vazio foi encontrado na posição:", depotTileLocation)
            self.actions.move_and_left_click(depotTileLocation)
            sleep(4)
        else:
            sleep(5)
            self.depotTileFinder()

    def depositFinder(self):
        # Busca o depot esquerdo do DP
        leftPlayerDepotPath = "images/depotImages/leftPlayerDepot.png"
        leftDepotLocation = LocateImageCenter(leftPlayerDepotPath, self.WindowName)

        if leftDepotLocation is not None:
            print("O DP da esquerda foi encontrado na posição:", leftDepotLocation)
            pyautogui.moveTo(leftDepotLocation)
            sleep(1)
            pyautogui.rightClick()
        else:
            # Busca o depot direito do DP
            rightPlayerDepotPath = "images/depotImages/rightPlayerDepot.png"
            rightDepotLocation = LocateImageCenter(rightPlayerDepotPath, self.WindowName)
            if rightDepotLocation is not None:
                print("O DP da direita foi encontrado na posição:", rightDepotLocation)
                pyautogui.moveTo(rightDepotLocation)
                sleep(1)
                pyautogui.rightClick()
            else:
                # Busca o depot de cima do DP
                topPlayerDepotPath = "images/depotImages/topPlayerDepot.png"
                topDepotLocation = LocateImageCenter(topPlayerDepotPath, self.WindowName)
                if topDepotLocation is not None:
                    print("O DP de cima foi encontrado na posição:", topDepotLocation)
                    pyautogui.moveTo(topDepotLocation)
                    sleep(1)
                    pyautogui.rightClick()
                else:
                    # Busca o depot de baixo do DP
                    bottomPlayerDepotPath = "images/depotImages/bottomPlayerDepot.png"
                    bottomDepotLocation = LocateImageCenter(bottomPlayerDepotPath, self.WindowName)
                    if bottomDepotLocation is not None:
                        print("O DP de baixo foi encontrado na posição:", bottomDepotLocation)
                        pyautogui.moveTo(bottomDepotLocation)
                        sleep(1)
                        pyautogui.rightClick()
        sleep(1)
                
    def marketFinder(self):
        marketPath = "images/depotImages/market.png"
        marketLocation = LocateImageCenter(marketPath, self.WindowName)
        if marketLocation is not None:
            print("O market foi encontrado na posição:", marketLocation)
            pyautogui.moveTo(marketLocation)
            sleep(0.5)
            pyautogui.rightClick()

    def start_keyboard(self):
        with Listener(on_press=self.target_key) as listener:
            listener.join()

    def target_key(self, key):
        if key == keyboard.Key.esc:
            return False
        if key == keyboard.Key.delete:
            threading.Thread(target= self.run).start()

    def run(self):
        dp = DPactions()
        dp. depotTileFinder()
        dp.depositFinder()
        dp.marketFinder()

