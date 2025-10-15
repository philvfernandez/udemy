import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input("Please enter your name: ") # This is a blocking operation
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start} seconds')

def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start} seconds')

start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time:', time.time() - start)

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

#These are locking operations because they wait for something to happen.
thread1.join() # Wait for thread1 to finish
thread2.join() # Wait for thread2 to finish

print(f'Two thread total time:', time.time() - start)
