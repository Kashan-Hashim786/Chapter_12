a = int(input("Enter a number : "))
b = int(input("Enter a second number : "))

if b==0:
    raise ZeroDivisionError("Can not be divide by Zero")
else:
    print(f"The division a/b is {a/b}")
