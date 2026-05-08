Feature: Book List
    Given we have a book database
    When the user visits the home page
    Then that book database should be visible as a rendered list

Feature: Book Adding System

    Scenario: adding a book
        Given we have a book database
        And we have a page for adding books
        When a user clicks 'Lägg till bok'
        And types in the title of the book in the 'Titel' field
        And types in the title of the author in the 'Författare' field
        And clicks the 'Lägg till ny bok' button
        Then that book's title and author should be in the book database

Feature: Book Overview

    Scenario: viewing the list of books
        Given we have a book database
        And we have a landing page
        When the user navigates to the landing page
        Then the user should see the full list of books on the landing page

Feature: Favorite Books

    Scenario: marking a book as favorite
        Given we have a book database
        And we have a list associated with the user
        When the user presses the "favorite" button on a book in the database
        Then that book should be added to the user's favorites list

    Scenario: removing a book from favorites
        Given we have a book database
        And we have a list associated with the user
        And the user has a book marked as a favorite
        When the user presses the "favorite" button on that book
        Then that book should be removed from the user's favorites list

Feature: User Overview

    Scenario: viewing user activity
        Given we have a book database
        And we have a user database
        And each user has a list of favorite books
        When the user visits the "users" page
        Then they should see the total number of users
        And they should see the total number of favorite books across all users