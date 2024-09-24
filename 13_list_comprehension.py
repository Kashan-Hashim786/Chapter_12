list1 = [1,2,3,4,5,6,7]
'''    
squaredList = []
for item in list1:
    squaredList.append(item * item)
'''
squaredList = [i * i for i in list1 if i*i > 10]

print(squaredList)