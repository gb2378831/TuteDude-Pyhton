name = input("Enter the student's name: ")
name = name.capitalize()

students_marks = {'Alice':85,'Ghanshyam':95,'James':90}

print(f"{name}'s marks:",students_marks.get(name,"Student not found."))

#           OR

# if name in students_marks:
#     print(f"{name}'s marks: {students_marks[name]}")
# else:
#     print("Student not found.")