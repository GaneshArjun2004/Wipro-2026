# Assertions & Regex Modifiers

import re

# 1 password validation 
t1 = "Abc@1234"

p1 = re.match(
    r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}",
    t1
)

if p1:
    print("valid")
else:
    print("invalid")

# 2 re.IGNORECASE
t2 = "hello"
m1 = re.match(r"HELLO", t2, re.IGNORECASE)
print(bool(m1))

# 3 re.MULTILINE
t3 = "one\ntwo\nthree"
m2 = re.findall(r"^t\w+", t3, re.MULTILINE)
print(m2)

# 4 re.DOTALL
t4 = "hi\nhello"
m3 = re.search(r"hi.*hello", t4, re.DOTALL)
print(bool(m3))
