Feature: Login


    Scenario: Log in successfully
        Given the user exists in the system
        When the Login post method is executed
        Then the user should login successfully


    Scenario: Try login without password
        Given I try login without password
        When the Login post method is executed
        Then I should get the "Missing password" error


    Scenario: Try login without email
        Given I try login without email
        When the Login post method is executed
        Then I should get the "Missing email or username" error


    Scenario: Try login with non-exists user
        Given the user non-exists in the system
        When the Register post method is executed
        Then I should get the "user not found" error
