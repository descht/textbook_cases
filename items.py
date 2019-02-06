"""The definitions for all items found throughout the game."""
# from rooms import *


# Generic classes for an item-----------------------------------
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
        return "{}\n".format(self.description)

    def __str__(self):
        return "{}\n=====\n{}\nDiscovered: {}\nObtainable: {}\n".format(self.name, self.description, self.discovered, self.obtainable)


class evidence(item):
    def __init__(self, name, true_name, state, description, discovered, obtainable, combines, combo_text):
        self.combines = combines
        self.combo_text = combo_text
        super(evidence, self).__init__(name, true_name, state, description, discovered, obtainable)

    def compares(self, player, second_item):
        if second_item.combines.true_name == self.combines.true_name and self.combines != -1:
            player.evidence.remove(second_item)
            player.evidence.remove(self)
            player.evidence.append(self.combines)
            return "{}\n".format(self.combo_text)
        else:
            return "Those two don't go together."


# Specific items   --------------------------------------------
class notebook(item):
    def __init__(self):
        self.contents = {}
        super(notebook, self).__init__(
                                        name=["notebook"],
                                        true_name="Notebook",
                                        state="",
                                        description="My pocket sized notebook, for jotting down notes on what happens in the case.",
                                        discovered=True,
                                        obtainable=True
                                    )

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
        super(pen, self).__init__(
                                    name=["pen"],
                                    true_name="Pen",
                                    state="",
                                    description="A plain, blue biro. Would have preferred black, but it's the only pen I could find on whort notice when I was called.",
                                    discovered=True,
                                    obtainable=True
                                )


class phone(item):
    def __init__(self):
        self.numbers = {}
        super(phone, self).__init__(
                                    name=["phone"],
                                    true_name="Phone",
                                    state="",
                                    description="My mobile phone - a bulky classic from years ago. The battery will last all week, but if I want to do anything other than ring people I'll have to use a computer.",
                                    discovered=True,
                                    obtainable=True
                                )

    def modify_object(self, new_contact):
        self.numbers[new_contact] = 0

    def use_item(self):
        if len(self.numbers) == 0:
            return "I don't have anyones numbers yet - at least, none that are in any way relevant to this case"
        else:
            print("Who shall I ring?")
            for key in self.numbers.keys():
                print("-- {}".format(key.title()))
                print("Cancel")
                chosen = input("> ").lower()
                if chosen == "cancel":
                    return "Guess there's no one I need to speak to now."
                else:
                    for key in self.numbers.keys():
                        if key == chosen:
                            return "I dial the number for {}.".format(chosen)
                        return "I don't know that number."


class fingerprint(item):
    def __init__(self):
        super(fingerprint, self).__init__(
                                            name=["fingerprint kit"],
                                            true_name="Fingerprint Kit",
                                            state="Incomplete",
                                            description="A kit for gathering prints in the field. It comes with a brush, powder, tape and ink.",
                                            discovered=True,
                                            obtainable=True
                                        )

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
        super(dna, self).__init__(
                                    name=["dna kit"],
                                    true_name="DNA Kit",
                                    state="",
                                    description="A kit for gathering DNA evidence, containing a bundle of cotten swabs. I'm pretty sure they come from the same place as the ones in my bathroom at home.",
                                    discovered=True,
                                    obtainable=True
                                )


class cigarettes(item):
    def __init__(self, amount):
        self.amount = amount
        super(cigarettes, self).__init__(
                                            name=["cigarettes"],
                                            true_name="Cigarettes",
                                            state="",
                                            description="My pack of cigarettes. I find smoking always helps me process what I've seen in the case so far, and plan out what my next actions should be. Looks like there's only {} left.".format(self.amount),
                                            discovered=True,
                                            obtainable=True
                                        )

    def use_item(self):
        if self.amount == 0:
            return "Damn, I'm out. I'll have to remember to pick some up later."
        else:
            self.amount -= 1
            return "I pull out my lighter, and light a cigarette.\nSomething something text about getting a hint."


class lighter(item):
    def __init__(self):
        super(lighter, self).__init__(
                                        name=["lighter"],
                                        true_name="Lighter",
                                        state="",
                                        description="My silver zippo lighter. It's been passed down for generations on my Father's side, though as far as I can tell I'm the first to actually use the damn thing.",
                                        discovered=True,
                                        obtainable=True
                                    )


# Evidence -----------------------
class victim_fingerprints(evidence):
    def __init__(self):
        super(victim_fingerprints, self).__init__(
                                                    name=["victims fingerprints", "victim's fingerprints"],
                                                    true_name="Victim's Fingerprints",
                                                    state="",
                                                    description="A copy of the victim's fingerprints, on a page from my notebook.",
                                                    discovered=True,
                                                    obtainable=True,
                                                    combines=-1,
                                                    combo_text=""
                                                )


class victim_dna(evidence):
    def __init__(self):
        super(victim_dna, self).__init__(
                                            name=["victims dna", "victim's dna"],
                                            true_name="Victim's DNA",
                                            state="",
                                            description="A swab of DNA, taken from the victim.",
                                            discovered=True,
                                            obtainable=True,
                                            combines=-1,
                                            combo_text=""
                                        )


