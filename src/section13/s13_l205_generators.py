# Works like multi-threading but without using threads.

def counter(n):
    while n > 0:
        yield n # function is suspended.  Then the next time it's called, it will continue from where it left off.'
        n -= 1

c1 = counter(10)
c2 = counter(20)

print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))