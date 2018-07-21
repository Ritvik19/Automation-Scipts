import pyperclip
import pyttsx3
import sys

engine = pyttsx3.init()
if len(sys.argv) == 1:
    text = pyperclip.paste()
else:
    text = ' '.join(sys.argv[1:])
print(text)
engine.say(text)
engine.runAndWait()
