marks = [23,43.4,34.3,54,32,64.90]
student = ["karan", "shashank",43,59,"priya"]
print(marks)
print(student)
print(type(marks))
print(type(student))
print(marks[0])
print(marks[2])
print(marks[4])
print(marks[5])
print(len(marks))

#mutable condition
print(student[3])
student[3]="shubham"
print(student)
print(student[1:4])  #slicing and in slicing ending index is not included but starting index is included
print(student[1:])
print(marks[:3])
