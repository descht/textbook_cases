"""The definitions for all interactive objects found throughout the game."""

from items import *

#Generic classes for an object-----------------------------------

class world_object(object):
    def __init__(self, name, true_name, description, discovered, has_inv, inventory, state, use_item):
        self.name = name
        self.true_name = true_name
        self.description = description
        self.discovered = discovered
        self.has_inv = has_inv
        self.inventory = inventory
        self.state = state
        self.use_item = use_item
    def modify_object(self, player):
        return "That doesn't work like that."
    def open(self, player):
        return "That doesn't work like that."
    def close(self, player):
        return "That doesn't work like that."
    def look_desc(self, player):
        for item in self.inventory:
            item.discovered = True
        return self.description
    def __str__(self):
        return "{}\n=====\n{}\nDiscovered: {}\nInventory: {}\nState: {}\n".format(self.name, self.description, self.discovered, self.inventory, self.state)

#Specific objects   -----------------------------------

class body(world_object):
    def __init__(self):
        super(body, self).__init__(name=["body", "corpse", "victim"],
                                   true_name="body",
                                   description="The body of a caucasian male, looks to be about 30 years old. He's lying on his back, clutching what appears to be a stab wound on his stomach with his right hand, and stretching upwards towards the back door with his left hand. Other than being dead, he looks remarkably unremarkable.",
                                   discovered=False,
                                   has_inv=True,
                                   inventory=[stab_wound()],
                                   state=["DNA", "FP"],
                                   use_item=[fingerprint(), dna()])
    def modify_object(self, player, item_name):
        if self.discovered:
            if item_name in fingerprint().name:
                return self.fingerprint_object(player)
            elif item_name in dna().name:
                return self.dna_object(player)
            else:
                return "Doesn't look like that works..."
        else:
            return "Is there there one of those in the room? I should look around first and check."
    def fingerprint_object(self, player):
        if "FP" in self.state:
            for item in player.inventory:
                if item.true_name == "Fingerprint Kit" and item.state == "Incomplete":
                    return "I've got the ink required, but I can't find the card used to take the transfers. I wonder if I've got anything I can use instead..."
                elif item.true_name == "Fingerprint Kit" and item.state == "Complete":
                    self.state.remove("FP")
                    player.evidence.append(victim_fingerprints())
                    return "I smear the victim's fingers in ink, and press the fingers on at a time onto a notebook page."
        else:
            return "I've already fingerprinted the victim."
    def dna_object(self, player):
        if "DNA" in self.state:
            self.state.remove("DNA")
            player.evidence.append(victim_dna())
            return "I take out a swab from my kit, and rub it around the inside of the victim's mouth."
        else:
            return "I've already got DNA from the victim."

class counter(world_object):
    def __init__(self):
        super(counter, self).__init__(name=["counter", "worktop", "counters", "kitchen counter", "kitchen counters"],
                                      true_name="Kitchen Counter",
                                      )
