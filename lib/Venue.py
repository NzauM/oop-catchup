from Concert import Concert
class Venue:
    allvenues = []
    def __init__(self, title, city) :
        self.title = title
        self.city = city
        Venue.allvenues.append(self)
        pass

    @classmethod
    def all(cls):
        return cls.allvenues
    
    # returns an list of all the concerts for the venue
    def concerts(self):
        venue_concerts = []
        all_concerts = Concert.all()
        for i in all_concerts:
            if i.venue == self:
                venue_concerts.append(i)
        return venue_concerts
    
    def bands(self):
        # self.concerts()
        venue_bands = []
        for i in self.concerts():
            # band = i.band
            venue_bands.append(i.band)

        return venue_bands

            



    pass