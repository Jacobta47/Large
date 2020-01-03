#*****************************************************************
#JACOB T. ARMENTROUT *********************************************
#*****************************************************************

import webbrowser

url = "Large.txt"

chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

webbrowser.get(chrome).open(url)