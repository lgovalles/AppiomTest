@dimentionFeature
Feature: Test the Dimension feature
  This test should verify the functionality of Dimension module

  @LengthTest
    Scenario Outline: Verify the Length page works
      Given I am on the Length page
      When I select the Length "<fromLength>" to convert "<toLength>"
      Then The initial value should be "<iniVal>"
        And The concert value should "<resVal>"
      Examples:
        | fromLength   | toLength    | iniVal | resVal |
        | ft           | mm          | 1      | 304.8  |
        | ft           | um          | 1      | 304800 |


    @areaTest
    Scenario Outline: Verify the Area model works
        Given I am on the Area page
        When I select the Area "<fromArea>" to convert "<toArea>"
        Then The initial value should be "<iniVal>"
          And The concert value should "<resVal>"
        Examples:
            | fromArea | toArea | iniVal | resVal     |
            | ha       | dm2    | 1      | 1000000    |
            | ha       | cm2    | 1      | 100000000 |

    @volumeTest
    Scenario Outline: Verify the volume model works
      Given I am on the volume page
      When I select the volume "<fromVol>" to convert "<toVol>"
      Then The initial value should be "<iniVal>"
          And The concert value should "<resVal>"
      Examples:
        | fromVol      | toVol       | iniVal | resVal    |
        | gal          | mL          | 1      | 3785.4118 |
        | gal          | bl imp      | 1      | 0.02313   |