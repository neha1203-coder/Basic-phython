s = input("Enter a string: ")

i = 0
j = len(s) - 1
flag = True

while i < j:
    if s[i] != s[j]:
        flag = False
        break
    i += 1
    j -= 1

if flag:
    print(True)
else:
    print(False)
