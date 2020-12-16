#experimental test branch (woring with some bugs atm)

import time
import pynput
from PIL import Image
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

keyboard = Controller()
mouse = MouseController()

print(mouse.position)

lword = input("Last word: ")
from PIL import ImageGrab, ImageDraw
image = ImageGrab.grab(bbox=(450, 74, 1425, 300))
image.save('sc.png') 

time.sleep(0.25)
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
text = pytesseract.image_to_string(Image.open("sc.png"))

lwordc = text.count(lword)
progress = 0
progressrev = 0

text = text.strip()
text = text.replace("\n", " ")
text = text.replace("|", "I")
text = text.replace("1", "I")
text = text.split(" ")
print(text)
for word in text:
    time.sleep(0.10)
    keyboard.type(word)
    index = text.index("change")
    if (word == lword and lwordc == 1):
        progress += 1
        progressrev = len(text[0:index]) - progress
        print("Progress: " + str("[" + "■" * progress + "□" * progressrev  + "]"))
        print("End of Sentence")
        break
    elif (word == lword):
        lwordc -= 1
        progress += 1
        progressrev = len(text[0:index]) - progress
        print("Progress: " + str("[" + "■" * progress + "□" * progressrev  + "]"))
        keyboard.type(" ")
    else:
        progress += 1
        progressrev = len(text[0:index]) - progress
        print("Progress: " + str("[" + "■" * progress + "□" * progressrev  + "]"))
        keyboard.type(" ")