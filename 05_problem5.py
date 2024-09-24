tableNum = int(input("Enter a table number : "))
list1 = [1,2,3,4,5,6,7,8,9,10]
tableList = [tableNum * i for i in list1]
print(tableList)
with open("table.txt","a") as f:
    f.write(str(tableList))
    
