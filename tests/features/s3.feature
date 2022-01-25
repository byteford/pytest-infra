Feature: S3

    Background:
        Given I am logged in
    
    @after_s3
    Scenario: Can read file
        Given there is a file in bucket_location
        When I try and read the file
        Then I don't get an S3 error