class missing_knife(evidence):
    def __init__(self):
        super(missing_knife, self).__init__(
                                            name=["missing knife", "empty knife slot"],
                                            true_name="Missing Knife from Kitchen",
                                            state="",
                                            description="There appears to be a single knife missing from the kitchen. It might mean nothing, but it seems a little odd given how pristine the rest of the kitchen is.",
                                            discovered=False,
                                            obtainable=False,
                                            combines=knife_from_kitchen(),
                                            combo_text="A stab wound made by a regular kitchen knife, and a spot from which a kitchen knife is obviously missing. Not a very groundbreaking deduction, but the most likely answer at this point is that the victim was killed using a knife found on the scene, before the knife was removed somehow. This could also just be a coincidence, but to find out either way I really need to track down that knife."
                                        )


class stab_wound(evidence):
    def __init__(self):
        super(stab_wound, self).__init__(
                                            name=["stab wound", "knife wound", "incision"],
                                            true_name="Stab Wound on Victim",
                                            state="",
                                            description="The fatal wound on the victim. The wound only looks to be about an inch wide, meaning the murder weapon itself isn't too big - about the size of standard kitchen knife.",
                                            discovered=False,
                                            obtainable=False,
                                            combines=knife_from_kitchen(),
                                            combo_text="A stab wound made by a regular kitchen knife, and a spot from which a kitchen knife is obviously missing. Not a very groundbreaking deduction, but the most likely answer at this point is that the victim was killed using a knife found on the scene, before the knife was removed somehow. This could also just be a coincidence, but to find out either way I really need to track down that knife."
                                        )


class knife_from_kitchen(evidence):
    def __init__(self):
        super(knife_from_kitchen, self).__init__(
                                                    name=["murder weapon from kitchen", "murder weapon from scene"],
                                                    true_name="Murder Weapon is from the Scene",
                                                    state="",
                                                    description="The victim was stabbed, and the most likely weapon at the moment seems like one of the knives from the scene, which is currently missing. Did the murderer dispose of it?",
                                                    discovered=True,
                                                    obtainable=False,
                                                    combines=knife_disposed_of(),
                                                    combo_text="The blood near the bin seems too far from the body, but it definitely could have come from the murder weapon. The kitchen knife is still missing - did the killer throw it in the bin?"
                                                )


class empty_bins(evidence):
    def __init__(self):
        super(empty_bins, self).__init__(
            name=["empty bin", "empty bins", "empty kitchen bins", "empty kitchen bin"],
            true_name="Empty Kitchen Bins",
            state="",
            description="The kitchen bins are both empty, and the bin bags haven't been replaced.",
            discovered=False,
            obtainable=False,
            combines=knife_in_bin(),
            combo_text="The blood appears to indicate the murder weapon was thrown in the bin, but both bins have been emptied. There's no sign of the bags here in the kitchen - where would the killer take them?"
        )

    def compares(self, player, second_item):
        if second_item.combines.true_name == self.combines.true_name and self.combines != -1:
            player.evidence.remove(second_item)
            player.evidence.remove(self)
            player.evidence.append(self.combines)
            import rooms
            player.currentroom.connects.append(rooms.Outside())
            return "{}\n".format(self.combo_text)
        else:
            return "Those two don't go together."


class blood_smear(evidence):
    def __init__(self):
        super(blood_smear, self).__init__(
            name=["blood smear", "blood"],
            true_name="Blood Smear",
            state="",
            description="A smear of blood found in the kitchen, behind the bins. It seems like someone attempted to clean this up as well.",
            discovered=False,
            obtainable=False,
            combines=knife_disposed_of(),
            combo_text="The blood near the bin seems too far from the body, but it definitely could have come from the murder weapon. The kitchen knife is still missing - did the killer throw it in the bin?"
        )


class knife_disposed_of(evidence):
    def __init__(self):
        super(knife_disposed_of, self).__init__(
            name=["knife disposed of", "knife disposed", "knife has been disposed", "knife has been disposed of"],
            true_name="Knife has been Disposed of?",
            state="",
            description="The missing kitchen knife is the most likely murder weapon at this point, and there's a bloody smear behind the kitchen bin - did the killer throw it inside?",
            discovered=True,
            obtainable=False,
            combines=knife_in_bin(),
            combo_text="The blood appears to indicate the murder weapon was thrown in the bin, but both bins have been emptied. There's no sign of the bags here in the kitchen - where would the killer take them?"
        )

    def compares(self, player, second_item):
        if second_item.combines.true_name == self.combines.true_name and self.combines != -1:
            player.evidence.remove(second_item)
            player.evidence.remove(self)
            player.evidence.append(self.combines)
            import rooms
            player.currentroom.connects.append(rooms.Outside())
            return "{}\n".format(self.combo_text)
        else:
            return "Those two don't go together."


class knife_in_bin(evidence):
    def __init__(self):
        super(knife_in_bin, self).__init__(
            name=["knife in bin bag", "knife in missing bin bag"],
            true_name="Knife in the Missing Bin Bag",
            state="",
            description="The missing knife was most likely thrown in one of the bin bags, and then the bags themselves were moved somewhere. But where?",
            discovered=True,
            obtainable=False,
            combines=-1,
            combo_text=""
        )

