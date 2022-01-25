Feature: S3

    Background:
        Given I am logged in as testUser
    
    @after_s3
    Scenario: Can read file
        Given there is a file in sandford-james-test-bucket/test_file
        When I try and read the file
        Then I don't get an S3 error