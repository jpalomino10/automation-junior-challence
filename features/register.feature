Feature: Register


    Scenario: Register user successfully
        Given we want register a new user
        When the Register post method is executed
        Then the user should be created


# Scenario: Register user unsuccessfully
#     Given we try register a user without email
#     When the Register post method is executed
#     Then I should get an error message
