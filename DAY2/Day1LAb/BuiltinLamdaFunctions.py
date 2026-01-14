from functools import reduce

numbers = range(1, 21)
evennumbers = list(filter(lambda x: x % 2 == 0, numbers))
squarednumbers = list(map(lambda x: x ** 2, evennumbers))
sum_of_squares = reduce(lambda a, b: a + b, squarednumbers)

print("Squared Even Numbers with Index:")
for index, value in enumerate(squarednumbers, start=1):
    print(index,value)

print("\nSum of Squared Even Numbers:", sum_of_squares)
