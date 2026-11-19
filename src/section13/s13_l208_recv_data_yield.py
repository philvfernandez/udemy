from collections import deque

from src.section13.s13_l207_yielding_from_another_iterator import friends

# def greet():
#     field = yield
#     print(f"Hello {field}")
#
# g = greet()
# g.send(None) # Prime the generator
# g.send("Adam")

## Part 2 example from lecture.
friends = deque(['Rolf', 'Jose', 'Charlie', 'Jen', 'Adam'])

## This is known in Python as a coroutine.  Meaning they can take in data and be suspended.
## Additional info (The video and course may be out dated.):
# https://realpython.com/python-generators/
# https://youtu.be/MCs5OvhV9S4?si=nXhHRM1FzD6eGRP3
# https://youtu.be/Z_OAlIhXziw?si=cJLHJU_ssowHCGH2
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

greeter = greet(friend_upper())
greeter.send(None)
greeter.send("Hello")
print("Hello World Multitasking")
print("How are you?")