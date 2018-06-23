import sys, webbrowser
if len(sys.argv) > 1:
     search = " ".join(e for e in sys.argv[1:])
     webbrowser.open("https://syntaxdb.com/reference/search?utf8=✓&search="+search)
