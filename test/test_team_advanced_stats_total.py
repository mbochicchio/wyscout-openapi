# coding: utf-8

"""
    Wyscout API (v4)

    [Customer resources](https://www.hudl.com/support/wyscout) | [Customer support](https://www.hudl.com/support/contact)  [Wyscout Data resources](https://footballdata.wyscout.com/resources/)  **IMPORTANT: Version switching planned for July 20th 2021.**  On July 20th 2021 we will switch v3 as the Current version. V2 will become Legacy.  Please see [Versioning](#section/Versioning) section for any related details.  # Overview  This is the product documentation for our API service, in which you can find all definitions and technical information you may need.  # Authentication  ## Overview  This page explain how to authenticate to Wyscout APIs using Basic Access Authentication.  ## Using your client software  Depending on your client software you should be provided with a mechanism for supplying an username and password: that will build the required authentication headers automatically.  For example you can specify the -u argument with curl as username:password.  ## Supplying Basic Access Authentication headers  It is possible to construct the authentication headers manually:  * Build a string of the form username:password. * Encode the string in Base64 * Supply an `Authorization` header with content `Basic` followed by the encoded string.   For example, the string `Aladdin:OpenSesame` encodes to `QWxhZGRpbjpPcGVuU2VzYW1l` in base64,   so you would use this string `Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`  ## Rate limits  To avoid services overload requests are rate limited. The Wyscout API currently enforces a limit of **12** request per second per API Key.  If the rate limit is exceeded, the API will return the following HTTP 429 response:  ```json   {     \"error\": {       \"code\": 429,       \"message\": \"Too many requests\"     }   } ```  # Data glossary and definitions  At the following link you can find our Data Glossary that describes events, metrics and concepts used across the Wyscout API, Platform and reports.  <a href=\"https://dataglossary.wyscout.com/\" target=\"_blank\">Wyscout Data Glossary</a>   ## Pitch coordinates  ![Pitch map](assets/images/WyscoutDataCoordinates.png)  The event's coordinates depends on the subject. The subject's goal to be defended is always **x=0%** and the attack is always **x=100%**. All values are % expressed as **(x,y)**.  # Versioning  Wyscout gives you the chance to choose between three different sets of API endpoints.  ## Current The latest available version. It includes the most recent endpoints and improvements.  ## Preview The beta version of our next official release. Here we start to implement future improvements and new endpoints.  ## Legacy The old version. This is still available and running, in order to let users adapt their tools to new ones.  ## Version Switch  Wyscout will constantly improve its dataset by adding new endpoints and improving the existing ones. “Preview” version is where you can find last delivered updates. When a new and improved “Current” version is released, the previous version becomes “Legacy” – which means it will not immediately cease to exist, giving you the time to adapt your systems. It will be available and running until another new version – “Current” – is released, at least six months after the previous one.  ![Version Switch](assets/images/WyscoutVersionSwitch.png)  Documentation on [apidocs.wyscout.com](apidocs.wyscout.com) will always be available also for “Legacy” version. Each version will receive support as from the following table:  ![Version Support](assets/images/WyscoutVersionSupport.png)

    The version of the OpenAPI document: 2024-05-09T09:09:27Z
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.team_advanced_stats_total import TeamAdvancedStatsTotal

class TestTeamAdvancedStatsTotal(unittest.TestCase):
    """TeamAdvancedStatsTotal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamAdvancedStatsTotal:
        """Test TeamAdvancedStatsTotal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamAdvancedStatsTotal`
        """
        model = TeamAdvancedStatsTotal()
        if include_optional:
            return TeamAdvancedStatsTotal(
                accelerations = 1.337,
                aerial_duels = 1.337,
                aerial_duels_won = 1.337,
                assists = 1.337,
                attacking_actions = 1.337,
                back_passes = 1.337,
                clean_sheets = 1.337,
                conceded_goals = 1.337,
                corners = 1.337,
                crosses = 1.337,
                dangerous_opponent_half_recoveries = 1.337,
                dangerous_own_half_losses = 1.337,
                defensive_actions = 1.337,
                defensive_duels = 1.337,
                defensive_duels_won = 1.337,
                direct_free_kicks = 1.337,
                direct_free_kicks_on_target = 1.337,
                direct_red_cards = 1.337,
                dribbles = 1.337,
                duels = 1.337,
                duels_won = 1.337,
                field_aerial_duels = 1.337,
                field_aerial_duels_won = 1.337,
                forward_passes = 1.337,
                fouls = 1.337,
                free_kicks = 1.337,
                free_kicks_on_target = 1.337,
                gk_aerial_duels = 1.337,
                gk_aerial_duels_won = 1.337,
                gk_exits = 1.337,
                gk_goal_kicks = 1.337,
                gk_goal_kicks_success = 1.337,
                gk_saves = 1.337,
                gk_successful_exits = 1.337,
                goals = 1.337,
                head_shots = 1.337,
                interceptions = 1.337,
                key_passes = 1.337,
                lateral_passes = 1.337,
                linkup_plays = 1.337,
                long_goal_kicks = 1.337,
                long_passes = 1.337,
                loose_ball_duels = 1.337,
                loose_ball_duels_won = 1.337,
                losses = 1.337,
                matches = 1.337,
                matches_tagged = 1.337,
                missed_balls = 1.337,
                new_defensive_duels_won = 1.337,
                new_duels_won = 1.337,
                new_offensive_duels_won = 1.337,
                new_successful_dribbles = 1.337,
                offensive_duels = 1.337,
                offensive_duels_won = 1.337,
                offsides = 1.337,
                opponent_half_recoveries = 1.337,
                opponent_offsides = 1.337,
                own_half_losses = 1.337,
                passes = 1.337,
                passes_to_final_third = 1.337,
                penalties = 1.337,
                ppda = 1.337,
                pressing_duels = 1.337,
                pressing_duels_won = 1.337,
                progressive_run = 1.337,
                received_pass = 1.337,
                recoveries = 1.337,
                red_cards = 1.337,
                short_goal_kicks = 1.337,
                shot_assists = 1.337,
                shot_on_target_assists = 1.337,
                shots = 1.337,
                shots_against = 1.337,
                smart_passes = 1.337,
                successful_attacking_actions = 1.337,
                successful_back_passes = 1.337,
                successful_crosses = 1.337,
                successful_defensive_action = 1.337,
                successful_dribbles = 1.337,
                successful_forward_passes = 1.337,
                successful_key_passes = 1.337,
                successful_lateral_passes = 1.337,
                successful_linkup_plays = 1.337,
                successful_long_passes = 1.337,
                successful_passes = 1.337,
                successful_passes_to_final_third = 1.337,
                successful_penalties = 1.337,
                successful_smart_passes = 1.337,
                successful_through_passes = 1.337,
                successful_vertical_passes = openapi_client.models.successful_vertical_passes.Successful vertical passes(),
                through_passes = 1.337,
                touch_in_box = 1.337,
                vertical_passes = 1.337,
                xg_shot = 1.337,
                xg_shot_against = 1.337,
                yellow_cards = 1.337
            )
        else:
            return TeamAdvancedStatsTotal(
        )
        """

    def testTeamAdvancedStatsTotal(self):
        """Test TeamAdvancedStatsTotal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
