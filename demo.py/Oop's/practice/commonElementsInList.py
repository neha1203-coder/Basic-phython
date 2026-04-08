lst1 = list(map(int,input("enter first list: ").split()))
lst2 = list(map(int,input("enter second list: ").split()))
common = list(set(lst1)&set(lst2))
print("common elements: ",common)