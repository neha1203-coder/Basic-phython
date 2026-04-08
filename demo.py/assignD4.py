t = (21, 42, 84, 168, 336)

x = int(input("Enter element to search: "))

found = False

for item in t:
    if item == x:
        found = True
        break

if found:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")