Feature: Book List
    Scenario: viewing the list of books
        Given we have a book database
        And we have a landing page
        When the user is on the landing page
        Then the user should see the full list of books on the landing page

    Scenario: adding a book
        Given we have a book database
        And we have a page for adding books
        When a user clicks 'Lägg till bok'
        And types in the title of the book in the 'Titel' field
        And types in the name of the author in the 'Författare' field
        And clicks the 'Lägg till ny bok' button
        Then that book's title and author should be in the book database

# Feature: Favorite Books

    Scenario: marking a book as favorite
        Given we have a book database
        And we have a list associated with the user
        When the user presses the 'favorite' button on a book in the database
        Then that book should be added to the user's favorites list
        And the 'statistics' view should show 1 book marked as favorite

    Scenario: removing a book from favorites
        Given we have a book database
        And we have a list associated with the user
        And the user has a book marked as a favorite
        When the user presses the 'favorite' button on that book
        Then that book should be removed from the user's favorites list

# Feature: User Overview

    Scenario: viewing user activity
        Given each user has a list of favorite books
        When the user visits the 'statistics' page
        Then they should see the total number of users
        And they should see the total number of favorite books across all users