"""The definitions for all the rooms available."""
from items import *
from objects import *

#Generic classes for a room-----------------------------------
class room(object):
    def __init__(self, room_id, name, intro_desc, look_text, connects, connect_text, inventory, objects):
        self.room_id = room_id
        self.name = name
        self.intro_desc = intro_desc
        self.look_text = look_text
        self.connects = connects
        self.connect_text = connect_text
        self.inventory = inventory
        self.objects = objects
    def __str__(self):
        return "\n{}\n=====\n{}\nInventory: {}\nObjects: {}\nConnects to: {}\n".format(self.name, self.intro_desc, self.inventory, self.objects, self.connects)
    def modify_player(self, player):
        pass
    def look_desc(self):
        look_desc = "{}\n".format(self.look_text)
        if len(self.inventory) != 0:
            look_desc += "You can see the following items:\n"
            for item in self.inventory:
                look_desc += " -- {}\n".format(item.name.title())
                item.discovered = True
        if len(self.objects) != 0:
            for possible_object in self.objects:
                possible_object.discovered = True
        look_desc += "{}\n".format(self.connect_text)
        return look_desc



#Specific rooms -----------------------------------------------------------
class startroom(room):
    def __init__(self):
        super(startroom, self).__init__(room_id=1,
                                        name="start room",
                                        intro_desc="You are standing in a completely empty room. There's nothing of any use here.",
                                        look_text="On closer inspection, there's still nothing. You should move on.",
                                        connects=["key room", "paper room"],
                                        connect_text="From here you can see two doors, labelled 'Key Room' and 'Paper Room'.",
                                        inventory=[],
                                        objects=[])
   # def look_desc(self):
   #     look_desc = "On closer inspection, there's still nothing. You should move on.\n\nFrom here you can see two doors, labelled 'Key Room' and 'Paper Room'."
   #     return look_desc

class keyroom(room):
    def __init__(self):
        super(keyroom, self).__init__(room_id=2,
                                      name="key room",
                                      intro_desc="Another bland room.",
                                      look_text="The room is mostly bare, with a single chest of drawers in the centre of the room.",
                                      connects=["start room"],
                                      connect_text="From here you can see one door, labelled 'Start Room'.",
                                      inventory=[],
                                      objects=[])
    # def look_desc(self):
    #     look_desc = "The room is mostly bare"
    #     if len(self.items) != 0:
    #         look_desc += ", with a large key in the centre of the floor"
    #     look_desc += ".\n\nFrom here you can see one door, labelled 'Start Room'."
    #     return look_desc

class paperroom(room):
    def __init__(self):
        super(paperroom, self).__init__(room_id=3,
                                        name="paper room",
                                        intro_desc="Surprisingly the paper room contains paper.",
                                        look_text="The room is mostly bare.",
                                        connects=["start room", "end room", "death room"],
                                        connect_text="From here you can see three doors, labelled 'Start Room', 'End Room' and 'Death Room'.",
                                        inventory=[],
                                        objects=[])
    # def look_desc(self):
    #     look_desc = "The room is mostly bare"
    #     if len(self.inventory) != 0:
    #         look_desc += ", with a piece of paper on the floor"
    #     look_desc += ".\n\nFrom here you can see three doors, labelled 'Start Room', 'End Room' and 'Death Room'."
    #     return look_desc

class deathroom(room):
    def __init__(self):
        super(deathroom, self).__init__(room_id=5,
                                        name="death room",
                                        intro_desc="I don't really know what you expected.",
                                        look_text="You're totally dead.",
                                        connects=["paper room"],
                                        connect_text="",
                                        inventory=[],
                                        objects=[])
    # def look_desc(self):
    #     look_desc = "You're totally dead."
    #     return look_desc
    def modify_player(self, player):
        player.is_alive = False
        print "Better luck next time."

class endroom(room):
    def __init__(self):
        super(endroom, self).__init__(room_id=4,
                                      name="end room",
                                      intro_desc="This room contains a locked door.",
                                      look_text="Other than the large locked door, there's nothing else to see.",
                                      connects=["paper room"],
                                      connect_text="From here you can see one door, labelled 'Paper Room'.",
                                      inventory=[],
                                      objects=[])
    # def look_desc(self):
    #     look_desc = "Other than the large locked door, there's nothing else to see.\n\nFrom here you can see one door, labelled 'Paper Room'"
    #     return look_desc


rooms = {
    "start room" : startroom(),
    "key room" : keyroom(),
    "paper room" : paperroom(),
    "end room" : endroom(),
    "death room" : deathroom()
}

#print "Key" in rooms[2].items.name
