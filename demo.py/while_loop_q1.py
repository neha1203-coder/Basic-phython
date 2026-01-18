#ques 1: print no 1 to 100 using while loop
n = 1
while n<=100 :
    print(n)
    n += 1

 #ques 2: print no 100 to 1 using while loop
m = 100
while m>=1 :
    print(m)
    m -= 1

 #ques 3: print the multiplication table of a number n
number = int(input("enter a no: ")) 
i = 1
while i<=10:
   table = number*i
   print(table)
   i += 1

#ques 4: print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]   
squares = []
a = 1
while a<=10:
    squares.append(a*a)
    a += 1
print(squares)

#ques 5: search for a nubmber x in this tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter a number for search: "))
i = 0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx ", i)
    i += 1




   