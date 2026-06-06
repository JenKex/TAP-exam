from .favoriteBooks import FavoriteBooks

class BookStore:

    # Initializes the FavoriteBooks class to be able to insert books onto the list of favorites and use those functions 

    def __init__(self, favorite_books: FavoriteBooks):
        self.favorite_books = favorite_books
        self.books = [	{ "id": 100, "title": "Ormar på ett plan: En Python-berättelse", "author": "Guido van Rossum" },
	{ "id": 101, "title": "The Pragmatic Procrastinator", "author": "Dave Thomasson" },
	{ "id": 102, "title": "Python för folk som hatar ormar", "author": "Monty Pythonsson" },]

    def get_books(self):
        return self.books

    # Makes a new maximum book_id, then adds book to the list of books
    def add_book(self, author, title):
        new_book_id = max(book["id"] for book in self.books) + 1
        self.books.append({"id": new_book_id, "author": author, "title": title})

    # Looks for the book with the given ID, then 
    def toggle_favorite(self, book_id):
        new_favorite_book = None
        for book in self.books:
            if book["id"] == book_id:
                new_favorite_book = book
                break
        if new_favorite_book is None:
            raise ValueError(f"No book with ID {book_id}")
        if new_favorite_book in self.favorite_books.favorited_books:
            self.favorite_books.remove(new_favorite_book)
        else:
            self.favorite_books.add(new_favorite_book)