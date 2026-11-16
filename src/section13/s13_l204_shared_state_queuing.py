import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() # things to be printed out.
counter_queue = queue.Queue() # amounts by which to increase the counter.

def increment_manger():
    global counter
    while True:
        increment = counter_queue.get() # This waits until an item is available and the locks the queue
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'New Counter value is {counter}', '-------------'))
        counter_queue.task_done() # This unlocks the queue

Thread(target=increment_manger, daemon=True).start()

def printer_manger():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target=printer_manger, daemon=True).start()

def increment_counter():
    counter_queue.put(1)

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join() # wait for it to finish

counter_queue.join() # wait for counter_queue to be empty
job_queue.join() # wait for job_queue to be empty