def power(x,n):
    result=1
    for  _ in range(n):
        result*=x
    return result
    
x=int(input("enter the base(x):"))
n=int(input("enter the exponent :"))

result=power(x,n)
print(x,"raised to the power ",n,"is :",result)