f=open("file.txt","w")
f.write("hello balram saini.")
f.close()

f=open("file.txt",'r')
print(f.read(8))
print(f.readlines())
f.close()

print("file read sucessfully !")