try:
    num = float(input("Enter a number : "))
    print(num)

except ValueError as v:
    print(v)
    print("ValueError")
except TypeError as te:
    print(te)

else:  # it will run when the try block exceutes successfully
 print("try block exceuted successfully")
'''except Exception as e:
    print(e)'''


print("............")