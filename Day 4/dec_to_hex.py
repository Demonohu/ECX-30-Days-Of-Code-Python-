#Decimal to Hexadecimal
#Without using the inbuilt hex() function, write a function
#that takes an integer as input and prints out it's 
#conversion to Hexadecimal as output.


decimal = int(input("Enter an integer: "))


def dec_to_hex(num):
    """
    
    """
    ans = []
    codes = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'H'}
    while num > 0:
        if (num % 16) < 10:
            hex = str(num % 16)
        else:
            hex = codes[num % 16]
        ans.append(hex)
        num = num//16

    hex = (''.join(list(reversed(ans))))
    return hex


print(dec_to_hex(decimal))