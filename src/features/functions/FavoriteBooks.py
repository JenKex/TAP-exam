class FavoriteBooks:
    def __init__(self):
        self.favorited_books = []

    def get_favorite_books(self):
        return self.favorited_books

    def add(self, book):
        # adds a book-object -- should this only take author and title, in which case book_id needs to be calculated from max, or take book_id too? since 'book' is all one object it seems book_id should be specified, but that could run into errors
        # does this need to import the traits of the book one by one? like,
        # favorite_book = {
        #     "author": book.author,
        #     "title": book.title,
        #     "id": book.id
        # }
        if book not in self.favorited_books:
            self.favorited_books.append(book)

    def remove(self, book):
        if book in self.favorited_books:
            self.favorited_books.remove(book)