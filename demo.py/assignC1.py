import random

lst = [random.randint(1, 20) for _ in range(10)]
print("Original list:", lst)

lst = list(set(lst))   # remove duplicates
lst.sort(reverse=True)

print("Final list:", lst)
