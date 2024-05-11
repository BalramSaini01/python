def decimal_to_binary(decimal_num):
    binary_num=bin(decimal_num)[2:]
    return binary_num
#octal to hexadecimal
def octal_to_hexadecimal(octal_num):
    decimal_num=int(octal_num,8)
    hexadecimal_num=hex(decimal_num)[2:].upper()
    return hexadecimal_num


decimal_input=int(input("enter a decimal number :"))
binary_output=decimal_to_binary(decimal_input)
print("binary equivlent :",binary_output)


octal_input=(input("enter a octal number :"))
hexadecimal_output=octal_to_hexadecimal(octal_input)
print("hexadecimal equivlent :",hexadecimal_output)