
#swap using thried variable
def swap_numbers(a,b):
    print("befor swaping :")
    print("a=",a)
    print ("b= ",b)
    temp=a
    a=b
    b=temp
    print("after swapping :")
    print("a=",a)
    print ("b= ",b)

num1=int(input("enter value of a :")) 
num2=int(input("enter value of b :"))
swap_numbers(num1,num2) 


#without help of thried variable
print("without help of thried variable")

def swap_numberswithoutvariable(a,b):
    print("befor swaping :")
    print("a=",a)
    print ("b= ",b)
    a,b=b,a                 #code of swapping
    print("after swapping :")
    print("a=",a)
    print ("b= ",b)


 
a1=int(input("enter value of a1 :")) 
b1=int(input("enter value of b1 :"))
swap_numberswithoutvariable(a1,b1)