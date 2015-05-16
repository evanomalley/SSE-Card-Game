'''
Parses spreedsheet tsv or csv to json

Daniel Santoro
'''

import sys, getopt
import re
import json
from json import JSONEncoder

#An array of all the files to parse
#Overridden if command line argument is used
input_files = ['projects.tsv']
#Variables for customization
img_extension = '.png'
img_folder = 'pictures'
#Output path
output_path = '../'

#Global variable for file type
file_type = ''


class CardEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Card:

    def __init__(self, num_copies, name, _type, subtype, abilities, flavor_text, img_path):
        copies_len = []
        for i in range(num_copies):
            copies_len.append(i)

        self.copies = copies_len
        self.type = _type
        self.subtype = subtype
        self.name = name
        self.img_path = img_path
        self.flavorText = flavor_text
        self.abilities = abilities

def file_write(output_name, json_array):
    output_file = output_path + output_name
    with open( output_file, 'w') as jsonfile:
        json.dump(json_array, jsonfile, cls=CardEncoder, indent=2)

class DataParser:

    def __init__(self):
        pass

    def parse(self):
        pass

class ProjectParser(DataParser):
    
    def parse(self, file_lines):

        header_dict = self.assign_header(get_line_values(file_lines[0]))

        json_array = []

        #Constants for project cards
        _type = 'project'
        subtype = ''

        #For each row, parse the values and create json objects of the cards
        for line in file_lines[1:]:
            row_split = get_line_values(line)

            #Make sure each row is as long as the header
            #Prevents index out of bounds
            while len(row_split) < len(header_dict):
                    row_split.append('')

            name = row_split[header_dict[_type + ' name']]

            #if no value in the name column, skip row
            if not name:
                continue

            #Try to assign the number of copies of the card, else skip row
            try:
                num_copies = int(row_split[header_dict['#']])
            except ValueError:
                continue

            abilities = self.abilities_text(row_split[header_dict['platform']], row_split[header_dict['size']])

            flavor_text = row_split[header_dict['flavor text']]

            img_path = img_folder + '/'+ _type + 's/' + re.sub(r'\s+','',name) + img_extension

            #Append a new card object to the array
            json_array.append(Card(num_copies, name, _type, subtype, abilities, flavor_text, img_path))

        file_write(_type + '.json', json_array)

    #Get header data, map header to index
    def assign_header(self, header):
        header_dict = {}

        for idx, col in enumerate(header):

            col = col.lower()
            if col == '#':
                header_dict['#'] = idx
            elif col == 'project name':
                header_dict['project name'] = idx
            elif col == 'flavor text':
                header_dict['flavor text'] = idx
            elif col == 'platform':
                header_dict['platform'] = idx
            elif col == 'size':
                header_dict['size'] = idx

        return header_dict

    def abilities_text(self, platform, size):
        commit = 0;
        pp = 0;

        size = size[0].upper() + size[1:].lower()
        if size == 'Small':
            pp = 3;
            commit = 10
        elif size == 'Medium':
            pp = 5;
            commit = 12
        elif size == 'Large':
            pp = 8;
            commit = 18

        platform = platform[0].upper() + platform[1:].lower()
        if platform == 'none':
            platform = 'Generic'
        return ['Type: ' + size + ', ' + platform,  
        'Project Points: ' + str(pp),
        'Story Points: ' + str(commit)]


class ActionParser(DataParser):

    def parse(self, file_lines):
        json_array = []
        #TODO
        print("Sorry parser yet to be implemented")

class StudentParser(DataParser):

    def parse(self, file_lines):
        json_array = []
        #TODO
        print("Sorry parser yet to be implemented")

def get_line_values(line):

    row = []

    if file_type == 'tsv':
        row = (line.strip().split('\t'))
    elif file_type == "csv":
        row = (lin.strip().split(','))

    return row


def main(argv):

    #Try command line arguments
    try:
        opts, args = getopt.getopt(argv, 'hi:', ['help', 'input='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-i', '--input'):
            global input_files 
            input_files = [arg]

    for input_file in input_files:
        with open(input_file) as f:
            file_lines = f.readlines()

            global file_type
            if input_file.endswith('.tsv'):
                file_type = 'tsv'
            elif input_file.endswith('.csv'):
                file_type = 'csv'

            #TODO Call the parsers
            #split first line (header) and look for the 'name' row
            parser = ProjectParser()
            parser.parse(file_lines)

#Prints the usage of the command line arguments
def usage():
    print 'usage: -i <inputfile>'

if __name__ == '__main__':
    main(sys.argv[1:])