
from collections import deque
from types import coroutine

friends = deque(['Rolf', 'Jose', 'Charlie', 'Jen', 'Adam'])

## This is known in Python as a coroutine.  Meaning they can take in data and be suspended.
@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

async def greet(g):
    print("Starting...")
    await g
    print("Ending...")

greeter = greet(friend_upper())
greeter.send(None)
print("Hello World Multitasking")

while True:
    try:
        greeter.send("Hello")
        greeting = input('Enter a greeting: ')
        greeter.send(greeting)

        greeting = input('Enter a greeting: ')
        greeter.send(greeting)

        greeting = input('Enter a greeting: ')
        greeter.send(greeting)

        greeting = input('Enter a greeting: ')
        greeter.send(greeting)
    except StopIteration: # Signal completion.  Similar to reaching the end of a Java Iterator.
        break
