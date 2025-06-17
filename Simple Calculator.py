a=int(input("Enter 1st integer"))
b=int(input("ENter 2nd integer"))
print("Enter + for addition, - for subtraction, * for multiplication, / for division, and ^ for exponents")
ch=input("Enter choice of operator")
if ch == '+':
    print(a+b)
elif ch == '-':
    print(a-b)
elif ch == '*':
    print(a*b)
elif ch == '/':
    if b == 0:
        print("Division by zero, it is error")
    else:
        print(a/b)
elif ch == '^':
    if a == 0:
        print("Invalid")
    else:
        print(a**b)
else:
    print("I am not paid enough to do that")
