# TODO: tests for marking books as favorites

import pytest

from src.features.functions.favoriteBooks import FavoriteBooks

@pytest.fixture
def favorite_books():
    return FavoriteBooks()

@pytest.fixture
def book():
    book = { "title": "How I Learned To Stop Worrying And Love The Bots", "author": "Warren Peace", "id": 104 }
    return book

@pytest.mark.unit
def test_add_book_to_favorites(favorite_books, book):
    favorite_books.add(book)
    list_of_favorite_books = favorite_books.get_favorite_books()
    assert book in list_of_favorite_books

@pytest.mark.unit
def test_remove_book_from_favorites(favorite_books, book):
    favorite_books.remove(book)
    list_of_favorite_books = favorite_books.get_favorite_books()
    assert book not in list_of_favorite_books