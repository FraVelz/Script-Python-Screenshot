from pynput import keyboard
import pyautogui as r
import os

directory = os.path.abspath(os.getcwd()) + '\\Images\\'
name = 'Imagen'
sys = print
num = 1

def keylogger_(function_):
    keylogger_array = []

    def on_press(key): 
        if key == keyboard.Key.esc:
            return False
        
        try: k = key.char
        except: k = key.name

        keylogger_array.append(str(k))

        if k == '1': function_()
        if k == '0': return False
        
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    print(keylogger_array)

def screenShot(): 
    global name, num
    img = r.screenshot()

    img.save(
        r'{0}\\{1}{2}.png'.format(
            directory, name, num
        )
    )

    sys(f'\n [+] Capture saved as: {name}{num}.png...')
    num += 1

def main(): 
    sys('\n [+] Press 1 to take a screenshot...')
    keylogger_(screenShot)

if __name__ == '__main__':
    main()
    
#* Author: Francisco Velez
