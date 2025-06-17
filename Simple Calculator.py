try:
    a = int(input("Enter 1st integer: "))
    b = int(input("Enter 2nd integer: "))
except ValueError:
    print("Bro. That's not an integer.")
    exit()
print("Enter + for addition, - for subtraction, * for multiplication, / for division, and ^ for exponents")
ch=input("Enter choice of operator")
if ch == '+':
    print("Result",a+b)
elif ch == '-':
    print("Result",a-b)
elif ch == '*':
    print("Result",a*b)
elif ch == '/':
    if b == 0:
        print("Division by zero, it is error")
    else:
        print("Result",a/b)
elif ch == '^':
    if a == 0 and b == 0:
        print("0 raised to 0 is... mathematically cursed.")
    else:
        print("Result",a**b)
else:
    print("I am not paid enough to do that")
