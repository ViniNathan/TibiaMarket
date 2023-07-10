import pyautogui

def main():
    while True:
        x, y = pyautogui.position()
        print(f"Posição do mouse: X = {x}, Y = {y}")

if __name__ == '__main__':
    main()
