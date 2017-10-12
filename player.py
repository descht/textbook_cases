"""The definition for the player"""
from rooms import *
import os

replace_dict = [
    [" at ", " "],
    [" to ", " "],
    [" the ", " "],
    ["with", "on"],
    ["pick up", "get"],
    ["grab", "get"],
    ["collect", "get"],
    ["check", "look"],
    ["search", "look"],
    ["examine", "look"]
]

class Player(object):
    def __init__(self):
        self.inventory = [pen(), phone(), fingerprint(), dna(), notebook(), cigarettes(5), lighter()]
        self.evidence = []
        self.is_alive = True
        self.victory = False
        self.stage = 0
        self.currentroom = kitchen()
    def print_inventory(self):
        if len(self.inventory) == 0:
            return "I'm not carrying anything."
        else:
            inv_list = "With me I've got:\n"
            for item in self.inventory:
                inv_list += "-- {}\n".format(item.true_name)
            return inv_list
    def print_evidence(self):
        if len(self.evidence) == 0:
            return "I've not discovered any evidence yet."
        else:
            inv_list = "The evidence I've collected so far:\n"
            for item in self.evidence:
                inv_list += "-- {}\n".format(item.true_name)
            return inv_list

def clean_input(action):
    action = action.lower()
    for word_pair in replace_dict:
        action = action.replace(word_pair[0], word_pair[1])
    return action

def move_action(dest, player):
    if len(dest) == 0:
        return "Where do you want to go?"
    elif "{} {}".format(dest[0], dest[1]) in player.currentroom.connects:
        player.currentroom = rooms["{} {}".format(dest[0], dest[1])]
        print "\n--------------------------------------\n"
        player.currentroom.modify_player(player)
        return "{}\n\n".format(player.currentroom.intro_desc)
    else:
        return "Doesn't look like you can get there from here."

def get_action(get_list, player):
    if len(get_list) == 0:
        return "What do you want to pick up?"
    else:
        get_item = ""
        for word in get_list:
            get_item += "{} ".format(word)
        get_item = get_item.strip()
        for possible_item in player.currentroom.inventory:
            if possible_item.name == get_item and possible_item.discovered:
                player.inventory.append(possible_item)
                player.currentroom.inventory.remove(possible_item)
                return "You picked up the {}".format(get_item)
        for possible_object in player.currentroom.objects:
            for possible_object_item in possible_object.inventory:
                if get_item == possible_object_item.name and possible_object_item.obtainable:
                    player.inventory.append(possible_object_item)
                    possible_object.inventory.remove(possible_object_item)
                    return "You picked up the {}".format(get_item)

        return "Looks like that item isn't here"

def look_action(look_item, player):
    if len(look_item) == 0 or (len(look_item) == 1 and look_item[0] == "room"):
        return player.currentroom.look_desc()
    elif look_item[0] == "inventory":
        return player.print_inventory()
    elif look_item[0] == "evidence":
        return player.print_evidence()
    else:
        look_item_full = ""
        for item in look_item:
            look_item_full += "{} ".format(item)
        look_item_full = look_item_full.strip()

        if look_item_full in player.currentroom.name:
            return player.currentroom.look_desc()
        for possible_item in player.currentroom.inventory:
            if look_item_full in possible_item.name and possible_item.discovered:
                return possible_item.look_desc(player)
        for possible_object in player.currentroom.objects:
            if look_item_full in possible_object.name and possible_object.discovered:
                return possible_object.look_desc(player)
            for possible_item in possible_object.inventory:
                if look_item_full in possible_item.name and possible_item.discovered:
                    return possible_item.look_desc(player)
        for possible_item in player.inventory:
            if look_item_full in possible_item.name:
                return possible_item.look_desc(player)
        for possible_evidence in player.evidence:
            if look_item_full in possible_evidence.name:
                return possible_evidence.look_desc(player)
        return "There's nothing to see."

def use_action(use_list, player):
    try:
        split_index = use_list.index("on")
    except:
        return "What do you want to use that on?"
    use_item = ""
    use_object = ""
    for i in range(len(use_list)):
        if i < split_index:
            use_item += "{} ".format(use_list[i])
        elif i > split_index:
            use_object += "{} ".format(use_list[i])
    use_item = use_item.strip()
    use_object = use_object.strip()

    for possible_item in player.inventory:
        if use_item in possible_item.name:
            for possible_object in player.currentroom.objects:
                if use_object in possible_object.name:
                    return possible_object.modify_object(player, use_item)
            for possible_item2 in player.inventory:
                if use_object in possible_item2.name:
                    return possible_item2.modify_object(player, use_item)
    return "That doesn't do anything."

def open_action(open_list, player):
    if len(open_list) == 0:
        return "What do you want to try and open?"
    else:
        open_item = ""
        for item in open_list:
            open_item += "{} ".format(item)
        open_item = open_item.strip()
        for possible_object in player.currentroom.objects:
            if open_item in possible_object.name:
                return possible_object.open(player)
        return "Doesn't look like theres one of those around."

def close_action(close_list, player):
    if len(close_list) == 0:
        return "What do you want to try and close?"
    else:
        close_item = ""
        for item in close_list:
            close_item += "{} ".format(item)
        close_item = close_item.strip()
        for possible_object in player.currentroom.objects:
            if close_item in possible_object.name:
                return possible_object.close(player)
        return "Doesn't look like theres one of those around."

def check_action(action, player):
    action = action.split()
    if len(action) == 0:
        return "Please type a command."
    else:
        verb = action.pop(0)
        if verb == "die":
            player.is_alive = False
            return "You died"
        elif verb == "win":
            player.victory = True
            return "You won"
        elif verb == "go":
            return move_action(action, player)
        elif verb == "get":
            return get_action(action, player)
        elif verb == "look":
            return look_action(action, player)
        elif verb == "use":
            return use_action(action, player)
        elif verb == "open":
            return open_action(action, player)
        elif verb == "close":
            return close_action(action, player)
        else:
            return "Sorry, I don't know what you meant by that."
