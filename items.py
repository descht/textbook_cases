"""The definitions for all items found throughout the game."""

#Generic classes for an item-----------------------------------
class item(object):
    def __init__(self, name, true_name, description, discovered, obtainable):
        self.name = name
        self.true_name = true_name
        self.description = description
        self.discovered = discovered
        self.obtainable = obtainable
    def use_item(self):
        pass
    def __str__(self):
        return "{}\n=====\n{}\nDiscovered: {}\nObtainable: {}\n".format(self.name, self.description, self.discovered, self.obtainable)

#Specific items   --------------------------------------------
class notebook(item):
    def __init__(self):
        self.contents = {}
        super(notebook, self).__init__(name="notebook",
                                       true_name="Notebook",
                                       description="My pocket sized notebook, for jotting down notes on what happens in the case.",
                                       discovered=True,
                                       obtainable=True)
    def add_entry(self, new_key, new_entry):
        self.contents[new_key] = new_entry
    def remove_entry(self, remove_key):
        del self.contents[remove_key]
    def read_notebook(self):
        notebook_desc = ""
        for entry in self.contents.values():
            notebook_desc += " -- {}\n".format(str(entry))
        return notebook_desc


class pen(item):
    def __init__(self):
        super(pen, self).__init__(name="pen",
                                  true_name="Pen",
                                  description="A plain, blue biro. Would have preferred black, but it's the only pen I could find on whort notice when I was called.",
                                  discovered=True,
                                  obtainable=True)

class phone(item):
    def __init__(self):
        super(phone, self).__init__(name="phone",
                                    true_name="Phone",
                                    description="My mobile phone - a bulky classic from years ago. The battery will last all week, but if I want to do anything other than ring people I'll have to use a computer.",
                                    discovered=True,
                                    obtainable=True)
    def phone_call(self, phone_number):
        

class fingerprint(item):
    def __init__(self):
        super(fingerprint, self).__init__(name="fingerprint kit",
                                          true_name="Fingerprint Kit",
                                          description="A kit for gathering fingerprints from objects, out in the field. This kit comes with a brush, powder and tape.",
                                          discovered=True,
                                          obtainable=True)

class dna(item):
    def __init__(self):
        super(dna, self).__init__(name="dna kit",
                                  true_name="DNA Kit",
                                  description="A 'kit' for gathering DNA evidence, though the only thing it contains is a large bundle of cotten swabs.",
                                  discovered=True,
                                  obtainable=True)

class cigarettes(item):
    def __init__(self, amount):
        self.amount = amount
        super(cigarettes, self).__init__(name="cigarettes",
                                         true_name="Cigarettes",
                                         description="My pack of cigarettes. I find smoking always helps me process what I've seen in the case so far, and plan out what my next actions should be. Looks like there's only {} left.".format(self.amount),
                                         discovered=True,
                                         obtainable=True)
    def smoke(self):
        if self.amount == 0:
            return "Damn, I'm out. I'll have to remember to pick some up later."
        else:
            self.amount -= 1
            return "I pull out my lighter, and light a cigarette.\nSomething something text about getting a hint."

class lighter(item):
    def __init__(self):
        super(lighter, self).__init__(name="lighter",
                                      true_name="Lighter",
                                      description="My silver zippo lighter. It's been passed down for generations on my Father's side, though as far as I can tell I'm the first to actually use the damn thing.",
                                      discovered=True,
                                      obtainable=True)
