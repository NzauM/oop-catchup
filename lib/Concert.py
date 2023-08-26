class Concert:
    allconcerts = []
    def __init__(self, date, venue, band) :
        self.date = date
        self.venue = venue
        self.band = band
        Concert.allconcerts.append(self)
        pass

    @classmethod
    def all(cls):
        return cls.allconcerts
    
    def band(self):
        return self.band 
    
    def hometown_show(self):
        band_hometown = self.band.hometown
        venue_city = self.venue.city
        return band_hometown == venue_city
    
#     Concert hometown_show()
# returns true if the concert is in the band's hometown, false if it is not

    pass