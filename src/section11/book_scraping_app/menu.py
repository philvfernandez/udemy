from app import books

def print_best_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10] # sort by rating in desc order and get top 10
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price * -1)[:10] # sort by rating in desc order and get top 10
    for book in cheapest_books:
        print(book)

print('---- BEST BOOKS ----')
print_best_books()
print('---- CHEAPEST BOOKS ----')
print_cheapest_books()