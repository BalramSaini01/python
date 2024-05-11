global_var=10

def modify_global():
    global global_var
    global_var=20
    
def print_global():
    print("global variable inside fn:",global_var)
print("global variable before modification :",global_var)
modify_global();
print("global variable after modification :",global_var)
print_global()