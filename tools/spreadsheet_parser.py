"""
Parses spreadsheet -> json
Kocsen Chung
Dan Santoro
Winning
"""
import json
from json import JSONEncoder

input_file = "acards.tsv"
output_file = '../action.json'


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
        self.stats = [description]


def main():
    with open(input_file) as f:
        file_lines = f.readlines()

    json_ary = []
    for line in file_lines:
        split = line.strip().split("\t")
        # print(split)
        if len(split) <= 4:
            continue

        try:
            num_copies = int(split[0])
        except ValueError:
            continue

        _type = "action"
        name = split[1]
        subtype = split[2]
        # ignore split[3]
        description = split[4]
        try:
            flavor_text = split[5]
        except IndexError:
            flavor_text = ""

        card = Card(num_copies, _type, subtype, name, "ADDMANUALLY", flavor_text, description)
        json_ary.append(card)

    # Dump to array
    with open( output_file, 'w') as jsonfile:
        json.dump(json_ary, jsonfile, cls=CardEncoder, indent=2)


if __name__ == "__main__":
    main()




