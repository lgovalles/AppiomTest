@MotionFeature
Feature: Test the Motion feature
  This test should verify the functionality of the Motion module

  @SpeedTest
    Scenario Outline: Verify the speed page works
      Given I am on the "<menuOption>" page
      When I select the sped "<fromSpeed>" to convert "<toSpeed>"
      Then The speed initial value should be "<iniVal>"
        And The speed concert value should be "<resVal>"
          Examples:
        |menuOption| fromSpeed | toSpeed   | iniVal  | resVal  |
        |Speed| (mph)     | (km/min)  | 21      | 0.5633  |
        |Speed| (fps)     | (cm/h)    | 36      | 3950208 |
        |Speed| (min/km)  | (m/h)     | 5       | 12000   |
        |Speed| (hpf)     | Knot      | 16      | 0.00001029 |
