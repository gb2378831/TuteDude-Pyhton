#Taking input
entry = input("Enter text to write to the file: ")

#Appending to file
with open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Assignment-4\\output.txt','w') as file:
    write = file.write(entry + '\n')
print("Data successfully written to output.txt.\n")

entry = input("Enter additional text to append: ")

with open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Assignment-4\\output.txt',"a") as file:
    write = file.write(entry + '\n')
    print("Final content of output.txt:")
    # read = file.read()
    # print(read)

with open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Assignment-4\\output.txt','r') as file:
    read = file.read()
    print(read)