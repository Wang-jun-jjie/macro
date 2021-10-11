import time
import random
import threading
from pynput import mouse, keyboard
import pydirectinput

def main():

    class Operator(threading.Thread):
        def __init__(self, button):
            super(Operator, self).__init__()
            self.button = button
            self.running = False
            self.program_running = True

        def start_clicking(self):
            self.running = True

        def stop_clicking(self):
            self.running = False

        def exit(self):
            self.stop_clicking()
            self.program_running = False

        def anti_captcha(self):
            # random clicking time
            d = 0.15+random.random()*0.1
            time.sleep(d)
            # random movement
            t = random.random()
            if t > 0.97:
                d = random.random()*2.5
                time.sleep(d)
                # pydirectinput.press('d')
                # pydirectinput.press('a')
                # pydirectinput.press('a')

        def run(self):
            while self.program_running:
                while self.running:
                    mouse_ctl.click(self.button)
                    self.anti_captcha()
                time.sleep(0.1)

    mouse_ctl = mouse.Controller()
    click_thread = Operator(mouse.Button.left)
    click_thread.start()
    trigger = keyboard.Key.right
    kill_switch = keyboard.Key.left
    

    def on_press(key):
        if key == trigger:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == kill_switch:
            # Stop listener
            print('Program will now halt.')
            click_thread.exit()
            return False
    
    with keyboard.Listener(on_press=on_press) as listener:
        print('Program starting...')
        listener.join()

if __name__ == "__main__":
    main()