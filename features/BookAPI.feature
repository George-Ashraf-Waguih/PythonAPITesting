# Created by macbookpro at 22/11/2024
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @smoke @library
  Scenario: Verify AddBook API functionality
    Given the book details which needs to be added to library
    When we execute the AddBook Post API method
    Then book is successfully added
    And status code of response should be 200

  @regression @sprint15 @library
  Scenario Outline: Verify AddBook API functionality
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook Post API method
    Then book is successfully added
    Examples:
      | isbn | aisle |
      | gawa | 8765  |
      | power| 7654  |

