file1  = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Files, Exceptions and Errors\\myfile.txt', 'w')
writing = file1.write("Hello My Name is Ghanshyam")
print(writing)
file1.close()

file1 = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Files, Exceptions and Errors\\myfile.txt', 'r')
reading = file1.read()
print(reading)
file1.close()
