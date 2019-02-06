"""The definitions for all the rooms available."""
from objects import *
from utils import *

contents = load_descriptions_file("room_description.json")


# Generic classes for a room-----------------------------------
class room(object):
    def __init__(self, room_id, name, true_name, intro_desc, look_text, connects, connect_text, inventory, objects):
        self.room_id = room_id
        self.name = name
        self.true_name = true_name
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
            # look_desc += "You can see the following items:\n"
            for item in self.inventory:
                # look_desc += "-- {}\n".format(item.name.title())
                item.discovered = True
        if len(self.objects) != 0:
            for possible_object in self.objects:
                possible_object.discovered = True
        look_desc += "{}\n".format(self.connect_text)
        return look_desc


# Specific rooms -----------------------------------------------------------
class kitchen(room):
    def __init__(self):
        super(kitchen, self).__init__(
            room_id=1,
            name=["kitchen"],
            true_name="Kitchen",
            intro_desc=load_room_text(contents, "kitchen", "intro_text"),
            look_text=load_room_text(contents, "kitchen", "look_text"),
            connects=[],
            connect_text=load_room_text(contents, "kitchen", "connect_text"),
            inventory=[],
            objects=[body(), counter(), bins()]
        )


class Outside(room):
    def __init__(self):
        super(Outside, self).__init__(
            room_id=2,
            name=["outside", "front of house"],
            true_name="Outside Roger's House",
            intro_desc=load_room_text(contents, "outside", "intro_text"),
            look_text=load_room_text(contents, "outside", "look_text"),
            connects=[kitchen()],
            connect_text=load_room_text(contents, "outside", "connect_text"),
            inventory=[],
            objects=[]
        )

    def modify_player(self, player):
        # kitchen().connects=[]
        print("I push past Roger, straight through his living room, out the front door and to the kerb. If the murder weapon was thrown in the bin, and the bin bags are missing, then the next place I need to check is the black wheelie bin on the street.\n\nOnce outside, the sound of bin men clattering about in the distance becomes clear - luckily they have't got this far up the street yet. I flip open the black bin lid, and lift out the top bag.")
        return 0


rooms = {
    "kitchen": kitchen(),
    "outside": Outside()
}

# print "Key" in rooms[2].items.name
