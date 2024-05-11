#wap to calculate area of tringle using herons formula.

a=float(input("enter first side :"))
b=float(input("enter second side :"))
c=float(input("enter thrid side :"))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5

print("The area of tringle is :",area)