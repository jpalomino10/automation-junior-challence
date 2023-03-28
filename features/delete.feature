Feature: Delete User


    Scenario: Search user successfully
        Given I want search a user by id
        When the Users GET method is executed
        Then the user should be founded


    Scenario:  Search user unsuccessfully
        Given I want search a non-exists user by id
        When the Users GET method is executed
        Then I shouldn't get any result