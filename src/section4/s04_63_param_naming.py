class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

print(Movie('The Matrix', 1994).name)

matrix = Movie('The Matrix', 1994).year
print(matrix)