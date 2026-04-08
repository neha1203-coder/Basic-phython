matrix = [
    [6, 9, 1],
    [4, 0, 8]
]

# Display original matrix
print("Original Matrix:")
for r in matrix:
    print(r)

# Transpose using zip()
transpose = list(zip(*matrix))

print("\nTranspose (using zip):")
for r in transpose:
    print(list(r))
