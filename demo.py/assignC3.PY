lst = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original list: ",lst)

even_squares = [x * x for x in lst if x % 2 == 0]

print("Squares of even numbers:", even_squares)
