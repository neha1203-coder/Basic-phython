for i in range(1,11) :   #range() : range function returns a sequence of numbers, starting from 0 by defaul, and increments by 1(by default) , and stops before a specifies number.
                            # range(start?,stop,step?)   ? mark is for optional
  print(i*i)




#ques 1: prit numbers form 1 to 100
for i in range(1,101,1):
  print(i)

#ques 2: print numbers form 100 to 1
for i in range(100,0,-1):
  print(i)


#ques 3: print the multiplication table of a number n

n = int(input("enter a number: "))
for i in range(1,11):
  print(n*i)


#ques 4: print even no using for loop
for i in range(2,101,2):
  if(i<=20):
    break
  print(i)


# pass statement : pass is a null statement that does nothing. It is used as a placeholder for future code.
  for i in range(5):
    pass
  print("some useful work")
 
 
# pass can use in if statement also
  if(i<200):
    pass
  print("end of the code")


#ques 5: wap to find the sum of the first n natural number.(using for loop) 
n=int(input("enter a number: "))
sum = 0
for i in range(1,n+1):
   sum +=1
print(sum)

#ques 6: wap to find the sum of the first n natural number.(using while loop)
b = int(input("enter a number"))
sum = 0
i = 1
while(i<=b):
   sum += i
i+=1
print(sum)


#ques 7: wap to find the factorial of first n number (using for loop)
num1=int(input("enter a number"))
fact = 1
i = 1
for i in range(1,num1+1):
   fact*=i
print(fact)   






  
    
