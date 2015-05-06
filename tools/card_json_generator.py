"""
Parses spreedsheet tsv or csv to json

Daniel Santoro
"""

import re
import json
from json import JSONEncoder

#An array of all the files to parse
input_files = ["pcards.tsv"]
#Variables for customization
img_extension = '.png'
img_folder = 'pictures'
#Output files
project_file = '../project.json'
action_file = '../action.json'
student_file = '../student.json'


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
        self.img_path = img_path
        self.flavorText = flavor_text
        self.stats = description

def FileWrite(output_file):
    with open( output_file, 'w') as jsonfile:
        json.dump(json_ary, jsonfile, cls=CardEncoder, indent=2)

class DataParser:

    def __init__(self):
        pass

    def parse(self):
        pass

class ProjectParser(DataParser):
    
    def parse(self, split):
        json_aray = []
        #TODO

class ActionParser(DataParser):

    def parse(self, split):
        json_aray = []
        #TODO

class StudentParser(DataParser):

    def parse(self, split):
        json_aray = []
        #TODO

def get_lines(input_file):
    with open(input_file) as f:
        file_lines = f.readlines()

    for line in file_lines:
        lines = []
        if f.endswith('.tsv'):
            lines.append(line.strip().split("\t"))
        else if f.endswith('.csv'):
            lines.append(lin.strip().split(","))


def main():
    #TODO
    for input_file in input_files
        lines = get_lines(input_file)
        





    

if __name__ == "__main__":
    main()