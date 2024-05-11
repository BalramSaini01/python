def gcd_recurisive(a,b):
    if b==0:
        return a
    else:
        return gcd_recurisive(b,a%b)
    
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
gcd=gcd_recurisive(num1,num2)
print("the gcd of",num1,"&",num2,"is :",gcd)