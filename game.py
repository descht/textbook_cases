"""The main game, hopefully."""

from player import *
import time

player = Player()
#print player.currentroom.description
#print player.currentroom.description.lower()

now = time.strftime("%Y%m%d%H%M%S")

#with open("TextbookMysteriesUserTest{}.log".format(now), "w+") as f:
print player.currentroom.intro_desc
while player.is_alive and not player.victory:
    action = raw_input("> ")
    #f.writelines("> {}\n".format(action))
    action = clean_input(action)
    response = check_action(action, player)
    print response
    #f.writelines("{}\n".format(response))
