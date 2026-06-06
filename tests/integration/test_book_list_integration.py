import pytest

from src.features.functions.bookStore import BookStore
from src.features.functions.favoriteBooks import FavoriteBooks

@pytest.fixture
def book_store():
    return BookStore(FavoriteBooks())

@pytest.fixture
def book():
    book = {"title": "Great Expectations", "author": "Charles Dickens", "id": 103}
    return book

@pytest.mark.integration
def test_add_book_to_list_and_add_then_remove_favorite(book_store, book):
    book_store.add_book("Charles Dickens", "Great Expectations")
    books = book_store.get_books()
    assert book in books
    book_store.toggle_favorite(103)
    favorited_books = book_store.favorite_books.get_favorite_books()
    assert book in favorited_books
    book_store.toggle_favorite(103)
    favorited_books = book_store.favorite_books.get_favorite_books()
    assert book not in favorited_books