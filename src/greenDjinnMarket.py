import json
from screen import *
from textStractor import extrair_numero_imagem
from time import sleep
from mouseActions import Actions
import re

class greenDjinnMarket():
    def __init__(self):
        self.WindowName = "Projetor em tela cheia (prévia)"
        self.screen = WindowCapture(self.WindowName)
        self.itemPrice = 0
        self.count = 0
        with open("scripts/greenDjinn.json") as file:
            self.greenData = json.load(file)
            self.greenItens = self.greenData['itens']

    def marketSearchFinder(self):
        marketSearchPath = "images/searchMarket.png"
        marketSearchLocation = LocateImageCenter(marketSearchPath, self.WindowName)
        if marketSearchLocation is not None:
            print("A barra de pesquisa foi encontrada na posição:", marketSearchLocation)
            pyautogui.moveTo(marketSearchLocation)
            pyautogui.leftClick()

    def greenSearchMarket(self):
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
        save_path = "images/itemsPrice/greenDjinn/{0}_price.png".format(self.nome_item)
        cv2.imwrite(save_path, itemPricePhoto)

    def priceImageToText(self):
        price_path = "images/itemsPrice/greenDjinn/{0}_price.png".format(self.nome_item)
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
        sliderMarketPath = "images/sliderMarket.png"
        for i in range (10):
            sliderMarketLocation = LocateImageCenter(sliderMarketPath, self.WindowName)
        if sliderMarketLocation is not None:
            print("A barra de slide foi encontrada na posição:", sliderMarketLocation)
            destino_x = sliderMarketLocation[0] + 150
            destino_y = sliderMarketLocation[1]
            destino = destino_x, destino_y
            grab = Actions()
            grab.drag_and_move(sliderMarketLocation ,destino)
        self.nextItem()

    def nextItem(self):
        closeSearchPath = "images/closeSearch.png"
        closeSearchLocation = LocateImageCenter(closeSearchPath, self.WindowName)
        if closeSearchLocation is not None:
            print("O botão de resetar a pesquisa foi encontrado na posição:", closeSearchLocation)
            pyautogui.moveTo(closeSearchLocation)
            pyautogui.leftClick()

    def run(self):
        for i in range(len(self.greenItens)):
            item = self.greenItens[i]
            self.nome_item = item['nome']
            self.valor_item = item['valor']
            self.marketSearchFinder()
            self.greenSearchMarket()
            self.itemFinder()
            self.priceFinder()
            self.priceImageToText()
            self.priceCompare()
            self.count += 1

sleep(3)
g = greenDjinnMarket()
g.run()


