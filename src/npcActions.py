from src.screen import *
from src.marketActions import *
from time import sleep
from pynput.keyboard import Listener
from pynput import keyboard

class actionsNpc():
    def __init__(self):
        self.WindowName = "Projetor em tela cheia (prévia)"
        self.screen = WindowCapture(self.WindowName)

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

    def wordsToSay(self):
        # Digite o texto caractere por caractere
        for caractere in "hi":
            pyautogui.typewrite(caractere)
        # Pressione a tecla Enter para concluir a digitação
        pyautogui.press('enter')

        for caractere2 in "trade":
            pyautogui.typewrite(caractere2)       
        # Pressione a tecla Enter para concluir a digitação
        pyautogui.press('enter')

    def pressSell(self):
        # Busca o botão de sell
        sellButtonPath = "images/npcImages/sellButton.png"
        sellButtonLocation = LocateImageCenter(sellButtonPath, self.WindowName)
        if sellButtonLocation is not None:
            print("O botão de sell foi encontrado na posição:", sellButtonLocation)
            pyautogui.moveTo(sellButtonLocation)
            sleep(1)
            pyautogui.leftClick()

    def SearchFinder(self):
        SearchPath = "images/npcImages/searchBar.png"
        SearchLocation = LocateImageCenter(SearchPath, self.WindowName)
        if SearchLocation is not None:
            print("A barra de pesquisa foi encontrada na posição:", SearchLocation)
            pyautogui.moveTo(SearchLocation)
            pyautogui.leftClick()
    
    def SearchItems(self):
        # Digite o texto caractere por caractere
        for caractere in self.nome_item:
            pyautogui.typewrite(caractere)
        
        # Pressione a tecla Enter para concluir a digitação
        pyautogui.press('enter')
    
    def itemFinder(self):
        pyautogui.moveTo(1811, 726)
        pyautogui.leftClick()

    def doSell(self):
        sliderPath = "images/npcImages/itemSlider.png"
        acceptButonPath = "images/npcImages/acceptButton.png"
        for i in range (10):
            sliderLocation = LocateImageCenter(sliderPath, self.WindowName)
        if sliderLocation is not None:
            print("A barra de slide foi encontrada na posição:", sliderLocation)
            destino_x = sliderLocation[0] + 150
            destino_y = sliderLocation[1]
            destino = destino_x, destino_y
            mouse = Actions()
            mouse.drag_and_move(sliderLocation ,destino)
            if acceptButonPath is not None:
                acceptButtonLocation = LocateImageCenter(acceptButonPath, self.WindowName)
                print("O botão de confirmação foi encontrado na posição:", acceptButtonLocation)
                mouse.move_and_left_click(acceptButtonLocation)
        self.nextItem()


    def nextItem(self):
        closeSearchPath = "images/npcImages/cancelButton.png"
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
        sleep(2)
        self.wordsToSay() # EXECUTADAS APENAS NA PRIMEIRA
        self.pressSell()  # VEZ QUE O CÓDIGO É CHAMADOS
        for i in range(len(self.Items)):
            item = self.Items[i]
            self.nome_item = item['nome']
            self.SearchFinder()
            self.SearchItems()
            self.itemFinder()
            self.doSell()