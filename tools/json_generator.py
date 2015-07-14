'''
Parses SSE Card Game tsv or csv spreedsheet  
to json format

Daniel Santoro
'''

import sys, getopt
import re
import json
from json import JSONEncoder

#An array of all the files to parse
input_files = ['projects.tsv']
#Variables for customization
img_folder = 'pictures'
output_path = '../data/'

#Global variable for file type - do not edit
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
    print(output_name + " json file has been created.")

class DataParser(object):

    def __init__(self):
        pass

    def parse(self, file_lines, header_fields):
        
        header_line = get_line_values(file_lines[0])
        header_dict = self.assign_header(header_fields, header_line)

        if not header_dict:
            print(_type + 'header is missing fields.\nCheck the readme for format')
            return

        header_length = len(header_line)
        json_array = []

        _type = ''
        #Grab the type of card from "type name" 
        for i,v in enumerate(header_line):
            s = str(v).lower()
            if "name" in s:
                _type = s.split(' ')[0]
                break


        #For each row, parse the values and create json objects of the cards
        for line in file_lines[1:]:
            row_split = get_line_values(line)

            #Make sure each row is as long as the header
            #Prevents index out of bounds
            while len(row_split) < header_length:
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

            #Assign a subtype, or an empty string if none
            try:
                subtype = self.parse_subtype(row_split[header_dict['subtype']])
            except KeyError:
                subtype = ''

            #Abilities are genereated by the specific card types
            abilities = self.abilities_text(row_split, header_dict)

            flavor_text = row_split[header_dict['flavor text']]

            img_path = img_folder + '/'+ _type + 's/' + re.sub(r'\s+','',name)

            #Append a new card object to the array
            json_array.append(Card(num_copies, name, _type, subtype, abilities, flavor_text, img_path))

        file_write(_type + '.json', json_array)

    def abilities_text(self):
        pass

    def parse_subtype(self, subtype):
        return ''

    #Get header data, map header to index, returns dictionary
    #Fields is an array of values that are needed for the card
    #header_line is a line that is being mapped to fields
    #If the header_line misses a field, it prints an error 
    #and returns an empty dictionary
    def assign_header(self, header_fields, header_line):
        header_dict = {}

        #Check if the header_line contains each field
        for field in header_fields:
            has_field = False
            for idx, col in enumerate(header_line):
                col = col.lower()
                if col == field:
                    has_field = True
                    header_dict[field] = idx

            if has_field == False:
                return []

        return header_dict

class ProjectParser(DataParser):

    def parse(self, file_lines):
        header_fields = ['#', 'project name', 'flavor text', 'platform', 'size']

        super(ProjectParser, self).parse(file_lines, header_fields)

    def abilities_text(self, row_split, header_dict):
        print('todo')
        return ''


def get_line_values(line):

    row = []
    #TODO potentially implement strategy method for parsing lines
    #Have seperate methods for each format parser

    if file_type == 'tsv':
        row = (line.strip().split('\t'))
    elif file_type == "csv":
        row = (lin.strip().split(','))

    return row

def main(argv):

    #todo command line args
    for input_file in input_files:
        with open(input_file) as f:
            file_lines = f.readlines()

            global file_type
            if input_file.endswith('.tsv'):
                file_type = 'tsv'
            elif input_file.endswith('.csv'):
                file_type = 'csv'
                print('csv files may not work as intended')
            else:
                print('Not a valid file type')
                continue

            #Looks through the header file for the type of parser
            header = get_line_values(file_lines[0])
            if any("project" in s.lower() for s in header):
                parser = ProjectParser()
            elif any("action" in s.lower() for s in header):
                parser = ActionParser()
            elif any("student" in s.lower() for s in header):
                parser = StudentParser()
            else:
                print("Not a recognized card type.\n")
                return
            parser.parse(file_lines)

#Prints the usage of the command line arguments
def usage():
    print 'usage: -i <inputfile>'

if __name__ == '__main__':
    main(sys.argv[1:])