#RegEx

import re

# 1 re.match
t1 = "EMP123"
m = re.match(r"(EMP)(\d{3})", t1)

if m:
    print(m.group(0), m.group(1), m.group(2))
else:
    print("invalid")

# 2 re.search
t2 = "mail id is test_99@gmail.com"
ext = re.search(r"([\w\.]+)@([\w]+)\.(\w+)", t2)

if ext:
    print(ext.group(0), ext.group(1), ext.group(2), ext.group(3))

# 3 Meta-characters & special sequences
t3 = "user1 5 files."
p = re.search(r"(\w+)\s(\d+)\s(\w+)\.", t3)

if p:
    print(p.group(1), p.group(2), p.group(3))
