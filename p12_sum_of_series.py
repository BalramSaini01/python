#sum the series 1^2+1/2^2+-----+1/n^2

def sum_series(n):
    result=0;
    for i in range(1,1+n):
        result=result + 1/(i**2)
        return result
  
        n=int(input("enter the value of n :"))
        if n<0:
            print("please enter a positive number")
            return 
        
        series_sum=sum_series(n)
        print("sum of the series is :",series_sum)
        
       
        if  __name__ == "_main_":
           main()