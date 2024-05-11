def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


num=int(input("enter a number :"))
if(num<0):
    print("gactorial is not defiend for negative number :",num)
elif(num==0):
    print("the factorial of 0 is 1")
else:
    print("the factorial of",num,"is :",factorial(num))
    