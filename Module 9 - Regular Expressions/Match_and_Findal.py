'''
# match{pattern, string, flags}

import re

pattern = "apples"
if re.match(pattern,"apple"):
    print("True")
else:
    print("False")
'''

# findall{pattern, string, flags}

import re

pattern = "apple"
string = re.findall("apple", pattern)
print(string)