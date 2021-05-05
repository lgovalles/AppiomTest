@dimentionFeature
Feature: Test the Dimension feature
  This test should verify the functionality of the Dimension module

  @LengthTest
    Scenario Outline: Verify the Length page works
      Given I am on the Length page
      When I select the Length "<fromLength>" to convert "<toLength>"
      Then The initial value should be "<iniVal>"
        And The concert value should "<resVal>"
      Examples:
        | fromLength | toLength | iniVal | resVal   |
        | (ft)       | (mm)     | 10     | 3048     |
        | (ft)       | (µm)     | 12     | 3657600  |


    @areaTest
    Scenario Outline: Verify the Area model works
        Given I am on the Area page
        When I select the Area "<fromArea>" to convert "<toArea>"
        Then The initial value should be "<iniVal>"
          And The concert value should "<resVal>"
        Examples:
            | fromArea | toArea | iniVal | resVal    |
            | (ha)     | (dm²)  | 2      | 2000000   |
            | (ha)     | (cm²)  | 9      | 900000000 |

    @volumeTest
    Scenario Outline: Verify the volume model works
      Given I am on the volume page
      When I select the volume "<fromVol>" to convert "<toVol>"
      Then The initial value should be "<iniVal>"
          And The concert value should "<resVal>"
      Examples:
        | fromVol               | toVol     | iniVal | resVal      |
        | Gallon U.S. liquid    | (mL)      | 145    | 548884.7087 |
        | Gallon U.S. liquid    | (bl imp)  | 785    | 18.1569     |