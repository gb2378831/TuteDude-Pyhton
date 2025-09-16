file1  = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Module 5 - Files-Exceptions-and-Errors\\myfile.txt', 'w')
writing = file1.write("Hello My Name is Ghanshyam")
# print(writing)
file1.close()

# file1 = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Module 5 - Files-Exceptions-and-Errors\\myfile.txt', 'r')
# reading = file1.read()
# print(reading)
# file1.close()

file1 = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Module 5 - Files-Exceptions-and-Errors\\myfile.txt','a')

appending = file1.write('/nWelcome to this lecture. ')
# print(appending)

file1.close()



file1 = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Module 5 - Files-Exceptions-and-Errors\\myfile.txt', 'r')
reading = file1.read()
print(reading)
file1.close()
