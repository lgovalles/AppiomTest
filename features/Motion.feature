@MotionFeature
Feature: Test the Motion feature
  This test should verify the functionality of the Motion module

  @SpeedTest
    Scenario Outline: Verify the speed page works
      Given I am on the speed page
      When I select the sped "<fromSpeed>" to convert "<toSpeed>"
      Then The speed initial value should be "<iniVal>"
        And The speed concert value should be "<resVal>"
          Examples:
        | fromSpeed | toSpeed   | iniVal  | resVal |
        | (mph)     | (km/min)  | 21      | 0.5633 |