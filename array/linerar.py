arr = [int(x) for x in input().split()]
key = int(input("Enter element to search: "))
if key in arr:
    print("Found at index", arr.index(key))
else:
    print("Not found")
