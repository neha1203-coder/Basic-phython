lst = list(map(int,input("enter numbers: ").split()))
length = len(lst)
for i in range(length):
        count = 1
        for j in range(i+1,length):
                if lst[i] == lst[j]:
                        count = count+1
        if lst[i] not in lst[:i]:
                print(f"frequency of {lst[i]} is {count}")                
                                       
        

 

