import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import pool


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start} seconds')

def complex_calculation():
    print('Started calculating...')
    start = time.time()
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start} seconds')


# With a single thread, we can do one at a time--e.g
start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time:', time.time() - start)

# Processes

start = time.time()
with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)

print(f'Two process total time:', time.time() - start)