import re
email="admin@gmail.com"
if re.match(r"[a-zA-Z]+@",email):
    print("Valid Start")

result2=re.fullmatch(r"\d{10}","1234567898")
print(result2)


print(re.findall(r"\d+","price 50 and 100 and 200"))

for n in re.finditer(r"\d+","A1 b1000, B33, C444"):
    print(n.group(),n.start(),n.end())

for n in re.finditer(r"[a-z]","a1 b1000, B33, C444"):
    print(n.group(),n.start(),n.end())
for n in re.finditer(r"[A-Z]","a1 b1000, B33, C444"):
    print(n.group(),n.start(),n.end())

print(re.search(r"\d+","Age is 25"))

print(re.search(r"^a.*c$","abnkkkkkknnc"))

m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())
 
print(re.search('pyThOn','PyTHon',re.I))

new1 = 'tortoise\ntwo\nthree'
print (re.findall(r"^t\w+",new1,re.M))