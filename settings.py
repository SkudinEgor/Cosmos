import menu
import read
close = 2
WIDTH = int(menu.value["width"])
HEIGHT = int(menu.value["height"])
USERNAME = (menu.value["fieldname"])
WELCOME = read.myread(USERNAME)
if WELCOME == False:
    read.myadd(USERNAME)
COLOR = (menu.value["fieldcolor"])
if menu.event == "Exit":
    close = 3