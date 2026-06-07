import behave
import re
from playwright.sync_api import Page, expect
from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError

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