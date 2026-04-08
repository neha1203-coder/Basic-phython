def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

matrix = [
    [6, 9, 1],
    [4, 0, 8]
]

# Display original matrix
print("Original Matrix:")
for r in matrix:
    print(r)

# Display transpose
print("\nTranspose (without built-in):")
t = transpose(matrix)
for r in t:
    print(r)
