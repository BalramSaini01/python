#sum the series 1+1/2+------+1/n
n=int(input("enter the number of terms :"))
sum1=0

for i in range(1,n+1):
    sum1=sum1+(1/i)
    
    
print("the sum of series is :",sum1)