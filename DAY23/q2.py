import math
import time
from multiprocessing import Pool, cpu_count

numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    # Sequential execution
    starttime1 = time.time()
    seq_results = []

    for num in numbers:
        compute_factorial(num)
        seq_results.append(num)
        print(f"Sequential: Factorial of {num} calculated")

    seqtime = time.time() - starttime1
    print(f"\nSequential time: {seqtime:.2f} seconds")

    # Parallel execution
    starttime2 = time.time()

    with Pool(cpu_count()) as pool:
        pool.map(compute_factorial, numbers)

    for num in numbers:
        print(f"Multiprocessing: Factorial of {num} calculated")

    paralleltime = time.time() - starttime2
    print(f"\nParallel time: {paralleltime:.2f} seconds")