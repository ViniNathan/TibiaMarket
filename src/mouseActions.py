import pyautogui
from time import sleep

class Actions:
    def __init__(self):
        pass

    def move_and_left_click(self, image_location):
        pyautogui.moveTo(image_location)
        pyautogui.leftClick()

    def move_and_right_click(self, image_location):
        pyautogui.moveTo(image_location)
        pyautogui.leftClick()

    def move_and_right_click_delay(self, image_location):
        pyautogui.moveTo(image_location)
        sleep(1)
        pyautogui.leftClick()

    def double_click(self, image_location):
        pyautogui.moveTo(image_location)
        pyautogui.doubleClick()

    def drag_and_move(self, origem, destino):
        # Obtém as coordenadas iniciais do cursor
        pyautogui.moveTo(origem)
        
        # Pressiona o botão esquerdo do mouse
        pyautogui.mouseDown(button='left')

        # Move o cursor para uma nova posição
        new_x, new_y = destino
        pyautogui.moveTo(new_x, new_y, duration=1.0)  # Duração opcional para mover suavemente

        # Solta o botão esquerdo do mouse
        pyautogui.mouseUp(button='left')
    