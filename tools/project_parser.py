"""
Parses tab seperated values -> json
Kocsen Chung
Daniel Santoro
Winning
"""
import re
import json
from json import JSONEncoder

input_file = "pcards.tsv"
output_file = '../project.json'
img_folder = 'projects'
img_extension = '.png'

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

def parse_stats(platform, size):
    commit = 0;
    if size == 'Small':
        commit = 10
    elif size == 'Medium':
        commit = 12
    elif size == 'Large':
        commit = 18

    if platform == 'None':
        platform = 'Generic'
    return ['Type: ' + platform, 'Commits Required: ' + str(commit)]

def main():
    with open(input_file) as f:
        file_lines = f.readlines()

    json_ary = []
    for line in file_lines:
        split = line.strip().split("\t")
        # print(split)

        if len(split) <= 2:
            continue

        try:
            num_copies = int(split[1])
        except ValueError:
            continue

        _type = "project"
        subtype = ''
        name = split[2]
        try:
            flavor_text = split[3]
        except IndexError:
            flavor_text = ""

        description = parse_stats(split[4], split[5])

        img_path = img_folder + '/' + re.sub(r'\s+','',name) + img_extension

        card = Card(num_copies, _type, subtype, name, img_path, flavor_text, description)
        json_ary.append(card)

    # Dump to array
    with open( output_file, 'w') as jsonfile:
        json.dump(json_ary, jsonfile, cls=CardEncoder, indent=2)


if __name__ == "__main__":
    main()




