#q1. 1. Create a custom iterator class that iterates over numbers from 1 to N
class NumberIterator:
    def __init__(self, N):
        self.N = N
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.N:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

print("Iterator :")
for num in NumberIterator(5):
    print(num)

def fibonacci_generator(N):
    a, b = 0, 1
    count = 0
    while count < N:
        yield a
        a, b = b, a + b
        count += 1

#q2 2. Create a generator function that yields the first N Fibonacci numbers

print("generator:")
for num in fibonacci_generator(7):
    print(num)



#q3 3. Demonstrate the difference between using the iterator and generator by printing values using a for loop
# Using Iterator

for num in NumberIterator(5):
    print("iterator:",num)

for num in fibonacci_generator(7):
    print("genrator:",num)
