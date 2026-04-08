import re

string = input("Enter the main string: ")
sub = input("Enter the substring: ")

if re.search(sub, string):
    print("Substring found")
else:
    print("Substring not found")
