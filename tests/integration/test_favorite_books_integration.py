import pytest

from src.features.functions.favoriteBooks import FavoriteBooks

@pytest.fixture
def favorite_books():
    return FavoriteBooks()

@pytest.fixture
def book():
    book = { "title": "How I Learned To Stop Worrying And Love The Bots", "author": "Warren Peace", "id": 104 }
    return book

@pytest.mark.integration
def test_add_and_remove_favorite(favorite_books, book):
    favorite_books.add(book)
    books = favorite_books.get_favorite_books()
    assert book in books
    favorite_books.remove(book)
    assert book not in books