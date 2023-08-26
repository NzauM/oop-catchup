#!/usr/bin/env python3
import ipdb;
from Band import Band
from Venue import Venue
from Concert import Concert


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    moringa = Band("Moringa","Westie")
    kicc = Venue("Kicc centre", "Nairobi")
    kicc2 = Venue("Kicc centre", "Nairobi")
    moringafest = Concert("2020/04/25", kicc,moringa)









# DO NOT REMOVE THIS
    ipdb.set_trace()
