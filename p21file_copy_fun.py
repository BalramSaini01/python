f=open("file.txt","w")
f.write("i am mca student.")
f.close()


try:
    with open("file.txt")as f2:
        with open("file.txt","w")as f3:
            for i in f2:
                f3.write(i)
    print("file has been copied.")
except:
    print("file is not aviable.")
    
else:
    f2.close()
    print("file closed")