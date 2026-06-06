import behave
import re
from playwright.sync_api import Page, expect
from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError

@given(u"we have a book database")
def step_impl(context):
    pass

@given(u'we have a landing page')
def step_impl(context):
    context.page.goto(context.url, timeout=5000)

@when(u'the user is on the landing page')
def step_impl(context):
    locator = context.page.get_by_role("h2", name = "Välkommen!")

@then(u'the user should see the full list of books on the landing page')
def step_impl(context):
    # This should probably test against the expectation of length of full unedited list of books, but that could get messed with across multiple tests.
    all_books = context.page.locator('.book')
    expect(all_books).to_be_visible

@given(u"we have a page for adding books")
def step_impl(context):
    context.page.goto(context.url, timeout=5000)
    # trying to get by data-testid, but may use page.get_by_role("button", name = "Lägg till bok") if it doesn't work
    # name -- "Lägg till bok" works when testid doesn't, but I'd prefer testId. Troubleshoot it.
    context.add_book_button = context.page.get_by_role("button", name = "Lägg till bok")
    # locator = context.page.get_by_role('button')
    # context.add_book_button = locator.get_by_test_id('add-book')
    expect(context.add_book_button).to_be_visible(timeout=300)

@when(u"a user clicks 'Lägg till bok'")
def step_impl(context):
    # may need a timeout here
    context.add_book_button.click(timeout=500)

@when(u"types in the title of the book in the 'Titel' field")
def step_impl(context):
    title_input = context.page.locator('#add-input-title')
    title_input.fill('Tyrannosaurus Regex', timeout=300)

@when(u"types in the name of the author in the 'Författare' field")
def step_impl(context):
    author_input = context.page.locator('#add-input-author')
    author_input.fill('Mannie Patterns', timeout=300)

@when(u"clicks the 'Lägg till ny bok' button")
def step_impl(context):
    context.page.get_by_role('button', name="Lägg till ny bok").click(timeout=300)


@then(u"that book's title and author should be in the book database")
def step_impl(context):
    context.page.get_by_role('button', name="Katalog").click(timeout=300)
    all_books = context.page.locator('.book')
    new_book = all_books.get_by_text(re.compile('"Tyrannosaurus Regex", Mannie Patterns'))
    expect(new_book).to_be_visible()


# Scenario: adding a book
#     Given we have a book database
#     And we have a page for adding books
#     When a user clicks 'Lägg till bok'
#     And types in the title of the book in the 'Titel' field
#     And types in the title of the author in the 'Författare' field
#     And clicks the 'Lägg till ny bok' button
#     Then that book's title and author should be in the book database

# @given(u"we have a book database")
# def step_impl(context):
#     pass

@given(u"we have a list associated with the user")
def step_impl(context):
    context.page.goto(context.url, timeout=5000)
    context.favorite_book_button = context.page.get_by_role("button", name = "Mina böcker")
    expect(context.favorite_book_button).to_be_visible(timeout=300)

@when(u"the user presses the 'favorite' button on a book in the database")
def step_impl(context):
    context.first_book = context.page.get_by_text(", Guido van Rossum")
    context.first_book.hover(timeout=1000)
    context.page.get_by_test_id("star-Ormar på ett plan: En Python-berättelse").click(timeout=500)

@then(u"that book should be added to the user's favorites list")
def step_impl(context):
    context.page.get_by_role("button", name = "Mina böcker").click(timeout=300)
    favorited_book = context.page.get_by_test_id("fav-Ormar på ett plan: En Python-berättelse")
    expect(favorited_book).to_be_visible()

@then(u"the 'statistics' view should show 1 book marked as favorite")
def step_impl(context):
    context.page.get_by_role("button", name = "Statistik").click(timeout=500)
    favorites_count = context.page.get_by_test_id("stars-count")
    expect(favorites_count).to_contain_text('1')

@given(u"the user has a book marked as a favorite")
def step_impl(context):
    context.page.goto(context.url, timeout=5000)
    context.first_book = context.page.get_by_text(", Guido van Rossum")
    context.first_book.hover(timeout=1000)
    context.page.get_by_test_id("star-Ormar på ett plan: En Python-berättelse").click(timeout=300)
    context.page.get_by_role("button", name = "Mina böcker").click(timeout=300)
    favorited_book = context.page.get_by_test_id("fav-Ormar på ett plan: En Python-berättelse")
    expect(favorited_book).to_be_visible()

@when(u"the user presses the 'favorite' button on that book")
def step_impl(context):
    context.page.get_by_role("button", name = "Katalog").click(timeout=300)
    favorite_icon = context.page.get_by_test_id("star-Ormar på ett plan: En Python-berättelse")
    favorite_icon.click(timeout=300)

@then(u"that book should be removed from the user's favorites list")
def step_impl(context):
    context.page.get_by_role("button", name = "Mina böcker").click(timeout=300)
    placeholder_text = context.page.get_by_text("När du valt, kommer dina favoritböcker att visas här.")
    expect(placeholder_text).to_be_visible()

@given(u"each user has a list of favorite books")
def step_impl(context):
    context.page.goto(context.url, timeout=5000)
    context.favorite_books_button = context.page.get_by_role("button", name = "Mina böcker")
    expect(context.favorite_books_button).to_be_visible()

@when(u"the user visits the 'statistics' page")
def step_impl(context):
    statistics_button = context.page.get_by_role("button", name = "Statistik")
    statistics_button.click(timeout=300)

@then(u"they should see the total number of users")
def step_impl(context):
    book_count = context.page.get_by_test_id("book-count")
    expect(book_count).to_be_visible()

@then(u"they should see the total number of favorite books across all users")
def step_impl(context):
    favorites_count = context.page.get_by_test_id("stars-count")
    expect(favorites_count).to_be_visible()

# Feature: Favorite Books

#     Scenario: marking a book as favorite
#         Given we have a book database
#         And we have a list associated with the user
#         When the user presses the "favorite" button on a book in the database
#         Then that book should be added to the user's favorites list

#     Scenario: removing a book from favorites
#         Given we have a book database
#         And we have a list associated with the user
#         And the user has a book marked as a favorite
#         When the user presses the "favorite" button on that book
#         Then that book should be removed from the user's favorites list

# Feature: User Overview

#     Scenario: viewing user activity
#         Given we have a book database
#         And we have a user database
#         And each user has a list of favorite books
#         When the user visits the "statistics" page
#         Then they should see the total number of books
#         And they should see the total number of favorites across all users