import time
from src.screen import *
from src.mouseActions import Actions
from src.marketActions import *


class record:
    def __init__(self):
        self.count = 0
        self.coordinates = []
        self.npc = actionsMarket().npc
        

    def photo (self):
        window_name = "Projetor em tela cheia (prévia)"
        window = WindowCapture(window_name)
        screen = WindowCapture.capture_mouse_region3(window)
        save_path = "images/moveToNpc/{0}/flag_{1}.png".format(self.npc, self.count)
        cv2.imwrite(save_path, screen)
        self.count += 1
        infos = {
            "path": save_path,
            "wait": 0,
            "start": None
        }
        self.coordinates.append(infos)
        print(infos)

    def tick (self):
        last_coordinates = self.coordinates[-1]
        if last_coordinates["start"] == None:
            last_coordinates["start"] = time.time()
        else:
            last_coordinates["wait"] = time.time() - last_coordinates["start"]
            del last_coordinates["start"]


    def key_code(self, key):
        print(key)
        if key == keyboard.Key.esc:
            with open("scripts/moveToNpc/{0}.json".format(self.npc), "w") as file:
                file.write(json.dumps(self.coordinates))
            return False
        if key == keyboard.Key.insert:
            self.photo()
        if key == keyboard.Key.page_up:
            self.tick()
        

    def start (self):
        with Listener(on_press= self.key_code) as listener:
            listener.join()
