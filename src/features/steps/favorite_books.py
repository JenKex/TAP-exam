import behave
import re
from playwright.sync_api import Page, expect
from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError

@given(u"we have a list associated with the user")
def step_impl(context):
    context.page.goto(context.url, timeout=5000)
    context.favorite_book_button = context.page.get_by_role("button", name = "Mina böcker")
    expect(context.favorite_book_button).to_be_visible(timeout=300)

@when(u"the user presses the 'favorite' button on a book in the database")
def step_impl(context):
    context.first_book = context.page.get_by_text(", Guido van Rossum")
    context.heart = context.page.get_by_test_id("star-Ormar på ett plan: En Python-berättelse")
    context.first_book.hover(timeout=1000)
    context.heart.wait_for(state = "visible", timeout=3000)
    # doubling up on timeout redundancy due to the little pulsing heart animation on hover
    context.heart.hover(timeout=1000)
    context.heart.click(timeout=1000)

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