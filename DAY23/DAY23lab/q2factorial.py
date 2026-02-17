import math
import time
from multiprocessing import Pool, cpu_count

numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    # ------------------ Sequential Computation ------------------
    start_time = time.time()

    sequential_results = []
    for num in numbers:
        result = compute_factorial(num)
        sequential_results.append(result)
        print(f"Sequential: Factorial of {num} calculated")

    sequential_time = time.time() - start_time
    print(f"\nSequential time: {sequential_time:.2f} seconds")

    # ------------------ Multiprocessing Computation ------------------
    start_time = time.time()

    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)

    for num in numbers:
        print(f"Multiprocessing: Factorial of {num} calculated")

    parallel_time = time.time() - start_time
    print(f"\nMultiprocessing time: {parallel_time:.2f} seconds")