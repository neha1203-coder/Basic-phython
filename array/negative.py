arr = [int(x) for x in input().split()]
pos = sum(1 for i in arr if i>0)
neg = sum(1 for i in arr if i<0)
print("Positive =", pos, "Negative =", neg)
