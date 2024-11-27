# coding: utf-8

"""
    Wyscout API (v4)

    [Customer resources](https://www.hudl.com/support/wyscout) | [Customer support](https://www.hudl.com/support/contact)  [Wyscout Data resources](https://footballdata.wyscout.com/resources/)  **IMPORTANT: Version switching planned for July 20th 2021.**  On July 20th 2021 we will switch v3 as the Current version. V2 will become Legacy.  Please see [Versioning](#section/Versioning) section for any related details.  # Overview  This is the product documentation for our API service, in which you can find all definitions and technical information you may need.  # Authentication  ## Overview  This page explain how to authenticate to Wyscout APIs using Basic Access Authentication.  ## Using your client software  Depending on your client software you should be provided with a mechanism for supplying an username and password: that will build the required authentication headers automatically.  For example you can specify the -u argument with curl as username:password.  ## Supplying Basic Access Authentication headers  It is possible to construct the authentication headers manually:  * Build a string of the form username:password. * Encode the string in Base64 * Supply an `Authorization` header with content `Basic` followed by the encoded string.   For example, the string `Aladdin:OpenSesame` encodes to `QWxhZGRpbjpPcGVuU2VzYW1l` in base64,   so you would use this string `Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`  ## Rate limits  To avoid services overload requests are rate limited. The Wyscout API currently enforces a limit of **12** request per second per API Key.  If the rate limit is exceeded, the API will return the following HTTP 429 response:  ```json   {     \"error\": {       \"code\": 429,       \"message\": \"Too many requests\"     }   } ```  # Data glossary and definitions  At the following link you can find our Data Glossary that describes events, metrics and concepts used across the Wyscout API, Platform and reports.  <a href=\"https://dataglossary.wyscout.com/\" target=\"_blank\">Wyscout Data Glossary</a>   ## Pitch coordinates  ![Pitch map](assets/images/WyscoutDataCoordinates.png)  The event's coordinates depends on the subject. The subject's goal to be defended is always **x=0%** and the attack is always **x=100%**. All values are % expressed as **(x,y)**.  # Versioning  Wyscout gives you the chance to choose between three different sets of API endpoints.  ## Current The latest available version. It includes the most recent endpoints and improvements.  ## Preview The beta version of our next official release. Here we start to implement future improvements and new endpoints.  ## Legacy The old version. This is still available and running, in order to let users adapt their tools to new ones.  ## Version Switch  Wyscout will constantly improve its dataset by adding new endpoints and improving the existing ones. “Preview” version is where you can find last delivered updates. When a new and improved “Current” version is released, the previous version becomes “Legacy” – which means it will not immediately cease to exist, giving you the time to adapt your systems. It will be available and running until another new version – “Current” – is released, at least six months after the previous one.  ![Version Switch](assets/images/WyscoutVersionSwitch.png)  Documentation on [apidocs.wyscout.com](apidocs.wyscout.com) will always be available also for “Legacy” version. Each version will receive support as from the following table:  ![Version Support](assets/images/WyscoutVersionSupport.png)

    The version of the OpenAPI document: 2024-05-09T09:09:27Z
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.season_fixtures import SeasonFixtures

class TestSeasonFixtures(unittest.TestCase):
    """SeasonFixtures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SeasonFixtures:
        """Test SeasonFixtures
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SeasonFixtures`
        """
        model = SeasonFixtures()
        if include_optional:
            return SeasonFixtures(
                competition = {"area":{"alpha2code":"JO","alpha3code":"JOR","id":400,"name":"Jordan"},"category":"default","divisionLevel":0,"format":"Domestic league","gender":"male","gsmId":1195,"name":"1st Division","type":"club","wyId":1495},
                competition_id = 56,
                matches = [
                    openapi_client.models.the_match_object.The match object(
                        goals = [
                            openapi_client.models.the_match_goal_object.The match goal object(
                                minute = 56, 
                                period = 'FirstHalf', 
                                player = null, 
                                player_id = 56, 
                                team = null, 
                                team_id = 56, 
                                type = 'goal', )
                            ], 
                        match = {"competition":{"area":{"alpha2code":"EU","alpha3code":"XEU","id":1106,"name":"Europe"},"category":"default","divisionLevel":3,"format":"International cup","gender":"male","gsmId":18,"name":"UEFA Europa League","type":"club","wyId":109},"competitionId":109,"date":"August 1, 2019 at 6:00:00 PM GMT+2","dateutc":"2019-08-01 16:00:00","duration":"Regular","gameweek":2,"gsmId":-174997,"hasDataAvailable":true,"label":"Zorya - Budućnost, 1 - 0","referees":[{"referee":{"birthArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"firstName":"Neil","gender":"male","gsmId":83716,"lastName":"Doyle","middleName":"","passportArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"shortName":"N. Doyle","status":"active","wyId":383495},"refereeId":383495,"role":"referee"},{"referee":{"birthArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"firstName":"Darren","gender":"male","gsmId":123424,"lastName":"Carey","middleName":"","passportArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"shortName":"D. Carey","status":"active","wyId":421655},"refereeId":421655,"role":"firstAssistant"},{"referee":{"birthArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"firstName":"Darragh","gender":"male","gsmId":331117,"lastName":"Keegan","middleName":"","passportArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"shortName":"D. Keegan","status":"active","wyId":421664},"refereeId":421664,"role":"secondAssistant"},{"referee":{"birthArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"firstName":"John","gender":"male","gsmId":121397,"lastName":"McLoughlin","middleName":"","passportArea":{"alpha2code":"IE","alpha3code":"IRL","id":372,"name":"Ireland Republic"},"shortName":"J. McLoughlin","status":"active","wyId":393686},"refereeId":393686,"role":"fourthOfficial"},{"refereeId":0,"role":"firstAdditionalAssistant"},{"refereeId":0,"role":"secondAdditionalAssistant"}],"round":{"competitionId":109,"endDate":"2019-08-01","gsmId":-3526,"name":"2nd Qualifying Round","seasonId":185518,"startDate":"2019-07-25","type":"table","wyId":4419932},"roundId":4419932,"season":{"active":false,"competitionId":109,"endDate":"2020-08-21","gsmId":-859,"name":"2019/2020","startDate":"2019-06-28","wyId":185518},"seasonId":185518,"status":"Played","teamsData":{"14536":{"coach":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1969-11-19","currentTeamId":14536,"firstName":"Viktor","gender":"male","gsmId":305413,"lastName":"Skripnik","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"shortName":"V. Skripnik","status":"active","wyId":271998},"coachId":271998,"formation":{"bench":[{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1990-06-21","currentTeamId":38304,"firstName":"Maksym","foot":"right","gender":"male","gsmId":130072,"height":187,"lastName":"Bilyi","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"M. Bilyi","status":"active","weight":78,"wyId":105551},"playerId":105551,"redCards":"0","shirtNumber":25,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1997-03-21","currentNationalTeamId":14622,"currentTeamId":5068,"firstName":"Bogdan","foot":"left","gender":"male","gsmId":319815,"height":178,"lastName":"Mykhaylichenko","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"B. Mykhaylichenko","status":"active","weight":73,"wyId":286249},"playerId":286249,"redCards":"0","shirtNumber":14,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"GE","alpha3code":"GEO","id":268,"name":"Georgia"},"birthDate":"1993-04-06","currentTeamId":14550,"firstName":"Levan","foot":"right","gender":"male","gsmId":302177,"height":181,"lastName":"Arveladze","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"L. Arveladze","status":"active","weight":75,"wyId":274576},"playerId":274576,"redCards":"0","shirtNumber":99,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1993-01-26","currentTeamId":14536,"firstName":"Mykyta","foot":"right","gender":"male","gsmId":179305,"height":191,"lastName":"Shevchenko","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"GK","code3":"GKP","name":"Goalkeeper"},"shortName":"M. Shevchenko","status":"active","weight":88,"wyId":105715},"playerId":105715,"redCards":"0","shirtNumber":30,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1985-06-03","firstName":"Mykyta","foot":"right","gender":"male","gsmId":36892,"height":172,"lastName":"Kamenyuka","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"M. Kamenyuka","status":"retired","weight":64,"wyId":105563},"playerId":105563,"redCards":"0","shirtNumber":6,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1991-10-07","currentTeamId":14536,"firstName":"Igor","foot":"right","gender":"male","gsmId":120112,"height":171,"lastName":"Chaykovskyi","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"I. Chaykovskyi","status":"active","weight":68,"wyId":138455},"playerId":138455,"redCards":"0","shirtNumber":77,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1995-09-01","currentTeamId":14536,"firstName":"Vladyslav","foot":"right","gender":"male","gsmId":335818,"height":176,"lastName":"Kabaev","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"V. Kabaev","status":"active","weight":63,"wyId":303428},"playerId":303428,"redCards":"0","shirtNumber":22,"yellowCards":"0"}],"lineup":[{"assists":"0","goals":"1","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1990-01-14","currentTeamId":14536,"firstName":"Artem","foot":"left","gender":"male","gsmId":125173,"height":178,"lastName":"Hromov","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"A. Hromov","status":"active","weight":72,"wyId":105860},"playerId":105860,"redCards":"0","shirtNumber":28,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1997-01-20","currentNationalTeamId":14622,"currentTeamId":14503,"firstName":"Oleksandr","foot":"right","gender":"male","gsmId":319813,"height":180,"lastName":"Tymchyk","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"O. Tymchyk","status":"active","weight":67,"wyId":286251},"playerId":286251,"redCards":"0","shirtNumber":18,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1996-04-30","currentTeamId":14536,"firstName":"Vladyslav","foot":"right","gender":"male","gsmId":389947,"height":178,"lastName":"Kochergin","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"V. Kochergin","status":"active","weight":70,"wyId":355915},"playerId":355915,"redCards":"0","shirtNumber":7,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"DE","alpha3code":"DEU","id":276,"name":"Germany"},"birthDate":"1998-01-22","currentNationalTeamId":13382,"currentTeamId":14536,"firstName":"Joël","foot":"left","gender":"male","gsmId":324626,"height":184,"lastName":"Abu Hanna","middleName":"","passportArea":{"alpha2code":"DE","alpha3code":"DEU","id":276,"name":"Germany"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"J. Abu Hanna","status":"active","weight":78,"wyId":292122},"playerId":292122,"redCards":"0","shirtNumber":20,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1998-05-22","currentNationalTeamId":14628,"currentTeamId":14536,"firstName":"Maksym","foot":"left","gender":"male","gsmId":450328,"height":183,"lastName":"Lunyov","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"M. Lunyov","status":"active","weight":73,"wyId":444166},"playerId":444166,"redCards":"0","shirtNumber":19,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1998-04-07","currentNationalTeamId":14628,"currentTeamId":14503,"firstName":"Bogdan","foot":"left","gender":"male","gsmId":459864,"height":173,"lastName":"Lednev","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"B. Lednev","status":"active","weight":70,"wyId":471622},"playerId":471622,"redCards":"0","shirtNumber":17,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1990-04-16","currentTeamId":14536,"firstName":"Dmytro","foot":"right","gender":"male","gsmId":140915,"height":182,"lastName":"Khomchenovskiy","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"D. Khomchenovskiy","status":"active","weight":74,"wyId":105564},"playerId":105564,"redCards":"0","shirtNumber":10,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1994-01-11","currentTeamId":14536,"firstName":"Dmitriy","foot":"right","gender":"male","gsmId":253049,"height":189,"lastName":"Ivanisenya","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"D. Ivanisenya","status":"active","weight":76,"wyId":221997},"playerId":221997,"redCards":"0","shirtNumber":21,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1998-01-23","currentNationalTeamId":14628,"currentTeamId":8754,"firstName":"Evgen","foot":"left","gender":"male","gsmId":377505,"height":177,"lastName":"Cheberko","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"E. Cheberko","status":"active","weight":66,"wyId":347438},"playerId":347438,"redCards":"0","shirtNumber":98,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1987-10-17","currentTeamId":14536,"firstName":"Vitali","foot":"right","gender":"male","gsmId":37042,"height":194,"lastName":"Vernydub","middleName":"","passportArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"V. Vernydub","status":"active","weight":84,"wyId":105556},"playerId":105556,"redCards":"0","shirtNumber":15,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"UA","alpha3code":"UKR","id":804,"name":"Ukraine"},"birthDate":"1993-03-24","currentTeamId":14536,"firstName":"Zaur","foot":"left","gender":"male","gsmId":196324,"height":186,"lastName":"Makharadze","middleName":"","passportArea":{"alpha2code":"GE","alpha3code":"GEO","id":268,"name":"Georgia"},"role":{"code2":"GK","code3":"GKP","name":"Goalkeeper"},"shortName":"Z. Makharadze","status":"active","weight":88,"wyId":106313},"playerId":106313,"redCards":"0","shirtNumber":1,"yellowCards":"0"}],"substitutions":[{"assists":"0","minute":61,"playerIn":303428,"playerOut":105860},{"assists":"0","minute":64,"playerIn":105563,"playerOut":286251},{"assists":"0","minute":68,"playerIn":138455,"playerOut":355915}]},"hasFormation":1,"score":1,"scoreET":0,"scoreHT":1,"scoreP":0,"side":"home","teamId":14536},"17331":{"coach":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1967-08-08","currentTeamId":0,"firstName":"Branko","gender":"male","gsmId":104866,"lastName":"Brnović","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"shortName":"B. Brnović","status":"active","wyId":267747},"coachId":267747,"formation":{"bench":[{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1993-02-28","currentTeamId":17340,"firstName":"Vuk","gender":"male","gsmId":228207,"height":187,"lastName":"Radović","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"GK","code3":"GKP","name":"Goalkeeper"},"shortName":"V. Radović","status":"active","weight":73,"wyId":236018},"playerId":236018,"redCards":"0","shirtNumber":27,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"2001-03-02","currentTeamId":17331,"firstName":"Petar","gender":"male","gsmId":518003,"height":0,"lastName":"Vukčević","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"P. Vukčević","status":"active","weight":0,"wyId":545392},"playerId":545392,"redCards":"0","shirtNumber":4,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"2001-02-20","currentNationalTeamId":17374,"currentTeamId":17331,"firstName":"Ivan","gender":"male","gsmId":518007,"height":0,"lastName":"Bojović","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"I. Bojović","status":"active","weight":0,"wyId":545396},"playerId":545396,"redCards":"0","shirtNumber":77,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1995-08-26","firstName":"Miloš","foot":"right","gender":"male","gsmId":286666,"height":182,"lastName":"Vučić","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"Miloš Vučić","status":"active","weight":72,"wyId":256534},"playerId":256534,"redCards":"0","shirtNumber":22,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1993-04-11","currentTeamId":17331,"firstName":"Dejan","foot":"right","gender":"male","gsmId":212070,"height":178,"lastName":"Zarubica","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"D. Zarubica","status":"active","weight":72,"wyId":140189},"playerId":140189,"redCards":"0","shirtNumber":99,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1993-12-02","currentTeamId":17331,"firstName":"Miloš","foot":"right","gender":"male","gsmId":212071,"height":0,"lastName":"Raičković","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"M. Raičković","status":"active","weight":0,"wyId":140187},"playerId":140187,"redCards":"0","shirtNumber":19,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"2000-09-28","currentNationalTeamId":17372,"currentTeamId":17339,"firstName":"Bojan","foot":"left","gender":"male","gsmId":466661,"height":0,"lastName":"Roganović","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"B. Roganović","status":"active","weight":0,"wyId":480154},"playerId":480154,"redCards":"0","shirtNumber":6,"yellowCards":"0"}],"lineup":[{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1997-01-23","currentTeamId":14536,"firstName":"Mihailo","foot":"right","gender":"male","gsmId":318378,"height":180,"lastName":"Perović","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"M. Perović","status":"active","weight":77,"wyId":284738},"playerId":284738,"redCards":"0","shirtNumber":9,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1988-08-07","currentTeamId":17331,"firstName":"Petar","foot":"right","gender":"male","gsmId":82994,"height":188,"lastName":"Grbić","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"P. Grbić","status":"active","weight":83,"wyId":97885},"playerId":97885,"redCards":"0","shirtNumber":18,"yellowCards":"35"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"SI","alpha3code":"SVN","id":705,"name":"Slovenia"},"birthDate":"1994-09-05","currentTeamId":17111,"firstName":"Dušan","foot":"left","gender":"male","gsmId":333794,"height":183,"lastName":"Stoiljković","middleName":"","passportArea":{"alpha2code":"SI","alpha3code":"SVN","id":705,"name":"Slovenia"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"D. Stoiljković","status":"active","weight":78,"wyId":300664},"playerId":300664,"redCards":"0","shirtNumber":30,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1999-05-12","currentNationalTeamId":17372,"currentTeamId":17331,"firstName":"Vasilije","foot":"right","gender":"male","gsmId":424240,"height":0,"lastName":"Terzić","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"V. Terzić","status":"active","weight":0,"wyId":405881},"playerId":405881,"redCards":"0","shirtNumber":29,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1990-05-30","currentTeamId":10988,"firstName":"Dejan","foot":"left","gender":"male","gsmId":84532,"height":183,"lastName":"Boljević","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"D. Boljević","status":"active","weight":83,"wyId":127917},"playerId":127917,"redCards":"0","shirtNumber":23,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1990-11-01","currentTeamId":17331,"firstName":"Luka","foot":"right","gender":"male","gsmId":92584,"height":170,"lastName":"Mirković","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"L. Mirković","status":"active","weight":70,"wyId":129056},"playerId":129056,"redCards":"0","shirtNumber":8,"yellowCards":"25"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"RS","alpha3code":"SRB","id":688,"name":"Serbia"},"birthDate":"1989-11-22","currentTeamId":17101,"firstName":"Miloš","foot":"left","gender":"male","gsmId":202963,"height":175,"lastName":"Mijić","middleName":"","passportArea":{"alpha2code":"RS","alpha3code":"SRB","id":688,"name":"Serbia"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"M. Mijić","status":"active","weight":72,"wyId":127567},"playerId":127567,"redCards":"0","shirtNumber":20,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"RS","alpha3code":"SRB","id":688,"name":"Serbia"},"birthDate":"1989-11-06","firstName":"Nikola","foot":"right","gender":"male","gsmId":143839,"height":183,"lastName":"Đurić","middleName":"","passportArea":{"alpha2code":"RS","alpha3code":"SRB","id":688,"name":"Serbia"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"N. Đurić","status":"active","weight":78,"wyId":127762},"playerId":127762,"redCards":"33","shirtNumber":80,"yellowCards":"24"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"2000-07-06","currentNationalTeamId":17372,"currentTeamId":9417,"firstName":"Stefan","foot":"right","gender":"male","gsmId":466664,"height":187,"lastName":"Milić","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"DF","code3":"DEF","name":"Defender"},"shortName":"S. Milić","status":"active","weight":79,"wyId":480156},"playerId":480156,"redCards":"0","shirtNumber":24,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1989-02-03","currentTeamId":17331,"firstName":"Miloš","foot":"right","gender":"male","gsmId":39659,"height":192,"lastName":"Dragojević","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"GK","code3":"GKP","name":"Goalkeeper"},"shortName":"M. Dragojević","status":"active","weight":88,"wyId":128725},"playerId":128725,"redCards":"0","shirtNumber":1,"yellowCards":"0"},{"assists":"0","goals":"0","ownGoals":"0","player":{"birthArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"birthDate":"1988-06-30","currentTeamId":17331,"firstName":"Draško","foot":"right","gender":"male","gsmId":41455,"height":182,"lastName":"Božović","middleName":"","passportArea":{"alpha2code":"ME","alpha3code":"MNE","id":499,"name":"Montenegro"},"role":{"code2":"MD","code3":"MID","name":"Midfielder"},"shortName":"D. Božović","status":"active","weight":80,"wyId":97875},"playerId":97875,"redCards":"34","shirtNumber":7,"yellowCards":"0"}],"substitutions":[{"assists":"0","minute":38,"playerIn":480154,"playerOut":284738},{"assists":"0","minute":53,"playerIn":140187,"playerOut":97885},{"assists":"0","minute":75,"playerIn":140189,"playerOut":300664}]},"hasFormation":1,"score":0,"scoreET":0,"scoreHT":0,"scoreP":0,"side":"away","teamId":17331}},"winner":14536,"wyId":2848936}, 
                        match_id = 56, )
                    ],
                season = {"active":true,"competition":{"area":{"alpha2code":"WO","alpha3code":"XWO","id":1420,"name":"World"},"category":"default","divisionLevel":0,"format":"International cup","gender":"female","gsmId":1633,"name":"Yongchuan Tournament","type":"international","wyId":43037},"competitionId":43037,"endDate":"2019-11-17","gsmId":-2095,"name":"2019","startDate":"2019-11-07","wyId":186754},
                season_id = 56
            )
        else:
            return SeasonFixtures(
        )
        """

    def testSeasonFixtures(self):
        """Test SeasonFixtures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()