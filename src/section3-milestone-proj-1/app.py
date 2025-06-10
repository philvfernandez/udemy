## A movie collection application

## User Stories:
## - Add new movies to my collection in order to keep track of all the movies.
## - List all the movies in my collection
## - Find a movie by using the movie title

## Implementation tasks
## - Decide where to store movies in the code.
##    - Store movies in a Python list. --> movies = []
## - Decide what data we want to store for each movie.
##    - Create a dictionary for each movie
##    - In the dictionary we'll store the movie title, director, and release year
## - Show the user a menu and let them pick an option.
##   - Get user's input
##   - Then run a loop and get their input again at the end
## - Implement each requirement in turn, each as a separate function.
##     --
## - Stop running the program when the user types 'q' in the menu.

movies = []
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie by title, 'q' to quit: "


def add_movie():
    title = input("Enter movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    print("Movie added!")

def list_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print("Title: " + movie['title'] + "\n")
    print("Director: " + movie['director'] + "\n")
    print("Year: " + movie['year'] + "\n")


def find_movie_by_title():
    search_title = input("Enter movie title: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)
        else:
            print("Movie Not Found For this Title")

def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection == "a":
            add_movie()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movie_by_title()
        else:
            print("Unknown command.  Please try again.")

        selection = input(MENU_PROMPT)

menu()




