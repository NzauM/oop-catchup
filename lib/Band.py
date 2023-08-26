class Band:
    allbands = []
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown
        Band.allbands.append(self)

    def gethometown(self):
        return self._hometown
    
    def sethometown(self, newhometown):
        if(newhometown != "Nairobi"):
            self._hometown = newhometown
        else:
            print("A nairobian is not accepted")


    hometown = property(gethometown, sethometown)

    @classmethod
    def all(cls):
        return cls.allbands
    pass

