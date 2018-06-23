# import the various required modules
import os, pyperclip, shelve, sys

os.chdir("E:\\Coding\\Automation\\MCB_data")
shelfFile = shelve.open("clips")

if len(sys.argv) > 2:

    if sys.argv[1] == "save":
        shelfFile[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1] == "delt":
        if sys.argv[2] in list(shelfFile.keys()):
            del(shelfFile[sys.argv[2]])

elif len(sys.argv) == 2:
    if sys.argv[1] == "list":
        pyperclip.copy(", ".join(k for k in shelfFile.keys()))

    elif sys.argv[1] == "dall":
        for k in list(shelfFile.keys()):
            del(shelfFile[k])
    elif sys.argv[1] in shelfFile:
        pyperclip.copy(shelfFile[sys.argv[1]])

shelfFile.close()
