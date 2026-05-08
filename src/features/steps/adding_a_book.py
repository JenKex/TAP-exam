import behave
from playwright.sync_api import Page, expect

url = "https://tap-ht25-testverktyg.github.io/exam/"

# @given("we have a book database")
# def step_impl(context):
#     pass

# @given("we have a page for adding books")
# def step_impl(context):
#     context.browser.get(url)

@when("a user clicks 'Lägg till bok")
    # simulate click

@when("types in the title of the book in the 'Titel' field")

@when("types in the name of the author in the 'Författare' field")

@when("clicks the 'Lägg till ny bok' button")

@then("that book's title and author should be in the book database")

# Scenario: adding a book
#     Given we have a book database
#     And we have a page for adding books
#     When a user clicks 'Lägg till bok'
#     And types in the title of the book in the 'Titel' field
#     And types in the title of the author in the 'Författare' field
#     And clicks the 'Lägg till ny bok' button
#     Then that book's title and author should be in the book database

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
#         When the user visits the "users" page
#         Then they should see the total number of users
#         And they should see the total number of favorites across all users