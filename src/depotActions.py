from src.screen import *
from time import sleep



class DPactions():
    def __init__(self):
        self.WindowName = "Projetor em tela cheia (prévia)"

    def depotTileFinder(self):
        # Compor o caminho do template para o nome atual
        depotTilePath = "images/depotImages/depotTile.png"
        window_capture = WindowCapture(self.WindowName)
        template_matcher = TemplateMatcher(depotTilePath)
        screenshot = window_capture.capture()
        template_location = template_matcher.find_template(screenshot)

        if template_location is not None:
            print("O DP vazio foi encontrado na posição:", template_location)
            pyautogui.moveTo(template_location)
            pyautogui.leftClick()

    def depositFinder(self):
        # Busca o depot direito ou esquerdo do DP
        leftPlayerDepotPath = "images/depotImages/leftPlayerDepot.png"
        leftDepotLocation = LocateImageCenter(leftPlayerDepotPath, self.WindowName)

        if leftDepotLocation is not None:
            print("O DP da esquerda foi encontrado na posição:", leftDepotLocation)
            pyautogui.moveTo(leftDepotLocation)
            sleep(0.5)
            pyautogui.rightClick()
        else:
            rightPlayerDepotPath = "images/depotImages/rightPlayerDepot.png"
            rightDepotLocation = LocateImageCenter(rightPlayerDepotPath, self.WindowName)
            if rightDepotLocation is not None:
                print("O DP da direita foi encontrado na posição:", rightDepotLocation)
                pyautogui.moveTo(rightDepotLocation)
                sleep(0.5)
                pyautogui.rightClick()
                
    def marketFinder(self):
        marketPath = "images/depotImages/market.png"
        marketLocation = LocateImageCenter(marketPath, self.WindowName)
        if marketLocation is not None:
            print("O market foi encontrado na posição:", marketLocation)
            pyautogui.moveTo(marketLocation)
            sleep(0.5)
            pyautogui.rightClick()           
        
# sleep(4)
# depotTileFinder()
# sleep(1)
# depositFinder()
# sleep(1)
# marketFinder()
# sleep(1)
# marketSearchFinder()