for index in range(1,101):
    if index % 3 == 0 and index % 5 == 0:
        print("FizzBuzz")
        continue
    if index % 3 == 0:
        print("Fizz")
        continue
    if index % 5 == 0:
        print("Buzz")
        continue
    else:
        print(index)
        continue