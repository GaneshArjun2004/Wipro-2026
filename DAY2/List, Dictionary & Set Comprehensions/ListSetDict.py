num = [1,2,3,4,5,6,2,4]
t1 = [x **2 for x in num]
t2 = {x for x in num if x%2 == 0}
t3 = {x:x**3 for x in num}
print("list",t1)
print("set",t2)
print("dict",t3)
