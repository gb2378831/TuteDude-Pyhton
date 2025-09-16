dictionary = {'a':'apple','b':'ball','c':'cat','d':'dog'}

#Adding elements to it
dictionary['e'] = 'elephant'

# Deleting elements from it
del(dictionary['c'])

print(dictionary)

#Checking elements in it
print('b' in dictionary)

#Getting all the keys from it
print(dictionary.keys())

#Getting all the values from it
print(dictionary.values())

#Returning none, if there is no key
print(dictionary.get('g','Key Not Found'))