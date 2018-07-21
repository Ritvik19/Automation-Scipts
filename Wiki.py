import sys, wikipedia, pyperclip

if len(sys.argv) == 1:
    print(pyperclip.paste()+'\n\n')
    print(wikipedia.page(pyperclip.paste).title)
    print('\n')
    print(wikipedia.page(pyperclip.paste).content)

elif len(sys.argv) == 2:
    if sys.argv[1] == 'search' or sys.argv[1] == 'Search':
        print(pyperclip.paste()+'\n\n')
        print(wikipedia.search(pyperclip.paste))
    elif sys.argv[1] == 'summary' or sys.argv[1] == 'Summary':
        print(pyperclip.paste()+'\n\n')
        print(wikipedia.summary(pyperclip.paste))
    else:
        print(wikipedia.page(sys.argv[1]).title)
        print('\n')
        print(wikipedia.page(sys.argv[1]).content)

elif len(sys.argv) == 3:
    if sys.argv[1] == 'search' or sys.argv[1] == 'Search':
        print(sys.argv[2]+'\n\n')
        print(wikipedia.search(sys.argv[2]))
    elif sys.argv[1] == 'summary' or sys.argv[1] == 'Summary':
        print(sys.argv[2]+'\n\n')
        print(wikipedia.summary(sys.argv[2]))
