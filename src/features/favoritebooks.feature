Feature: Favorite Books

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