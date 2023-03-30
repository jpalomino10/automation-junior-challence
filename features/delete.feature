Feature: Delete User


    Scenario: Delete user successfully
        Given I want delete a user by id
        When the Users DELETE method is executed
        Then the user should be deleted


