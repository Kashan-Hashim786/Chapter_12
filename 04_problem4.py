try:
    a  = int(input("Enter a number : "))
    b = int(input("Enter a second number : "))

    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")
