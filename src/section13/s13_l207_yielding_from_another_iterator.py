from collections import deque

friends = deque(['Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'])

def get_friend():
    yield from friends

c = get_friend()
print(next(c))
print(next(c))