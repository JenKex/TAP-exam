import pytest

from src.features.functions.bookStore import BookStore
from src.features.functions.favoriteBooks import FavoriteBooks

@pytest.fixture
def book_store():
    return BookStore(FavoriteBooks())

@pytest.mark.unit
def test_get_book_list(book_store):
    books = book_store.get_books()
    assert len(books) == 3

@pytest.mark.unit
def test_add_book_to_list(book_store):
    book_store.add_book("Charles Dickens", "Great Expectations")
    books = book_store.get_books()
    assert any(book["author"] == "Charles Dickens" and book["title"] == "Great Expectations" for book in books)

@pytest.mark.unit
def test_toggle_favorite_book(book_store):
    book_store.toggle_favorite(101)
    favorited_books = book_store.favorite_books.get_favorite_books()
    assert { "id": 101, "title": "The Pragmatic Procrastinator", "author": "Dave Thomasson" } in favorited_books