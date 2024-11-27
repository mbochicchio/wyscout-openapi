# coding: utf-8

"""
    Wyscout API (v4)

    [Customer resources](https://www.hudl.com/support/wyscout) | [Customer support](https://www.hudl.com/support/contact)  [Wyscout Data resources](https://footballdata.wyscout.com/resources/)  **IMPORTANT: Version switching planned for July 20th 2021.**  On July 20th 2021 we will switch v3 as the Current version. V2 will become Legacy.  Please see [Versioning](#section/Versioning) section for any related details.  # Overview  This is the product documentation for our API service, in which you can find all definitions and technical information you may need.  # Authentication  ## Overview  This page explain how to authenticate to Wyscout APIs using Basic Access Authentication.  ## Using your client software  Depending on your client software you should be provided with a mechanism for supplying an username and password: that will build the required authentication headers automatically.  For example you can specify the -u argument with curl as username:password.  ## Supplying Basic Access Authentication headers  It is possible to construct the authentication headers manually:  * Build a string of the form username:password. * Encode the string in Base64 * Supply an `Authorization` header with content `Basic` followed by the encoded string.   For example, the string `Aladdin:OpenSesame` encodes to `QWxhZGRpbjpPcGVuU2VzYW1l` in base64,   so you would use this string `Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`  ## Rate limits  To avoid services overload requests are rate limited. The Wyscout API currently enforces a limit of **12** request per second per API Key.  If the rate limit is exceeded, the API will return the following HTTP 429 response:  ```json   {     \"error\": {       \"code\": 429,       \"message\": \"Too many requests\"     }   } ```  # Data glossary and definitions  At the following link you can find our Data Glossary that describes events, metrics and concepts used across the Wyscout API, Platform and reports.  <a href=\"https://dataglossary.wyscout.com/\" target=\"_blank\">Wyscout Data Glossary</a>   ## Pitch coordinates  ![Pitch map](assets/images/WyscoutDataCoordinates.png)  The event's coordinates depends on the subject. The subject's goal to be defended is always **x=0%** and the attack is always **x=100%**. All values are % expressed as **(x,y)**.  # Versioning  Wyscout gives you the chance to choose between three different sets of API endpoints.  ## Current The latest available version. It includes the most recent endpoints and improvements.  ## Preview The beta version of our next official release. Here we start to implement future improvements and new endpoints.  ## Legacy The old version. This is still available and running, in order to let users adapt their tools to new ones.  ## Version Switch  Wyscout will constantly improve its dataset by adding new endpoints and improving the existing ones. “Preview” version is where you can find last delivered updates. When a new and improved “Current” version is released, the previous version becomes “Legacy” – which means it will not immediately cease to exist, giving you the time to adapt your systems. It will be available and running until another new version – “Current” – is released, at least six months after the previous one.  ![Version Switch](assets/images/WyscoutVersionSwitch.png)  Documentation on [apidocs.wyscout.com](apidocs.wyscout.com) will always be available also for “Legacy” version. Each version will receive support as from the following table:  ![Version Support](assets/images/WyscoutVersionSupport.png)

    The version of the OpenAPI document: 2024-05-09T09:09:27Z
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.the_resource_object_resource_id import TheResourceObjectResourceId

class TestTheResourceObjectResourceId(unittest.TestCase):
    """TheResourceObjectResourceId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TheResourceObjectResourceId:
        """Test TheResourceObjectResourceId
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TheResourceObjectResourceId`
        """
        model = TheResourceObjectResourceId()
        if include_optional:
            return TheResourceObjectResourceId(
                alpha2code = '',
                alpha3code = '',
                id = 56,
                name = '',
                birth_area = openapi_client.models.area.Area(
                    alpha2code = '', 
                    alpha3code = '', 
                    id = 56, 
                    name = '', ),
                birth_date = '',
                current_team = {"area":{"alpha2code":"US","alpha3code":"USA","id":840,"name":"United States"},"category":"default","children":[{"name":"Richmond United U15/16","wyId":59333},{"name":"Richmond United U17/18","wyId":59421},{"name":"Richmond United U18/19","wyId":61155},{"name":"Richmond United U16/17","wyId":61231}],"city":"Richmond, Virginia","gender":"male","imageDataURL":"https://cdn5.wyscout.com/photos/team/public/g3196_120x120.png","name":"Richmond Kickers","officialName":"Richmond Kickers","type":"club","wyId":7862},
                current_team_id = 56,
                first_name = '',
                gender = 'male',
                gsm_id = 56,
                image_data_url = '',
                last_name = '',
                middle_name = '',
                passport_area = openapi_client.models.area.Area(
                    alpha2code = '', 
                    alpha3code = '', 
                    id = 56, 
                    name = '', ),
                short_name = '',
                status = '',
                wy_id = 56,
                area = openapi_client.models.area.Area(
                    alpha2code = '', 
                    alpha3code = '', 
                    id = 56, 
                    name = '', ),
                category = 'default',
                division_level = 0,
                format = 'Domestic cup',
                type = 'club',
                competition = {"area":{"alpha2code":"JO","alpha3code":"JOR","id":400,"name":"Jordan"},"category":"default","divisionLevel":0,"format":"Domestic league","gender":"male","gsmId":1195,"name":"1st Division","type":"club","wyId":1495},
                competition_id = '',
                var_date = '',
                dateutc = '',
                duration = 'Regular',
                gameweek = 56,
                has_data_available = True,
                label = '',
                referees = [
                    openapi_client.models.match_referees_inner.Match_referees_inner(
                        referee = null, 
                        referee_id = 56, 
                        role = 'referee', )
                    ],
                round = {"competition":{"area":{"alpha2code":"CO","alpha3code":"COL","id":170,"name":"Colombia"},"category":"default","divisionLevel":1,"format":"Domestic cup","gender":"male","gsmId":613,"name":"Copa Colombia","type":"club","wyId":293},"competitionId":293,"endDate":"2020-11-30","gsmId":-5447,"name":"Finals","season":{"active":true,"competitionId":293,"endDate":"2020-11-06","gsmId":-1812,"name":"2020","startDate":"2020-02-13","wyId":186471},"seasonId":186471,"startDate":"2020-11-01","type":"cup","wyId":4421914},
                round_id = 56,
                season = {"active":true,"competition":{"area":{"alpha2code":"WO","alpha3code":"XWO","id":1420,"name":"World"},"category":"default","divisionLevel":0,"format":"International cup","gender":"female","gsmId":1633,"name":"Yongchuan Tournament","type":"international","wyId":43037},"competitionId":43037,"endDate":"2019-11-17","gsmId":-2095,"name":"2019","startDate":"2019-11-07","wyId":186754},
                season_id = 56,
                teams_data = openapi_client.models.match_teams_data.Match teams data(
                    team_aid = null, 
                    team_bid = null, ),
                venue = '',
                winner = 56,
                elements = [
                    openapi_client.models.a_response_element_object.A response element object(
                        coaches = openapi_client.models.coaches_fetch.Coaches fetch(
                            <team_id> = openapi_client.models.team_coach.Team coach(
                                coach = {"birthArea":{"alpha2code":"IT","alpha3code":"ITA","id":380,"name":"Italy"},"birthDate":"1967-08-11","currentTeamId":3159,"firstName":"Massimiliano","gender":"male","gsmId":110817,"imageDataURL":"https://cdn5.wyscout.com/photos/players/public/g110817_100x130.png","lastName":"Allegri","middleName":"","passportArea":{"alpha2code":"IT","alpha3code":"ITA","id":380,"name":"Italy"},"shortName":"M. Allegri","status":"active","type":"coach","wyId":20386}, ), ), 
                        events = [
                            openapi_client.models.match_event.Match Event(
                                aerial_duel = openapi_client.models.aerial_duel_details.Aerial duel details(
                                    first_touch = True, 
                                    height = 56, 
                                    opponent = openapi_client.models.opponent_details.Opponent details(
                                        height = 56, 
                                        id = 56, 
                                        name = '', 
                                        position = '', ), 
                                    related_duel_id = 56, ), 
                                carry = openapi_client.models.carry_details.Carry details(
                                    end_location = openapi_client.models.carry_end_location.Carry end location(
                                        x = 56, 
                                        y = 56, ), 
                                    progression = 1.337, ), 
                                ground_duel = openapi_client.models.ground_duel_details.Ground duel details(
                                    duel_type = '', 
                                    kept_possession = True, 
                                    progressed_with_ball = True, 
                                    recovered_possession = True, 
                                    related_duel_id = 56, 
                                    side = '', 
                                    stopped_progress = True, 
                                    take_on = True, ), 
                                id = 56, 
                                infraction = openapi_client.models.infraction_details.Infraction details(
                                    red_card = True, 
                                    type = '', 
                                    yellow_card = True, ), 
                                location = openapi_client.models.event_location.Event location(
                                    x = 56, 
                                    y = 56, ), 
                                match_id = 56, 
                                match_period = '', 
                                match_timestamp = '', 
                                minute = 56, 
                                opponent_team = openapi_client.models.opponent_team_details.Opponent team details(
                                    formation = '', 
                                    id = 56, 
                                    name = '', ), 
                                pass = openapi_client.models.pass_details.Pass details(
                                    accurate = True, 
                                    angle = 56, 
                                    length = 1.337, 
                                    recipient = openapi_client.models.pass_recipient.Pass recipient(
                                        id = 56, 
                                        name = '', 
                                        position = '', ), ), 
                                player = openapi_client.models.player_details.Player details(
                                    id = 56, 
                                    name = '', 
                                    position = '', ), 
                                possession = openapi_client.models.possession_details.Possession details(
                                    attack = openapi_client.models.attack_details.Attack details(
                                        flank = '', 
                                        with_goal = True, 
                                        with_shot = True, 
                                        with_shot_on_goal = True, 
                                        xg = 56, ), 
                                    duration = '', 
                                    event_index = 56, 
                                    events_number = 56, 
                                    id = 56, 
                                    start_location = openapi_client.models.possession_start_location.Possession start location(
                                        x = 56, 
                                        y = 56, ), 
                                    team = openapi_client.models.team_details.Team details(
                                        formation = '', 
                                        id = 56, 
                                        name = '', ), 
                                    types = [
                                        ''
                                        ], ), 
                                related_event_id = 56, 
                                second = 56, 
                                shot = openapi_client.models.shot_details.Shot details(
                                    body_part = '', 
                                    goal_zone = '', 
                                    goalkeeper = openapi_client.models.goalkeeper_details.Goalkeeper details(
                                        id = 56, 
                                        name = '', ), 
                                    goalkeeper_action_id = 56, 
                                    is_goal = True, 
                                    on_target = True, 
                                    post_shot_xg = 1.337, 
                                    xg = 1.337, ), 
                                team = openapi_client.models.team_details.Team details(
                                    formation = '', 
                                    id = 56, 
                                    name = '', ), 
                                type = openapi_client.models.event_type.Event type(
                                    primary = '', 
                                    secondary = [
                                        ''
                                        ], ), 
                                video_timestamp = '', )
                            ], 
                        formations = openapi_client.models.formations_fetch.Formations fetch(), 
                        match = null, 
                        players = openapi_client.models.players_fetch.Players fetch(), 
                        referees = [
                            openapi_client.models.the_referee_object.The referee object(
                                referee_id = 56, 
                                role = '', )
                            ], 
                        substitutions = openapi_client.models.substitution_fetch.Substitution fetch(), 
                        teams = openapi_client.models.teams_fetch.Teams fetch(), )
                    ],
                meta = openapi_client.models.meta.Meta(
                    applied_filters = openapi_client.models.the_applied_filters_schema.The appliedFilters schema(
                        advsearch = [
                            ''
                            ], 
                        fetch = [
                            ''
                            ], 
                        filter = [
                            ''
                            ], 
                        limit = 56, 
                        page = 56, 
                        search = '', 
                        sort = [
                            ''
                            ], ), 
                    available_filters = openapi_client.models.the_available_filters_object.The available filters object(
                        advsearches = [
                            ''
                            ], 
                        fetches = [
                            ''
                            ], 
                        filters = [
                            ''
                            ], 
                        searches = [
                            ''
                            ], 
                        sorts = [
                            ''
                            ], ), 
                    page_count = 56, 
                    page_current = 56, 
                    page_size = 56, 
                    total_items = 56, ),
                career = [
                    openapi_client.models.the_team_career_array_inner.The_team_career_array_inner(
                        competition = null, 
                        competition_id = 56, 
                        goal_against = 56, 
                        goal_pro = 56, 
                        group_id = 56, 
                        group_name = '', 
                        match_draw = 56, 
                        match_lost = 56, 
                        match_total = 56, 
                        match_won = 56, 
                        points = 56, 
                        rank = 56, 
                        round_id = 56, 
                        round_name = '', 
                        season = null, 
                        season_id = 56, 
                        team_id = 56, )
                    ],
                player = {"birthArea":{"alpha2code":"PL","alpha3code":"POL","id":616,"name":"Poland"},"birthDate":"1995-07-01","currentNationalTeamId":13869,"currentTeam":{"area":{"alpha2code":"DE","alpha3code":"DEU","id":276,"name":"Germany"},"category":"default","children":[{"name":"Hertha BSC U23","wyId":63021},{"name":"Hertha BSC U17","wyId":32876},{"name":"Hertha BSC II","wyId":2589},{"name":"Hertha BSC U19","wyId":3130}],"city":"Berlin","gender":"male","gsmId":974,"name":"Hertha BSC","officialName":"Hertha BSC","type":"club","wyId":2457},"currentTeamId":2457,"firstName":"Krzysztof","foot":"right","gender":"male","gsmId":342295,"height":183,"imageDataURL":"https://cdn5.wyscout.com/photos/players/public/g342295_100x130.png","lastName":"Piątek","middleName":"","passportArea":{"alpha2code":"PL","alpha3code":"POL","id":616,"name":"Poland"},"role":{"code2":"FW","code3":"FWD","name":"Forward"},"shortName":"K. Piątek","status":"active","weight":77,"wyId":329061},
                injuries = [
                    openapi_client.models.the_injury_object.The injury object(
                        description = '', 
                        from_date = '', 
                        games_missed = 56, 
                        id = 56, 
                        injury_localization = '', 
                        injury_side = '', 
                        injury_type = '', 
                        is_disease = 56, 
                        player_id = 56, )
                    ],
                current_national_team_id = 56,
                foot = '',
                height = 56,
                role = openapi_client.models.main_role.Main role(
                    code2 = '', 
                    code3 = '', 
                    name = '', ),
                weight = 56,
                end_date = '',
                start_date = '',
                active = True,
                team = {"area":{"alpha2code":"US","alpha3code":"USA","id":840,"name":"United States"},"category":"default","children":[{"name":"Richmond United U15/16","wyId":59333},{"name":"Richmond United U17/18","wyId":59421},{"name":"Richmond United U18/19","wyId":61155},{"name":"Richmond United U16/17","wyId":61231}],"city":"Richmond, Virginia","gender":"male","imageDataURL":"https://cdn5.wyscout.com/photos/team/public/g3196_120x120.png","name":"Richmond Kickers","officialName":"Richmond Kickers","type":"club","wyId":7862},
                children = [
                    openapi_client.models.related_teams_inner.Related_teams_inner(
                        name = '', 
                        wy_id = 56, )
                    ],
                city = '',
                official_name = '',
                parent = openapi_client.models.parent_team.Parent team(
                    name = '', 
                    wy_id = 56, ),
                transfer = [
                    openapi_client.models.the_transfer_object.The transfer object(
                        active = 56, 
                        announce_date = '', 
                        currency = 'USD', 
                        end_date = '', 
                        from_team_id = 56, 
                        from_team_name = '', 
                        player_id = 56, 
                        start_date = '', 
                        teams_data = openapi_client.models.the_teams_data.The teams data(
                            from_team = openapi_client.models.origin_team_details.Origin team details(
                                team = {"area":{"alpha2code":"US","alpha3code":"USA","id":840,"name":"United States"},"category":"default","children":[{"name":"Richmond United U15/16","wyId":59333},{"name":"Richmond United U17/18","wyId":59421},{"name":"Richmond United U18/19","wyId":61155},{"name":"Richmond United U16/17","wyId":61231}],"city":"Richmond, Virginia","gender":"male","imageDataURL":"https://cdn5.wyscout.com/photos/team/public/g3196_120x120.png","name":"Richmond Kickers","officialName":"Richmond Kickers","type":"club","wyId":7862}, ), 
                            to_team = openapi_client.models.destination_team_details.Destination team details(), ), 
                        to_team_id = 56, 
                        to_team_name = '', 
                        transfer_id = 56, 
                        type = 'Transfer', 
                        value = 56, )
                    ]
            )
        else:
            return TheResourceObjectResourceId(
        )
        """

    def testTheResourceObjectResourceId(self):
        """Test TheResourceObjectResourceId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()