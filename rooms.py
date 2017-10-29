"""The definitions for all the rooms available."""
from items import *
from objects import *

#Generic classes for a room-----------------------------------
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



#Specific rooms -----------------------------------------------------------
class kitchen(room):
    def __init__(self):
        super(kitchen, self).__init__(
                                        room_id=1,
                                        name=["kitchen"],
                                        true_name="Kitchen",
                                        intro_desc="Roger's kitchen is reasonably sized - there's a handful of furniture and various kitchen appliances, and still enough floor space left over for two or three people to move around without getting in each others way. At least, not too much.",
                                        look_text="There are two kitchen counters running along the North and West walls, and a small table and chairs in the South-East corner. Next to the table are a couple of bins, and a door in the East wall which leads outside. Finally, there's a body lying on the floor. I'm going to make an educated guess and say that the last isn't an intentional design feature.",
                                        connects=[],
                                        connect_text="There's one doorway back into the living room, which Roger is currently standing in.",
                                        inventory=[],
                                        objects=[body(), counter(), bins()]
                                    )

class outside(room):
    def __init__(self):
        super(outside, self).__init__(
            room_id=2,
            name=["outside", "front of house"],
            true_name="Outside Roger's House",
            intro_desc="",
            look_text="",
            connects=[],
            connect_text="",
            inventory=[],
            objects=[]
        )
    def modify_player(self, player):
        kitchen().connects=[]
        return "I push past Roger, straight through his living room, out the front door and to the kerb. If the murder weapon was thrown in the bin, and the bin bags are missing, then the next place I need to check is the black wheelie bin on the street.\n\nOnce outside, the sound of bin men clattering about in the distance becomes clear - luckily they have't got this far up the street yet. I flip open the black bin lid, and lift out the top bag."



rooms = {
    "kitchen" : kitchen(),
    "outside" : outside()
}

#print "Key" in rooms[2].items.name
