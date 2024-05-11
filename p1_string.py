print("hello balram")

str="hello syam"
print(str[0])
print(str[-1])
print(str[0:6])
print(str[::1])
print(str[::-2])
print(str[::])


str1="My Name is Balram "
str2="i am from jaipur"
str3=("hi","this","is","balram")

print(len(str1)) #lenth()
print(str1.count("a")) #count a spicial word in string
print(str1+str2)       #add to string
print(str1.upper())    #upper()
print(str1.lower())     #lower()
print(str1.startswith("my")) #startwith()
print(str1.endswith("is"))   #cheak if string is end is or given word in function than return true || false
print(str1.find("a"))
print(str1.split())
print(str1.strip())

x=str1.index("Balram")
print(x)

y=" _".join(str3)
print(y)