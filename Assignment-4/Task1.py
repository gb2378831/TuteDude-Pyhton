try:
    print("Reading file content:\n")
    file = open('C:\\Users\\Ghanshyam\\Documents\\TUTE_DUDE PYTHON\\Assignment-4\\sample.txt','r+')

    line_no = 1
    for i in file:
        print(f"Line {line_no}: {i}", end='')
        line_no += 1
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")