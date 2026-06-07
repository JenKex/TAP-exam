class FavoriteBooks:
    def __init__(self):
        self.favorited_books = []

    def get_favorite_books(self):
        return self.favorited_books

    # takes objects, including hardcoded book_id, to add or remove to the favorite books list directly

    def add(self, book):
        if book not in self.favorited_books:
            self.favorited_books.append(book)

    def remove(self, book):
        if book in self.favorited_books:
            self.favorited_books.remove(book)