try:
    num = float(input("Enter a number : "))
    print(num)

except ValueError as v:
    print(v)
    print("ValueError")
except TypeError as te:
    print(te)

'''except Exception as e:
    print(e)'''
print("............")