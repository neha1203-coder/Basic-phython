for i in range(1,11) :   #range() : range function returns a sequence of numbers, starting from 0 by defaul, and increments by 1(by default) , and stops before a specifies number.
                            # range(start?,stop,step?)   ? mark is for optional
  print(i*i)




#ques 1: prit numbers form 1 to 100
for i in range(1,100,1):
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




  
    
