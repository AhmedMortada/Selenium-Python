Feature: Google Login
    As a user
    I want to access Google
    So that I can use its services

    Scenario: Demo Shop login
        Given the user is on the Shop Page
        When the user clicks the login button
        When the user enters the username
        When the user enters the password
        When the user clicks the login button
        Then the user is logged in

        
        
       
