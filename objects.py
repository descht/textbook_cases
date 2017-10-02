"""The definitions for all interactive objects found throughout the game."""

from items import *

#Generic classes for an object-----------------------------------

class world_object(object):
    def __init__(self, name, description, discovered, has_inv, inventory, state, use_item):
        self.name = name
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
    def __str__(self):
        return "{}\n=====\n{}\nDiscovered: {}\nInventory: {}\nState: {}\n".format(self.name, self.description, self.discovered, self.inventory, self.state)

#Specific objects   -----------------------------------

class enddoor(world_object):
    def __init__(self):
        super(enddoor, self).__init__(name=["locked door", "door"],
                                      description="A large wooden door, with a giant padlock on it.",
                                      discovered=False,
                                      has_inv=False,
                                      inventory=[],
                                      state="locked",
                                      use_item=[])
    def modify_object(self, player, item_name):
        if self.discovered:
            for possible_item in self.use_item:
                if item_name == possible_item.name:
                    if self.state == "locked":
                        self.state = "unlocked"
                        self.name.remove("locked door")
                        self.name.append("unlocked door")
                        return "You hear a click as the door unlocks."
                    elif self.state == "unlocked":
                        self.state = "locked"
                        self.name.remove("unlocked door")
                        self.name.append("locked door")
                        return "You hear a click as the door locks."
            return "Doesn't look like that works..."
        else:
            return "Is there there one of those in the room? You should look around more and check."
    def open(self, player):
        if self.discovered:
            if self.state == "locked":
                return "You turn the handle and try pushing, pulling, shaking and shoving. Yep, definitely locked."
            elif self.state == "unlocked":
                player.victory = True
                return "You open the door, and step through into the light..."
        else:
            return "Is there there one of those in the room? You should look around more and check."

class drawers(world_object):
    def __init__(self):
        super(drawers, self).__init__(name=["drawers", "drawer", "chest of drawers"],
                                      description="It's a small chest of drawers. Looks like there's only one drawer left - all the others have been removed.",
                                      discovered=False,
                                      has_inv=True,
                                      inventory=[key()],
                                      state="closed",
                                      use_item=[])
    def open(self, player):
        if self.discovered:
            if self.state == "closed":
                item_list = ""
                self.state = "open"
                for item in self.inventory:
                    item.discovered = True
                    item.obtainable = True
                    item_list += "\n -- {}".format(item.name.title())
                if len(self.inventory) == 0:
                    drawer_desc = " There's nothing inside."
                else:
                    drawer_desc = " Inside, you can see the following items:{}".format(item_list)
                self.description = "It's a small chest of drawers, with it's only drawer hanging open.{}".format(drawer_desc)
                return "You open the drawer.{}".format(drawer_desc)
            else:
                return "The drawer is already open."
        else:
            return "Is there there one of those in the room? You should look around more and check."
    def close(self, player):
        if self.discovered:
            if self.state == "open":
                self.state = "closed"
                for item in self.inventory:
                    item.obtainable = False
                self.description = "It's a small chest of drawers. Looks like there's only one drawer left - all the others have been removed."
                return "You close the drawer."
            else:
                return "The drawer is already closed."
        else:
            return "Is there there one of those in the room? You should look around more and check."
