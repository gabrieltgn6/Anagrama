import re

my_string = ("holaque tal estamos")
my_other_string = ("adios que me canso")

match = (re.match("holaque tal", my_string, re.I))
print (match)