def counter(n):
    while n > 0:
        yield n # function is suspended.  Then the next time it's called, it will continue from where it left off.'
        n -= 1

c = counter(10)
print(next(c))
print(next(c))