This is a readme for how to use the card json parser.

Currently the parser only takes tsv files. 
TODO csv files support

This document will cover how to set up the ordering of the input files.
All files' first row (header) must contain #,  *type* name, and then the title of any additional fields

''#'' represents the number of those cards

#Formating
This is how the header of different files are formated. 
Each row requires a value for # and name to be considered.
Other required values are notated by a ''*''

##Actions
''#'', Action Name, subtype, Action''*'', Flavor text

##Projects
''#'', Project Name, Flavor text, Platform''*'', Size''*''

##Students
''#'', Student Name, Specialization, Flavor text, Custom Ability
