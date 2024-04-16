#1.integer use
i=10
for n in range(i):
    print(n)
#range function
for n in range(2,21,2):#(start,ending,update)
    print(n)
#range function take input user       
# num1=int(input("enter value of number which you want to print table")) 
# for n in range(num1,num1*10+1,num1):
#     print(n)
    
#2.>>>>>>>>>>>>>>>>>>>>>>><<<<<<use of string in loop>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<
str="balram"
for n in str:
    print(n)
    
#3.<<<<<<<<<<<<<<<<list use in for loop>>>>>>>>>>>>>>>>>>>>>>>>
list1=["ram","syam","dev",10,15,29]
for n in list1:
    print(n)
    
#4.<<<<<<<<<<<<dictonary use in for loop>>>>>>>>>>>>>>>>>>>>>
dict1={1:"one",2:"two",3:"three"}
for n in dict1:
    print(n,":",dict1[n])
    
#5.<<<<<<<<<<<use condtion in for loop>>>>>>>>
#break 
for x in range(6):
  if x == 3: 
      break
  print(x)
else:
  print("Finally finished!")
  
  
#continue
for x in range(6):
  if x == 3: continue
  print(x)
else:
  print("Finally finished!")