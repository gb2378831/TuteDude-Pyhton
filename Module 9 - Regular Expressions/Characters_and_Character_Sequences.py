# CHARACTERS AND CHARACTER SEQUENCES

# ^ - Matches the begining of a line
# $ - Matches the end of a line 
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non-digit
# \s - Matches whitespace
# \S - Matches any non-whitespace


import re
string = "It is a dog"
pattern = "."
print(re.findall(pattern,string,flags=0))


# CHARACTERS AND CHARACTER SEQUENCES

# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression 0 to 1 times

import re
string = "From bobby.mark@mail.com"
pattern = "ma+"
pattern = "^F.+?"
pattern = "^From (\S+@\S+)"
print(re.findall(pattern,string))


# CHARACTERS AND CHARACTER SEQUENCES

# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character
# [a-z 0-9] - Set of characters can include a range
# {}

'''
import re
string = "pythonn 3.0"
pattern = "[aeiou]"
pattern = "[^xyz]"
pattern = "[a-z 0-9]"
pattern = "[A-Z]"
pattern = "python{0}"
print(re.findall(pattern,string,flags=0))
'''

import re
string = "From bobby.mark@mail.com"
pattern = "@([^ ]*)"
print(re.findall(pattern,string,flags=0))