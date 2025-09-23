# regex
# strings
# import re
# validate the input

#1 Match

import re 

pattern = "apple"
if re.match(pattern,"appapple"):
    print(True)
else:
    print("False")