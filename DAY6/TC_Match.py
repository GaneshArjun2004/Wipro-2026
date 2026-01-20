import re
t1 = "java full stack course advanced"
t2 =re.match('java',t1)
if t2:
    print('matching')
else:
    print('no match')    


result = re.search('course',t1)
if result:
    print(result.group())
    print(result.start())
    print(result.end())

else:
    print('false output')    

