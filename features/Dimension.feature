@dimentionFeature
Feature: Test the Dimension feature
  This test should verify the functionality of the Dimension module

  @LengthTest
    Scenario Outline: Verify the Length page works
      Given I am on the "<menuOption>" page
      When I select the Length "<fromLength>" to convert "<toLength>"
      Then The initial value should be "<iniVal>"
        And The concert value should "<resVal>"
      Examples:
        |menuOption | fromLength | toLength | iniVal | resVal      |
        | Length    | (ft)       | (mm)     | 10     | 3048        |
        | Length    | (ft)       | (µm)     | 12     | 3657600     |
        | Length    | (ft)       | (li)     | 69     | 104.5455    |
        | Length    | (cbl)      | (li)     | 21     | 19333.09473 |

    @areaTest
    Scenario Outline: Verify the Area model works
        Given I am on the "<menuOption>" page
        When I select the Area "<fromArea>" to convert "<toArea>"
        Then The initial value should be "<iniVal>"
          And The concert value should "<resVal>"
        Examples:
            |menuOption | fromArea | toArea | iniVal | resVal    |
            |Area| (ha)     | (dm²)  | 2      | 2000000   |
            |Area| (ha)     | (cm²)  | 9      | 900000000 |
            |Area| (ha)     | (in²)  | 0.5    | 7750015.5 |
            |Area| (yd²)    | (in²)  | 0.8    | 1036.8    |


    @volumeTest
    Scenario Outline: Verify the volume model works
      Given I am on the "<menuOption>" page
      When I select the volume "<fromVol>" to convert "<toVol>"
      Then The initial value should be "<iniVal>"
          And The concert value should "<resVal>"
      Examples:
        |menuOption| fromVol               | toVol     | iniVal | resVal        |
        |Volume| Gallon U.S. liquid    | (mL)      | 145    | 548884.7087   |
        |Volume| Gallon U.S. liquid    | (bl imp)  | 785    | 18.1569       |
        |Volume| Gallon U.S. liquid    | (fl s)    | 30     | 95924.06607   |
        |Volume| (yd³)                 | (fl s)    | 0.9    | 581225.09435  |
