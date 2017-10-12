"""The definitions for all items found throughout the game."""

#Generic classes for an item-----------------------------------
class item(object):
    def __init__(self, name, true_name, state, description, discovered, obtainable):
        self.name = name
        self.true_name = true_name
        self.state = state
        self.description = description
        self.discovered = discovered
        self.obtainable = obtainable
    def use_item(self):
        return "That can't be used like that."
    def modify_object(self):
        return "That doesn't work like that."
    def look_desc(self, player):
        return self.description
    def __str__(self):
        return "{}\n=====\n{}\nDiscovered: {}\nObtainable: {}\n".format(self.name, self.description, self.discovered, self.obtainable)

class evidence(item):
    def __init__(self, name, true_name, state, description, discovered, obtainable, combines, combo_text):
        self.combines = combines
        self.combo_text = combo_text
        super(evidence, self).__init__(name, true_name, state, description, discovered, obtainable)
    def combines(self, player, second_item):
        if second_item.combines == self.combines and self.combines != -1:
            player.evidence.remove(second_item)
            player.evidence.remove(self)
            return self.combo_text
        else:
            return "Those two don't go together."


#Specific items   --------------------------------------------
class notebook(item):
    def __init__(self):
        self.contents = {}
        super(notebook, self).__init__(name=["notebook"],
                                       true_name="Notebook",
                                       state="",
                                       description="My pocket sized notebook, for jotting down notes on what happens in the case.",
                                       discovered=True,
                                       obtainable=True)
    def add_entry(self, new_key, new_entry):
        self.contents[new_key] = new_entry
    def remove_entry(self, remove_key):
        del self.contents[remove_key]
    def use_item(self):
        notebook_desc = ""
        for entry in self.contents.values():
            notebook_desc += " -- {}\n".format(str(entry))
        return notebook_desc


class pen(item):
    def __init__(self):
        super(pen, self).__init__(name=["pen"],
                                  true_name="Pen",
                                  state="",
                                  description="A plain, blue biro. Would have preferred black, but it's the only pen I could find on whort notice when I was called.",
                                  discovered=True,
                                  obtainable=True)

class phone(item):
    def __init__(self):
        self.numbers = {}
        super(phone, self).__init__(name=["phone"],
                                    true_name="Phone",
                                    state="",
                                    description="My mobile phone - a bulky classic from years ago. The battery will last all week, but if I want to do anything other than ring people I'll have to use a computer.",
                                    discovered=True,
                                    obtainable=True)
    def modify_object(self, new_contact):
        self.numbers[new_contact] = 0
    def use_item(self):
        if len(self.numbers) == 0:
            return "I don't have anyones numbers yet - at least, none that are in any way relevant to this case"
        else:
            print "Who shall I ring?"
            for key in self.numbers.keys():
                print "-- {}".format(key.title())
                print "Cancel"
                chosen = raw_input("> ").lower()
                if chosen == "cancel":
                    return "Guess there's no one I need to speak to now."
            else:
                for key in self.numbers.keys():
                    if key == chosen:
                        return "I dial the number for {}.".format(chosen)
                    return "I don't know that number."

class fingerprint(item):
    def __init__(self):
        super(fingerprint, self).__init__(name=["fingerprint kit"],
                                          true_name="Fingerprint Kit",
                                          state="Incomplete",
                                          description="A kit for gathering prints in the field. It comes with a brush, powder, tape and ink.",
                                          discovered=True,
                                          obtainable=True)
    def modify_object(self, player, use_item):
        if use_item in notebook().name:
            if self.state == "Incomplete":
                self.state = "Complete"
                self.description += " The kit's run out of card for the print transfers... it's not ideal, but I can use some pages from my notebook for now."
                return "A couple of pages should do for now, but I really shouldn't make a habit of these workarounds."
            elif self.state == "Complete":
                return "I've already added some notebook pages to the kit, I don't need to add any more just yet."
        else:
            return "That doesn't work like that."


