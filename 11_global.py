a = 23
def fun():
    global a
    a=12
    print(a)

fun() # print 12
print(a) # print 12
