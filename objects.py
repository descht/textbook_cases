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
        return "{}\n".format(self.description)
    def __str__(self):
        return "{}\n=====\n{}\nDiscovered: {}\nInventory: {}\nState: {}\n".format(self.name, self.description, self.discovered, self.inventory, self.state)

#Specific objects   -----------------------------------

class body(world_object):
    def __init__(self):
        super(body, self).__init__(
                                    name=["body", "corpse", "victim"],
                                    true_name="body",
                                    description="The body of a caucasian male, looks to be about 30 years old. He's lying on his back, clutching what appears to be a stab wound on his stomach with his right hand, and stretching upwards towards the back door with his left hand. Other than being dead, he looks remarkably unremarkable.",
                                    discovered=False,
                                    has_inv=True,
                                    inventory=[wound()],
                                    state=["DNA", "FP"],
                                    use_item=[fingerprint(), dna()]
                                )
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

class wound(world_object):
    def __init__(self):
        super(wound, self).__init__(
            name=["wound", "stomach"],
            true_name="Stomach Wound",
            description="Carefully lifting the victims hand, the wound can be seen clearly. There's a single incision on the left side of his stomach, about an inch wide. The size and shape means it was most likely made by an average sized knife, the kind that's commonly found in kitchens throughout households across the country. Great.",
            discovered=False,
            has_inv=True,
            inventory=[stab_wound()],
            state="Unseen",
            use_item=[]
        )
    def look_desc(self, player):
        if self.state == "Unseen":
            self.inventory = []
            stab_wound().discovered = True
            player.evidence.append(stab_wound())
            self.state = "Seen"
        return "{}\n".format(self.description)

class counter(world_object):
    def __init__(self):
        super(counter, self).__init__(
                                        name=["counter", "worktop", "counters", "kitchen counter", "kitchen counters", "north counter", "west counter"],
                                        true_name="Kitchen Counter",
                                        description="The counters running against two walls of the kitchen are completely clear of all clutter - clearly Roger likes to keep his house in order. The only thing of note is a utensil holder, at the back of the counter against the wall.",
                                        discovered=False,
                                        has_inv=True,
                                        inventory=[utensil_holder()],
                                        state="",
                                        use_item=[]
                                    )

class utensil_holder(world_object):
    def __init__(self):
        super(utensil_holder, self).__init__(
            name=["utensil holder"],
            true_name="Utensil Holder",
            description="The utensil holder is a simple design - a long block of wood, with clearly defined slots for various wooden spoons, knives, stirrers, and other utensils I couldn't possibly name. There's only one thing missing - one of the slots, clearly intended for a large knife, is empty.",
            discovered=False,
            has_inv=True,
            inventory=[missing_knife()],
            state="Unseen",
            use_item=[]
        )
    def look_desc(self, player):
        if self.state == "Unseen":
            self.inventory = []
            missing_knife().discovered = True
            player.evidence.append(missing_knife())
            self.state = "Seen"
        return "{}\n".format(self.description)

class bins(world_object):
    def __init__(self):
        super(bins, self).__init__(
            name=["bins", "kitchen bins", "bin", "kitchen bin"],
            true_name="Kitchen Bins",
            description="There are two bins, one for general waste and another for recycling - but both are completely empty. They must have been emptied recently too, because the bin bags haven't been replaced. There's also a gap behind one of the bins, where it's been pulled away from the wall slightly.",
            discovered=False,
            has_inv=True,
            inventory=[behind_bins(), empty_bins()]
            state="Unseen",
            use_item=[]
        )
    def look_desc(self, player):
        if self.state == "Unseen":
            for item in self.inventory:
                if item.true_name == "Empty Bins":
                    self.inventory.remove(item)
            empty_bins().discovered = True
            player.evidence.append(empty_bins())
            self.state = "Seen"
        return "{}\n".format(self.description)

class behind_bins(world_object):
    def __init__(self):
        super(behind_bins, self).__init__(
            name=["behind bins", "behind bin"],
            true_name="Behind Bins",
            description="Peering behind the recycling bin, I see a smear of what looks like blood on the wall. Murder can certainly be messy, but this seems too far from the body to be simple cast off. It's also clearly been smudged at the edges - did someone try to clean up?",
            discovered=False,
            has_inv=True,
            inventory=[blood_smear()],
            state="Unseen",
            use_item=[]
        )
    def look_desc(self, player):
        if self.state == "Unseen":
            for item in self.inventory:
                if item.true_name == "Blood Smear":
                    self.inventory.remove(item)
            blood_smear().discovered = True
            player.evidence.append(blood_smear())
            self.state = "Seen"
        return "{}\n".format(self.description)
