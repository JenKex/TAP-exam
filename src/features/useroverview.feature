Feature: User Overview

    Scenario: viewing user activity
        Given each user has a list of favorite books
        When the user visits the 'statistics' page
        Then they should see the total number of users
        And they should see the total number of favorite books across all users