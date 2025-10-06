arr = [int(x) for x in input().split()]
even = sum(1 for i in arr if i%2==0)
odd = len(arr) - even
print("Even =", even, "Odd =", odd)
