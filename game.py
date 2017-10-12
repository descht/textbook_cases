"""The main game, hopefully."""

from player import *
import time
import subprocess as sp

player = Player()
#print player.currentroom.description
#print player.currentroom.description.lower()

now = time.strftime("%Y%m%d%H%M%S")

#with open("TextbookMysteriesUserTest{}.log".format(now), "w+") as f:
sp.call('clear', shell=True)
print "I got the call an hour ago. Roger Truman woke up around 4:15 this morning and went downstairs to the kitchen to get a glass of water. Instead he found a body. He apparently has no clue who the victim is, how they came to be in his home - never mind how they ended up dead.\n\nI pull into the quiet street in the pouring rain. Roger's home is a little terraced house in a street full of identical copies. In these conditions I can't make out any of the buildings in detail, but my headlights pick out house numbers displayed in rough white paint on bins lining the street.\n\nI park the car, and check over my kit - I've got my fingerprinting and DNA kits, a notepad and pen, my mobile phone and a pack of cigarettes. Satisfied, I get out my car, hurry up the short narrow path to the front door, and ring the bell.\n"
raw_input("< Press ANY KEY to continue >")
print "\nI'm first on scene. Roger answers the door with an oddly blank expression, and shows me straight through to the kitchen. A few quick glances around the living room get me a family photo - Roger himself, along with a young boy. I try to stop and ask, but he hurries me along. Looks like he's anxious to get this over with.\n"
raw_input("< Press ANY KEY to continue >")
print "\n{}\n".format(player.currentroom.intro_desc)
while player.is_alive and not player.victory:
    action = raw_input("> ")
    #f.writelines("> {}\n".format(action))
    action = clean_input(action)
    response = check_action(action, player)
    print "\n{}".format(response)
    #f.writelines("{}\n".format(response))
