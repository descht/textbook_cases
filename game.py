"""The main game, hopefully."""

from player import *
import time
import subprocess as sp
from colorama import Fore, Back, Style
from utils import *


room_text = load_descriptions_file('room_description.json')

player = Player()

now = time.strftime("%Y%m%d%H%M%S")

# with open("TextbookMysteriesUserTest{}.log".format(now), "w+") as f:
sp.call('clear', shell=True)

print(Fore.WHITE + room_text["intro_text"]["first_line"])
input(Fore.GREEN + "< Press ANY KEY to continue >")

print(Fore.WHITE + room_text["intro_text"]["second_line"])
input(Fore.GREEN + "< Press ANY KEY to continue >")

print(Fore.WHITE + "\n{}\n".format(player.currentroom.intro_desc))

while player.is_alive and not player.victory:
    action = input(Fore.GREEN + "> ")
    # f.writelines("> {}\n".format(action))
    action = clean_input(action)
    response = check_action(action, player)
    print(Fore.WHITE + "\n{}".format(response))
    # f.writelines("{}\n".format(response))
