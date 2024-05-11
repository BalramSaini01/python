def fibonacci_recursive(n):
    if n<=1:
        return n
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

terms=int(input("enter the number :"))
if terms<=0:
    print("please enter postive number.")
else:
    print("fibonacci series:")
    for i in range(terms):
        print(fibonacci_recursive(i),end=" ")