import pyperclip, sys


if len(sys.argv) > 1 and "~" in sys.argv:
    original = pyperclip.paste()
    i = sys.argv.index("~")

    r1 = " ".join(e for e in sys.argv[1:i])
    r2 = " ".join(e for e in sys.argv[i+1:])

    replaced = original.replace(r1, r2)
    pyperclip.copy(replaced)

    print("All occurences of ", r1, " in the copied text replaced with ", r2)
    print("The text after replacement copied to the clip board")
