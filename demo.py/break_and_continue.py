#break : used to terminate the loop when encountered
#continue : terminates execution in the current iteration and continues execution of the loop with the next iteration.
nums = (23,54,75,93,29,43)
a = int(input("enter a no to search: "))
i = 0
while i<len(nums) :
    if(nums==nums[i]) :
        print("no found at idx :",i)
        break
    else :
        print("number not found")
        break
    i += 1 



#ex : 2
i = 0
while i<=10:    
    if(i>=6) :
        break
    print(i)
    i += 1  


n = 0
while n<=10:
    if(n==6) :
        n+=1
        continue #skip which means it skip 6 to print
    print(n)   
    n += 1

m = 0
while m<=20:
    if(m%2==0):
        m+=1
        continue  # it skip even no to print 
    print(m)       # it only print odd numbers
    m += 1