org = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {org}")

#first five elements
extract = org[0:5]
print(f"Extracted first five elements: {extract}")

#Reverse of extracted elements
# print(f"Reversed extracted elements: {extract.reverse()}") #why this is not working
# reverse = extract.reverse()
extract.reverse()
print(f"Reversed extracted elements: {extract}")


# print(f"Reversed extracted elements: {org[0:5][::-1]}") #how this work