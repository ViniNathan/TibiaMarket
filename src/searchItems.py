import json
import threading
from screen import *
from time import sleep
from mouseActions import Actions
from imageCompair import compare_images
from pynput.keyboard import Listener
from pynput import keyboard

class SearchBoughtItems:
    def __init__(self):
        self.WindowName = "Projetor em tela cheia (prévia)"
        self.actions = Actions()
        self.screen = WindowCapture(self.WindowName)
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

    def itemFinder(self):
        pyautogui.moveTo(1559, 644)
        itemPhoto = self.screen.capture_mouse_region2()
        save_path = "images/itemsPhoto/ItemPhoto.png"
        cv2.imwrite(save_path, itemPhoto)


    def catchItems(self):
        item_photo = "images/itemsPhoto/ItemPhoto.png"
        blank_template = "images/depotImages/blankTemplate.png"
        are_equal = compare_images(item_photo, blank_template)
        if are_equal:
            print("Itens indisponíveis") #ADICIONAR AÇÃO DE IR PRO PROXIMO ITEM
            self.nextItem()
        else:
            # Pega todos os itens para vender do respectivo npc
            self.actions.double_click(1581, 644)
            retrieveItemsPath = "images/depotImages/retrieveItems.png"
            retrieveItemsLocation = LocateImageCenter(retrieveItemsPath, self.WindowName)

            if retrieveItemsLocation is not None:
                print("O botão de pegar itens foi encontrado na posição:", retrieveItemsLocation)
                self.actions.move_and_left_click(retrieveItemsLocation)
            else:
                print("O botão de pegar itens não foi encontrado")

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
        self.findSearchButton() # DEVE SER EXECUTADA APENAS NA PRIMEIRA VEZ
        for i in range(len(self.Items)):
            item = self.Items[i]
            self.nome_item = item['nome']
            self.findSearchBar()
            self.doItemSearch()
            self.itemFinder()
            self.catchItems()
            self.count += 1


a = SearchBoughtItems()
a.start_keyboard()