"""
Parses spreadsheet -> json
Kocsen Chung
Dan Santoro
Winning
"""
import re
import json
from json import JSONEncoder

input_file = "scards.tsv"
output_file = '../people.json'
img_folder = 'students'
img_extension = '.jpg'

class CardEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Card:
    """
    Card representation
    """

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

def parse_stats(description):
    if (description== 'Desktop'):
        return ['Desktop Commits +2','Base Commit +1']
    elif(description == 'Mobile'):
        return ['Mobile Commits +2','Base Commit +1']
    elif(description == 'Web'):
        return ['Web Commits +2','Base Commit +1']
    else:
        return ['Base Commit +2']

def main():
    with open(input_file) as f:
        file_lines = f.readlines()

    json_ary = []
    for line in file_lines:
        split = line.strip().split("\t")
        # print(split)
        if len(split) <= 4:
            continue

        _type = "student"
        name = split[1]
        # ignore split[3]
        description = parse_stats(split[2]);
        try:
            flavor_text = split[4]
        except IndexError:
            flavor_text = ""

        img_path = img_folder + '/' + re.sub(r'\s+','_',name) + img_extension

        card = Card(1, _type, "", name, img_path, flavor_text, description)
        json_ary.append(card)

    # Dump to array
    with open( output_file, 'w') as jsonfile:
        json.dump(json_ary, jsonfile, cls=CardEncoder, indent=2)


if __name__ == "__main__":
    main()