class dna(item):
    def __init__(self):
        super(dna, self).__init__(name=["dna kit"],
                                  true_name="DNA Kit",
                                  state="",
                                  description="A kit for gathering DNA evidence, containing a bundle of cotten swabs. I'm pretty sure they come from the same place as the ones in my bathroom at home.",
                                  discovered=True,
                                  obtainable=True)

class cigarettes(item):
    def __init__(self, amount):
        self.amount = amount
        super(cigarettes, self).__init__(name=["cigarettes"],
                                         true_name="Cigarettes",
                                         state="",
                                         description="My pack of cigarettes. I find smoking always helps me process what I've seen in the case so far, and plan out what my next actions should be. Looks like there's only {} left.".format(self.amount),
                                         discovered=True,
                                         obtainable=True)
    def use_item(self):
        if self.amount == 0:
            return "Damn, I'm out. I'll have to remember to pick some up later."
        else:
            self.amount -= 1
            return "I pull out my lighter, and light a cigarette.\nSomething something text about getting a hint."

class lighter(item):
    def __init__(self):
        super(lighter, self).__init__(name=["lighter"],
                                      true_name="Lighter",
                                      state="",
                                      description="My silver zippo lighter. It's been passed down for generations on my Father's side, though as far as I can tell I'm the first to actually use the damn thing.",
                                      discovered=True,
                                      obtainable=True)

#Evidence -----------------------

class victim_fingerprints(evidence):
    def __init__(self):
        super(victim_fingerprints, self).__init__(name=["victims fingerprints", "victim's fingerprints"],
                                                  true_name="Victim's Fingerprints",
                                                  state="",
                                                  description="A copy of the victim's fingerprints, on a page from my notebook.",
                                                  discovered=True,
                                                  obtainable=True,
                                                  combines=-1,
                                                  combo_text="")

class victim_dna(evidence):
    def __init__(self):
        super(victim_dna, self).__init__(name=["victims dna", "victim's dna"],
                                         true_name="Victim's DNA",
                                         state="",
                                         description="A swab of DNA, taken from the victim.",
                                         discovered=True,
                                         obtainable=True,
                                         combines=-1,
                                         combo_text="")

class missing_knife(evidence):
    def __init__(self):
        super(missing_knife, self).__init__(name=["utensil holder", "missing knife", "empty knife slot"],
                                            true_name="Missing Knife from Kitchen",
                                            state="Unseen",
                                            description="An empty slot in the utensil holder, intended to hold a sharp knife. It might mean nothing, but it seems a little odd given how pristine the rest of the kitchen is.",
                                            discovered=False,
                                            obtainable=False,
                                            combines=0,
                                            combo_text="Combined the knife and the wound.")
    def look_desc(self, player):
        if self.state == "Unseen":
            self.state = "Seen"
            player.evidence.append(self)
            return "The utensil holder is the only thing of note on the counters - a long block of wood, with clearly defined slots for various wooden spoons, knives, stirrers, and other utensils I couldn't possibly name. There's only one thing amiss - one of the slots, clearly intended for a large knife, is empty. It might mean nothing, but I'll make a note of it just in case."
        else:
            return self.description

class stab_wound(evidence):
    def __init__(self):
        super(stab_wound, self).__init__(name=["wound", "stomach"],
                                         true_name="Stab Wound on Victim",
                                         state="Unseen",
                                         description="The fatal wound on the victim. The wound only looks to be about an inch wide, meaning the murder weapon itself isn't too big - about the size of standard kitchen knife.",
                                         discovered=False,
                                         obtainable=False,
                                         combines=0,
                                         combo_text="Combined the wound and the knife.")
    def look_desc(self, player):
        if self.state == "Unseen":
            self.state = "Seen"
            self.name.append("stab wound")
            self.name.append("knife wound")
            player.evidence.append(self)
            return "I carefully lift the victims hand, and check the wound. There's a single wound on the left side of his stomach, about an inch wide. The size and shape means it was most likely made by an average sized knife, the kind that's commonly found in kitchens throughout households across the country. Great."
        else:
            return self.description
