"""
Parses spreedsheet tsv or csv to json

Daniel Santoro
"""

import re
import json
from json import JSONEncoder



class CardEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Card:

    def __init__(self, num_copies, _type, subtype, name, img_path, flavor_text, description):
        copies_len = []
        for i in range(num_copies):
            copies_len.append(i)

        self.copies = copies_len
        self.type = _type
        self.subtype = subtype
        self.name = name
        self.img = img_path
        self.flavorText = flavor_text
        self.stats = description

class DataParser:

    def __init__(self):
        pass

    def parse(self):
        pass

class ProjectParser(DataParser):
    
    def parse(self):
        #TODO

class ActionParser(DataParser):

    def parse(self):
        #TODO

class StudentParser(DataParser):

    def parse(self):
        #TODO



def main():
    #TODO

if __name__ == "__main__":
    main()