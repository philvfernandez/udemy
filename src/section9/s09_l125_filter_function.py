def starts_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf', 'John', 'Jack', 'Jill', 'Randy']
starts_with_r = filter(starts_with_r, friends) # arg 1: function that returns True/False

# we also could use a lambda
starts_with_r1 = filter(lambda x:x.startswith('R'), friends)
# using for loop is the same as using a lambda.  This runs faster than the lambda because you don't have to create a lambda.
another_starts_with_r = (f for f in friends if f.startswith('R'))

print(next(starts_with_r))
print(list(starts_with_r))
print(next(starts_with_r1))

# another method to use a customer filter.
def my_customer_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
