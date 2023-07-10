import json
import re
import threading
from src.screen import *
from src.textStractor import extrair_numero_imagem
from src.mouseActions import Actions
from time import sleep
from pynput.keyboard import Listener
from pynput import keyboard

class actionsMarket():
    def __init__(self):
        self.WindowName = "Projetor em tela cheia (prévia)"
        self.screen = WindowCapture(self.WindowName)
        self.itemPrice = 0
        self.npc = ""
        self.count = 0

        # Solicitar ao usuário que escolha o NPC
        escolha_npc = input("Escolha o NPC (greenDjinn, blueDjinn ou rashid): ")

        # Verificar a escolha do usuário e atribuir à variável self.npc
        if escolha_npc == "greenDjinn" or escolha_npc == "blueDjinn" or escolha_npc == "rashid":
            self.npc = escolha_npc
        else:
            print("NPC inválido!")

        with open(f"scripts/{self.npc}.json") as file:
            self.Data = json.load(file)
            self.Items = self.Data['itens']

    def marketSearchFinder(self):
        marketSearchPath = "images/depotImages/searchMarket.png"
        marketSearchLocation = LocateImageCenter(marketSearchPath, self.WindowName)
        if marketSearchLocation is not None:
            print("A barra de pesquisa foi encontrada na posição:", marketSearchLocation)
            pyautogui.moveTo(marketSearchLocation)
            pyautogui.leftClick()

    def SearchMarket(self):
        # Digite o texto caractere por caractere
        for caractere in self.nome_item:
            pyautogui.typewrite(caractere)
        
        # Pressione a tecla Enter para concluir a digitação
        pyautogui.press('enter')

    def itemFinder(self):
        pyautogui.moveTo(535, 477)
        pyautogui.leftClick()

    def priceFinder(self):
        pyautogui.moveTo(1045, 310)
        itemPricePhoto = self.screen.capture_mouse_region()
        save_path = "images/itemsPrice/{0}/{1}_price.png".format(self.npc, self.nome_item)
        cv2.imwrite(save_path, itemPricePhoto)

    def priceImageToText(self):
        price_path = "images/itemsPrice/{0}/{1}_price.png".format(self.npc, self.nome_item)
        textPrice = extrair_numero_imagem(price_path)
        clean_price = re.sub(r'\D', '', textPrice)

        try:
            self.itemPrice = int(clean_price)
        except ValueError:
            self.itemPrice = None

        return clean_price

    def priceCompare(self):
        sleep(1)
        if self.itemPrice is not None:
            extracted_price = int(self.itemPrice)
            if extracted_price < int(self.valor_item):
                print(f"O valor extraído {extracted_price}, do item {self.nome_item} é menor do que o valor do item {self.valor_item}")
                self.doBuy()
            elif extracted_price >= int(self.valor_item):
                print(f"O valor extraído {extracted_price}, do item {self.nome_item} é maior ou igual ao valor do item {self.valor_item}")
                self.nextItem()
        else:
            self.nextItem()

    def doBuy(self):
        sliderMarketPath = "images/depotImages/sliderMarket.png"
        acceptButonPath = "images/depotImages/acceptButton.png"
        for i in range (10):
            sliderMarketLocation = LocateImageCenter(sliderMarketPath, self.WindowName)
        if sliderMarketLocation is not None:
            print("A barra de slide foi encontrada na posição:", sliderMarketLocation)
            destino_x = sliderMarketLocation[0] + 150
            destino_y = sliderMarketLocation[1]
            destino = destino_x, destino_y
            mouse = Actions()
            mouse.drag_and_move(sliderMarketLocation ,destino)
            if acceptButonPath is not None:
                acceptButtonLocation = LocateImageCenter(acceptButonPath, self.WindowName)
                print("O botão de compra foi encontrado na posição:", acceptButtonLocation)
                mouse.move_and_left_click(acceptButtonLocation)
        self.nextItem()

    def nextItem(self):
        closeSearchPath = "images/depotImages/closeSearch.png"
        closeSearchLocation = LocateImageCenter(closeSearchPath, self.WindowName)
        if closeSearchLocation is not None:
            print("O botão de resetar a pesquisa foi encontrado na posição:", closeSearchLocation)
            pyautogui.moveTo(closeSearchLocation)
            pyautogui.leftClick()

    def start_keyboard(self):
        with Listener(on_press=self.target_key) as listener:
            listener.join()

    def target_key(self, key):
        if key == keyboard.Key.esc:
            return False
        if key == keyboard.Key.delete:
            threading.Thread(target= self.run).start()

    def run(self):
        sleep(3)
        for i in range(len(self.Items)):
            item = self.Items[i]
            self.nome_item = item['nome']
            self.valor_item = item['valor']
            self.marketSearchFinder()
            self.SearchMarket()
            self.itemFinder()
            self.priceFinder()
            self.priceImageToText()
            self.priceCompare()
            self.count += 1

# m = actionsMarket()
# m.start_keyboard()


