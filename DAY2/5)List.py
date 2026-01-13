names = ["arjun","ganesh","kwak","sohith"]
numbers = [1,2,3.4,5]
mixed = [1.2,3,"sumesh",True]

numbers[1]=100
print(names)
print(numbers)
print(mixed)

for i in numbers:
    print(i)
if 10 in numbers:
    print("Found")
else:
    print("not found")


matrix = [[1,2,3],[4,5,6]] #row0,row1
print(matrix[1][2]) #prints from row 1 column 2

#names
names.reverse()
print(names)
names.append("suresh")
print(names)
names.extend(["kartik","aryan"])
print(names)
names.pop(1)
print(names)
names.insert(3,"theworld")
print(names)