numbers = (31, 16, 20, 19, 17)

max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Tuple:", numbers)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

