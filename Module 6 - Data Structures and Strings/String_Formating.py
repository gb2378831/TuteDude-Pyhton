
'''
name = "Mike"
number = len(name)*3
print("Hello {}, your lucky number is {}.".format(name,number))
print(f"Hello {name}, your lucky number is {number}.")
'''

'''
example = "format() method"
string = "This is an example of {} on a string.".format(example)
print(string)
'''

'''
first = "apple"  #0
second = "ball"  #1
third = "cat"    #2
string = "{0} {2} {1}.".format(first,second,third)
print(string)
'''


price = 150 
with_tax = 150 + 50
print(price, with_tax)
print("Price: is Rs{:.2f}. With tax: Rs{:.2f}".format(price,with_tax)) # {:.2f} means it contains upto 2 float numbers.