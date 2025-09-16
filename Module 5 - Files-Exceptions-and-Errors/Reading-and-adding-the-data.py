# r+ ---> write and read

file = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Module 5 - Files-Exceptions-and-Errors\\myfile.txt','r+')
writing = file.write('welcome')
print(writing)
file.close()

file = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Module 5 - Files-Exceptions-and-Errors\\myfile.txt','r+')
read  = file.read()
print(read)
file.close