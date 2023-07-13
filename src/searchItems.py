import json
import threading
from src.depotActions import *
from src.screen import *
from src.imageCompair import compare_images
from src.mouseActions import *
from time import sleep
from pynput.keyboard import Listener
from pynput import keyboard

class SearchBoughtItems:
    def __init__(self, npc):
        self.WindowName = "Projetor em tela cheia (prévia)"
        self.actions = Actions()
        self.screen = WindowCapture(self.WindowName)
        self.npc = npc
        self.dpactions = DPactions()

        with open(f"scripts/{self.npc}.json") as file:
            self.Data = json.load(file)
            self.Items = self.Data['itens']

    def searchDepot(self):
        # Encontra o botão de abrir o depot
        searchDepotPath = "images/depotImages/depot.png"
        searchDepotLocation = LocateImageCenter(searchDepotPath, self.WindowName)

        if searchDepotLocation is not None:
            print("O Depot foi encontrado na posição:", searchDepotLocation)
            pyautogui.moveTo(searchDepotLocation)
            sleep(0.5)
            pyautogui.rightClick()
            # Definir o número de segundos para realizar a rolagem contínua
            tempo_rolagem = 1

            # Definir a velocidade de rolagem (pode ajustar conforme necessário)
            velocidade_rolagem = 0.1
            # Calcular o número de vezes com base no tempo e velocidade
            num_rolagens = int(tempo_rolagem / velocidade_rolagem)
            # Rolar o mouse para baixo (-1) repetidamente até o tempo definido
            for _ in range(num_rolagens):
                pyautogui.scroll(-10)
                sleep(velocidade_rolagem)
        else:
            print("Depot não encontrado")

    def searchLastDeposit(self):
        # Encontra o utlimo depot
        searchLastDepotPath = "images/depotImages/lastDeposit.png"
        searchLastDepotLocation = LocateImageCenter(searchLastDepotPath, self.WindowName)
        if searchLastDepotLocation is not None:
            print("O ultimo depot foi encontrado na posição:", searchLastDepotLocation)
            pyautogui.moveTo(searchLastDepotLocation)
            sleep(0.5)
            pyautogui.rightClick()
        else:
            print("Ultimo depot não encontrado")

    def reopenDP(self):
        self.dpactions.depositFinder()

    def searchMail(self):
        self.reopenDP()
        # Encontra o mail
        searchMailPath = "images/depotImages/mail.png"
        searchMailLocation = LocateImageCenter(searchMailPath, self.WindowName)
        if searchMailLocation is not None:
            print("O Mail foi encontrado na posição:", searchMailLocation)
            pyautogui.moveTo(searchMailLocation)
            sleep(0.5)
            pyautogui.rightClick()
            self.itemBoxFinder()
        else:
            print("Mail não encontrado")

    def itemBoxFinder(self):
        origem = pyautogui.moveTo(1738, 705)
        itemPhoto = self.screen.capture_mouse_region4()
        save_path = "images/depotImages/boxItem.png"
        cv2.imwrite(save_path, itemPhoto)
        equal = compare_images(save_path, "images/depotImages/emptyBox.png")
        while compare_images(save_path, "images/depotImages/emptyBox.png") is not True:
            destino = (1738, 605)
            self.actions.drag_and_move2(origem, destino)
            self.itemBoxFinder()
        if equal:
            print("Não existem itens no Mail")


    def findSearchButton(self):
        # Encontra o botão de busca no depot
        searchButtonPath = "images/depotImages/searchButton.png"
        searchButtonLocation = LocateImageCenter(searchButtonPath, self.WindowName)

        if searchButtonLocation is not None:
            print("O botão de busca foi encontrado na posição:", searchButtonLocation)
            self.actions.move_and_left_click(searchButtonLocation)
        else:
            print("Botão de busca não encontrado")

    def findSearchBar(self):
        # Encontra a barra de busca no depot
        searchBarPath = "images/depotImages/searchBar.png"
        searchBarLocation = LocateImageCenter(searchBarPath, self.WindowName)

        if searchBarLocation is not None:
            print("A barra de busca foi encontrado na posição:", searchBarLocation)
            self.actions.move_and_left_click(searchBarLocation)
        else:
            print("Botão de busca não encontrado")

    def doItemSearch(self):
        # Digita o texto caractere por caractere
        for caractere in self.nome_item:
            pyautogui.typewrite(caractere)
        
        # Pressione a tecla Enter para concluir a digitação
        pyautogui.press('enter')
        self.itemFinder()
        

    def itemFinder(self):
        pyautogui.moveTo(1559, 644)
        itemPhoto = self.screen.capture_mouse_region2()
        save_path = "images/itemsPhoto/ItemPhoto.png"
        cv2.imwrite(save_path, itemPhoto)
        self.catchItems()


    def catchItems(self):
        item_photo = "images/itemsPhoto/ItemPhoto.png"
        blank_template = "images/depotImages/blankTemplate.png"
        are_equal = compare_images(item_photo, blank_template)
        if are_equal:
            print("Itens indisponíveis")
            self.nextItem()
        else:
            # Pega todos os itens para vender do respectivo npc
            location = (1581, 644)
            self.actions.double_click(location)
            retrieveItemsPath = "images/depotImages/retrieveItems.png"
            retrieveItemsLocation = LocateImageCenter(retrieveItemsPath, self.WindowName)

            if retrieveItemsLocation is not None:
                print("O botão de pegar itens foi encontrado na posição:", retrieveItemsLocation)
                pyautogui.moveTo(retrieveItemsLocation)
                sleep(0.5)
                pyautogui.leftClick()
                self.findSearchButton()
                self.nextItem()
            else:
                print("O botão de pegar itens não foi encontrado")
                self.findSearchButton()

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
        self.searchDepot()
        self.searchLastDeposit()
        self.searchMail()
        self.findSearchButton()
        for i in range(len(self.Items)):
            item = self.Items[i]
            self.nome_item = item['nome']
            self.findSearchBar()
            self.doItemSearch()
        return False
