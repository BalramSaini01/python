import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("file deleted sucessfully")
    
else:
    print("file notr aviable.")
    