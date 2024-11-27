# coding: utf-8

"""
    Wyscout API (v4)

    [Customer resources](https://www.hudl.com/support/wyscout) | [Customer support](https://www.hudl.com/support/contact)  [Wyscout Data resources](https://footballdata.wyscout.com/resources/)  **IMPORTANT: Version switching planned for July 20th 2021.**  On July 20th 2021 we will switch v3 as the Current version. V2 will become Legacy.  Please see [Versioning](#section/Versioning) section for any related details.  # Overview  This is the product documentation for our API service, in which you can find all definitions and technical information you may need.  # Authentication  ## Overview  This page explain how to authenticate to Wyscout APIs using Basic Access Authentication.  ## Using your client software  Depending on your client software you should be provided with a mechanism for supplying an username and password: that will build the required authentication headers automatically.  For example you can specify the -u argument with curl as username:password.  ## Supplying Basic Access Authentication headers  It is possible to construct the authentication headers manually:  * Build a string of the form username:password. * Encode the string in Base64 * Supply an `Authorization` header with content `Basic` followed by the encoded string.   For example, the string `Aladdin:OpenSesame` encodes to `QWxhZGRpbjpPcGVuU2VzYW1l` in base64,   so you would use this string `Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`  ## Rate limits  To avoid services overload requests are rate limited. The Wyscout API currently enforces a limit of **12** request per second per API Key.  If the rate limit is exceeded, the API will return the following HTTP 429 response:  ```json   {     \"error\": {       \"code\": 429,       \"message\": \"Too many requests\"     }   } ```  # Data glossary and definitions  At the following link you can find our Data Glossary that describes events, metrics and concepts used across the Wyscout API, Platform and reports.  <a href=\"https://dataglossary.wyscout.com/\" target=\"_blank\">Wyscout Data Glossary</a>   ## Pitch coordinates  ![Pitch map](assets/images/WyscoutDataCoordinates.png)  The event's coordinates depends on the subject. The subject's goal to be defended is always **x=0%** and the attack is always **x=100%**. All values are % expressed as **(x,y)**.  # Versioning  Wyscout gives you the chance to choose between three different sets of API endpoints.  ## Current The latest available version. It includes the most recent endpoints and improvements.  ## Preview The beta version of our next official release. Here we start to implement future improvements and new endpoints.  ## Legacy The old version. This is still available and running, in order to let users adapt their tools to new ones.  ## Version Switch  Wyscout will constantly improve its dataset by adding new endpoints and improving the existing ones. “Preview” version is where you can find last delivered updates. When a new and improved “Current” version is released, the previous version becomes “Legacy” – which means it will not immediately cease to exist, giving you the time to adapt your systems. It will be available and running until another new version – “Current” – is released, at least six months after the previous one.  ![Version Switch](assets/images/WyscoutVersionSwitch.png)  Documentation on [apidocs.wyscout.com](apidocs.wyscout.com) will always be available also for “Legacy” version. Each version will receive support as from the following table:  ![Version Support](assets/images/WyscoutVersionSupport.png)

    The version of the OpenAPI document: 2024-05-09T09:09:27Z
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.the_match_goal_object import TheMatchGoalObject

class TestTheMatchGoalObject(unittest.TestCase):
    """TheMatchGoalObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TheMatchGoalObject:
        """Test TheMatchGoalObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TheMatchGoalObject`
        """
        model = TheMatchGoalObject()
        if include_optional:
            return TheMatchGoalObject(
                minute = 56,
                period = 'FirstHalf',
                player = {"birthArea":{"alpha2code":"PL","alpha3code":"POL","id":616,"name":"Poland"},"birthDate":"1995-07-01","currentNationalTeamId":13869,"currentTeam":{"area":{"alpha2code":"DE","alpha3code":"DEU","id":276,"name":"Germany"},"category":"default","children":[{"name":"Hertha BSC U23","wyId":63021},{"name":"Hertha BSC U17","wyId":32876},{"name":"Hertha BSC II","wyId":2589},{"name":"Hertha BSC U19","wyId":3130}],"city":"Berlin","gender":"male","gsmId":974,"name":"Hertha BSC","officialName":"Hertha BSC","type":"club","wyId":2457},"currentTeamId":2457,"firstName":"Krzysztof","foot":"right","gender":"male","gsmId":342295,"height":183,"imageDataURL":"https://cdn5.wyscout.com/photos/players/public/g342295_100x130.png","lastName":"Piątek","middleName":"","passportArea":{"alpha2code":"PL","alpha3code":"POL","id":616,"name":"Poland"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"K. Piątek","status":"active","weight":77,"wyId":329061},
                player_id = 56,
                team = {"area":{"alpha2code":"US","alpha3code":"USA","id":840,"name":"United States"},"category":"default","children":[{"name":"Richmond United U15/16","wyId":59333},{"name":"Richmond United U17/18","wyId":59421},{"name":"Richmond United U18/19","wyId":61155},{"name":"Richmond United U16/17","wyId":61231}],"city":"Richmond, Virginia","gender":"male","imageDataURL":"https://cdn5.wyscout.com/photos/team/public/g3196_120x120.png","name":"Richmond Kickers","officialName":"Richmond Kickers","type":"club","wyId":7862},
                team_id = 56,
                type = 'goal'
            )
        else:
            return TheMatchGoalObject(
        )
        """

    def testTheMatchGoalObject(self):
        """Test TheMatchGoalObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
