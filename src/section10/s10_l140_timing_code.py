import time
import timeit


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(f"It took {end - start} seconds to run.")

def powers(limit):
    return [x**2 for x in range(limit)]

# print(powers(5))

# start = time.time()
#powers(5000000)
#end = time.time()
#print(f"It took {end - start} seconds to run.")

measure_runtime(lambda: powers(5000000))

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
