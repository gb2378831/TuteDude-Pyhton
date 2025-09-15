'''
# 1
file1 = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Files, Exceptions and Errors\\myfile.txt', 'r')

# reading = file1.read(6)
read = file1.readline()
print(reading)

file1.close()
'''

# 2
with open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Files, Exceptions and Errors\\myfile.txt','r') as file1:
    reading = file1.read()
    print(reading)