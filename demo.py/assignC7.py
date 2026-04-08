A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

# Display original matrices
print("Matrix A:")
for r in A:
    print(r)

print("\nMatrix B:")
for r in B:
    print(r)

# Matrix multiplication
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

# Display result
print("\nMatrix Multiplication Result (A × B):")
for r in result:
    print(r)
