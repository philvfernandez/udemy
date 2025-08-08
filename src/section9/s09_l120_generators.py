# Generators function: Remembers the state it's in between executions.

#This is a generator function which uses yield
def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
        # nums.append(i)
        yield i
        i += 1

g = hundred_numbers()
print(next(g))
print(next(g))

print(list(g))
