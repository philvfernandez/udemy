def greet():
    print("Hello")

# Example of a Higher order function takes in a function as an argument and runs it within the body of the function.
def before_and_after(func):
    print("Before")
    func()
    print("After")

before_and_after(lambda: 5)
before_and_after(greet)


movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "The Sound of Music", "director": "Harrison"},
    {"name": "The Godfather", "director": "Marlboro"}
]

def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)

    return found

find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movie = find_movie(looking_for, lambda movie: movie[find_by])
print(movie or 'No Movies Found')