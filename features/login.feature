Feature: Google Login
    As a user
    I want to access Google
    So that I can use its services

    Scenario: Accept cookies and search on Google homepage
        Given the user is on the login page
        When the user accepts cookies
        When the user searches for "Selenium WebDriver"
        # Then the user able to search
        
        
       
