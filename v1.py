# working release branch

import time
import pynput
from PIL import Image
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

keyboard = Controller()
mouse = MouseController()

print(mouse.position)

# from PIL import ImageGrab
# image = ImageGrab.grab(bbox=(450, 450, 1425, 540))
# image.save('sc.png')
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
text = pytesseract.image_to_string(Image.open("sc.png"))
text = text.strip()
text = text.replace("\n", " ")
text = text.replace("|", "I")
text = text.split(" ")
print(text)

for word in text:
    time.sleep(0.25)
    keyboard.type(word)
    if (word == text[len(text) - 1]):
        print("End of Sentence")
    else:
        keyboard.type(" ")