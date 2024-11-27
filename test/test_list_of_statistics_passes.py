# coding: utf-8

"""
    Wyscout API (v4)

    [Customer resources](https://www.hudl.com/support/wyscout) | [Customer support](https://www.hudl.com/support/contact)  [Wyscout Data resources](https://footballdata.wyscout.com/resources/)  **IMPORTANT: Version switching planned for July 20th 2021.**  On July 20th 2021 we will switch v3 as the Current version. V2 will become Legacy.  Please see [Versioning](#section/Versioning) section for any related details.  # Overview  This is the product documentation for our API service, in which you can find all definitions and technical information you may need.  # Authentication  ## Overview  This page explain how to authenticate to Wyscout APIs using Basic Access Authentication.  ## Using your client software  Depending on your client software you should be provided with a mechanism for supplying an username and password: that will build the required authentication headers automatically.  For example you can specify the -u argument with curl as username:password.  ## Supplying Basic Access Authentication headers  It is possible to construct the authentication headers manually:  * Build a string of the form username:password. * Encode the string in Base64 * Supply an `Authorization` header with content `Basic` followed by the encoded string.   For example, the string `Aladdin:OpenSesame` encodes to `QWxhZGRpbjpPcGVuU2VzYW1l` in base64,   so you would use this string `Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`  ## Rate limits  To avoid services overload requests are rate limited. The Wyscout API currently enforces a limit of **12** request per second per API Key.  If the rate limit is exceeded, the API will return the following HTTP 429 response:  ```json   {     \"error\": {       \"code\": 429,       \"message\": \"Too many requests\"     }   } ```  # Data glossary and definitions  At the following link you can find our Data Glossary that describes events, metrics and concepts used across the Wyscout API, Platform and reports.  <a href=\"https://dataglossary.wyscout.com/\" target=\"_blank\">Wyscout Data Glossary</a>   ## Pitch coordinates  ![Pitch map](assets/images/WyscoutDataCoordinates.png)  The event's coordinates depends on the subject. The subject's goal to be defended is always **x=0%** and the attack is always **x=100%**. All values are % expressed as **(x,y)**.  # Versioning  Wyscout gives you the chance to choose between three different sets of API endpoints.  ## Current The latest available version. It includes the most recent endpoints and improvements.  ## Preview The beta version of our next official release. Here we start to implement future improvements and new endpoints.  ## Legacy The old version. This is still available and running, in order to let users adapt their tools to new ones.  ## Version Switch  Wyscout will constantly improve its dataset by adding new endpoints and improving the existing ones. “Preview” version is where you can find last delivered updates. When a new and improved “Current” version is released, the previous version becomes “Legacy” – which means it will not immediately cease to exist, giving you the time to adapt your systems. It will be available and running until another new version – “Current” – is released, at least six months after the previous one.  ![Version Switch](assets/images/WyscoutVersionSwitch.png)  Documentation on [apidocs.wyscout.com](apidocs.wyscout.com) will always be available also for “Legacy” version. Each version will receive support as from the following table:  ![Version Support](assets/images/WyscoutVersionSupport.png)

    The version of the OpenAPI document: 2024-05-09T09:09:27Z
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.list_of_statistics_passes import ListOfStatisticsPasses

class TestListOfStatisticsPasses(unittest.TestCase):
    """ListOfStatisticsPasses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListOfStatisticsPasses:
        """Test ListOfStatisticsPasses
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListOfStatisticsPasses`
        """
        model = ListOfStatisticsPasses()
        if include_optional:
            return ListOfStatisticsPasses(
                team_id = openapi_client.models.match_advanced_stats_passes.Match Advanced Stats Passes(
                    assists = 56, 
                    avg_pass_length = 1.337, 
                    avg_pass_to_final_third_length = 1.337, 
                    back_passes = 56, 
                    back_passes_successful = 56, 
                    crosses_blocked = 56, 
                    crosses_from_left_flank = 56, 
                    crosses_from_left_flank_successful = 56, 
                    crosses_from_right_flank = 56, 
                    crosses_from_right_flank_successful = 56, 
                    crosses_high = 56, 
                    crosses_low = 56, 
                    crosses_successful = 56, 
                    crosses_total = 56, 
                    deep_completed_passes = 56, 
                    deep_completed_passes_successful = 56, 
                    forward_passes = 56, 
                    forward_passes_successful = 56, 
                    key_passes = 56, 
                    key_passes_successful = 56, 
                    lateral_passes = 56, 
                    lateral_passes_successful = 56, 
                    long_passes = 56, 
                    long_passes_successful = 56, 
                    match_tempo = 1.337, 
                    pass_to_final_thirds = 56, 
                    pass_to_final_thirds_successful = 56, 
                    pass_to_penalty_areas = 56, 
                    pass_to_penalty_areas_successful = 56, 
                    passes = 56, 
                    passes_successful = 56, 
                    progressive_passes = 56, 
                    progressive_passes_successful = 56, 
                    short_medium_passes = 56, 
                    short_medium_passes_successful = 56, 
                    shot_assists = 56, 
                    smart_passes = 56, 
                    smart_passes_successful = 56, 
                    through_passes = 56, 
                    through_passes_successful = 56, 
                    vertical_passes = 56, 
                    vertical_passes_successful = 56, )
            )
        else:
            return ListOfStatisticsPasses(
        )
        """

    def testListOfStatisticsPasses(self):
        """Test ListOfStatisticsPasses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
