# class and object

class TV:
    def __init__(self, channel, id, trp):
        self.channel = channel
        self.id = id
        self.trp = trp

ekattor = TV("Ekattor", 25, 1.2)

print(ekattor.channel) # -> Ekattor

print(ekattor.trp) # -> 1.2
