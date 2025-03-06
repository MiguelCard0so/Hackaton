class NPC:
    def __init__(self, pos, items):
        self.pos = pos
        self.items = items
        self.dialogues = []
    
    def dialogue(self, int: input):
        return self.dialogues[input]

    # if the player does something, the NPC will drop an item
    def dropItem(self):
        return self.items.pop()