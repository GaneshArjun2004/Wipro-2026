num = 4
if num%2==0:
    print("even")
else:
    print("Num is odd")

PRICE = 300#int(input("purchased price:"));
if PRICE>=300:
    print("u have 10% discount")
else:
    print("discount is not applicable") 

for i in range(1,7):
    print ("range of i is", i)

j=1
while j<=5:
    print(j)
    j+=1
    if j==2:
        break

day=2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")