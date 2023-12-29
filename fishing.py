import mouse
import keyboard
import time
import pyautogui
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#auto-fishing
def auto_fish():
    casted = False
    toggle = False
    log = ["", "", ""]
    i = 0
    while keyboard.is_pressed('x') == False:

        if keyboard.is_pressed('z'):
            toggle = not toggle
            if toggle:
                print("toggle: ON")
            else:
                print("toggle: OFF")
            time.sleep(1)
        while toggle:
            if keyboard.is_pressed('z'):
                toggle = not toggle
                if toggle:
                    print("toggle: ON")
                else:
                    print("toggle: OFF")
            time.sleep(.35)
            img = pyautogui.screenshot(region=(1318, 565, 601, 514))
            string = pytesseract.image_to_string(img)
            #print(string)
            log[i] = string
            if i == 2:
                i = 0
            else: 
                i += 1
            if casted and "Splashing" not in log[0] and "Splashing" not in log[1] and "Splashing" not in log[2]:
                casted = False

            #print("============================")
            if not casted:
                if "Splashing" not in string or not string or string == "":
                    #print("casted=======================================================")
                    casted = True
                    mouse.click('right')
                    time.sleep(1)
            if casted:
                if "Fishing Bobber splashes" in string or "splashes" in string or "Fithing Bobber splashes" in string or "Fizhing Bobber splashes" in string:
                    #print("reeled=======================================================")
                    casted = False
                    time.sleep(.2)
                    mouse.click('right')
                    time.sleep(1)
            
#run minecraft and join realm
def open_mc():
    mouse.move(0, 1079, absolute=True, duration=0.2)

    mouse.click('left')
    time.sleep(1)
    keyboard.write("minecraft")
    keyboard.send("enter")

    time.sleep(10)
    #security
    mouse.move(1069, 616, absolute=True, duration=0.2)

    mouse.click('left')
    #run mc
    mouse.move(1054, 746, absolute=True, duration=0.2)

    mouse.click('left')

    time.sleep(30)
    #realms
    mouse.move(944, 695, absolute=True, duration=0.2)
    time.sleep(1)
    mouse.click('left')
    #pick server
    mouse.move(961, 253, absolute=True, duration=0.2)
    time.sleep(1)
    mouse.click('left')
    #join server
    mouse.move(546, 900, absolute=True, duration=0.2)

    mouse.click('left')
    time.sleep(5)




#open_mc()
auto_fish()


