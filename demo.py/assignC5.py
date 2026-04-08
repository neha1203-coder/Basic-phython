list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print("List1: ", list1)
print("List2: ", list2)

merged = list1 + list2
final_list = list(set(merged))

print("Merged list without duplicates:", final_list)
