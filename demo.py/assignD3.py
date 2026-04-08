# Storing student records as tuples
student1 = ("Ram", 1, 85)
student2 = ("Shyam", 2, 78)
student3 = ("Mohan", 3, 85)   # duplicate record

# Creating a tuple of student records
students = (student1, student2, student3)

# Converting tuple into a set to remove duplicates
unique_students = set(students)

# Display unique records
print("Unique student records:")
for s in unique_students:
    print(s)
