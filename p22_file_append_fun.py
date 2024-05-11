#appent a text in existing file

f=open("file.txt","w")
f.write("how are you .")
f.close()

file=open("file.txt","a")
file.write(" balram saini")

file.close()

print("file appended sucessfully")

f1=open("file.txt","r")
print(f1.readlines())
f1.close()