l = [3,4,5,6]
'''
index = 0

for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1
    '''

# This can be simplified by enumerate function
for index,item in enumerate(l):
    print(f"The item number at index {index} is {item}")