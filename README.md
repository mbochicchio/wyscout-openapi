# openapi-client
[Customer resources](https://www.hudl.com/support/wyscout) | [Customer support](https://www.hudl.com/support/contact)

[Wyscout Data resources](https://footballdata.wyscout.com/resources/)

**IMPORTANT: Version switching planned for July 20th 2021.**

On July 20th 2021 we will switch v3 as the Current version. V2 will become Legacy.

Please see [Versioning](#section/Versioning) section for any related details.

# Overview

This is the product documentation for our API service, in which you can find
all definitions and technical information you may need.

# Authentication

## Overview

This page explain how to authenticate to Wyscout APIs using Basic Access
Authentication.

## Using your client software

Depending on your client software you should be provided with a mechanism
for supplying an username and password: that will build the required
authentication headers automatically.

For example you can specify the -u argument with curl as username:password.

## Supplying Basic Access Authentication headers

It is possible to construct the authentication headers manually:

* Build a string of the form username:password.
* Encode the string in Base64
* Supply an `Authorization` header with content `Basic` followed by the
encoded string.


For example, the string `Aladdin:OpenSesame` encodes to
`QWxhZGRpbjpPcGVuU2VzYW1l` in base64, 

so you would use this string `Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`

## Rate limits

To avoid services overload requests are rate limited.
The Wyscout API currently enforces a limit of **12** request per second per API Key.

If the rate limit is exceeded, the API will return the following HTTP 429 response:

```json
  {
    \"error\": {
      \"code\": 429,
      \"message\": \"Too many requests\"
    }
  }
```

# Data glossary and definitions

At the following link you can find our Data Glossary that describes events, metrics and concepts used across the Wyscout API, Platform and reports.

<a href=\"https://dataglossary.wyscout.com/\" target=\"_blank\">Wyscout Data Glossary</a>


## Pitch coordinates

![Pitch map](assets/images/WyscoutDataCoordinates.png)

The event's coordinates depends on the subject. The subject's goal to be defended is always **x=0%**
and the attack is always **x=100%**.
All values are % expressed as **(x,y)**.

# Versioning

Wyscout gives you the chance to choose between three different sets of API endpoints.

## Current
The latest available version.
It includes the most recent endpoints and improvements.

## Preview
The beta version of our next official release.
Here we start to implement future improvements and new endpoints.

## Legacy
The old version.
This is still available and running, in order to let users adapt their tools to new ones.

## Version Switch

Wyscout will constantly improve its dataset by adding new endpoints and improving the existing ones. “Preview” version is where you can find last delivered updates.
When a new and improved “Current” version is released, the previous version becomes “Legacy” – which means it will not immediately cease to exist, giving you the time to adapt your systems.
It will be available and running until another new version – “Current” – is released, at least six months after the previous one.

![Version Switch](assets/images/WyscoutVersionSwitch.png)

Documentation on [apidocs.wyscout.com](apidocs.wyscout.com) will always be available also for “Legacy” version.
Each version will receive support as from the following table:

![Version Support](assets/images/WyscoutVersionSupport.png)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2024-05-09T09:09:27Z
- Package version: 1.0.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apirest.wyscout.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://apirest.wyscout.com/v4"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AdvancedStatsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    use_sides = 'use_sides_example' # str | Flag to change label (<teamId> –> home or <teamId> –> away) (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `teams`, `match` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Match Advanced Stats
        api_response = api_instance.matches_wy_id_advancedstats_get(wy_id, use_sides=use_sides, details=details, authorization=authorization)
        print("The response of AdvancedStatsApi->matches_wy_id_advancedstats_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedStatsApi->matches_wy_id_advancedstats_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apirest.wyscout.com/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdvancedStatsApi* | [**matches_wy_id_advancedstats_get**](docs/AdvancedStatsApi.md#matches_wy_id_advancedstats_get) | **GET** /matches/{wyId}/advancedstats | Match Advanced Stats
*AdvancedStatsApi* | [**matches_wy_id_advancedstats_players_get**](docs/AdvancedStatsApi.md#matches_wy_id_advancedstats_players_get) | **GET** /matches/{wyId}/advancedstats/players | All players Match Advanced Stats
*AdvancedStatsApi* | [**players_wy_id_advancedstats_get**](docs/AdvancedStatsApi.md#players_wy_id_advancedstats_get) | **GET** /players/{wyId}/advancedstats | Player Advanced Stats
*AdvancedStatsApi* | [**players_wy_id_matches_match_wy_id_advancedstats_get**](docs/AdvancedStatsApi.md#players_wy_id_matches_match_wy_id_advancedstats_get) | **GET** /players/{wyId}/matches/{matchWyId}/advancedstats | Players match advanced stats
*AdvancedStatsApi* | [**teams_wy_id_advancedstats_get**](docs/AdvancedStatsApi.md#teams_wy_id_advancedstats_get) | **GET** /teams/{wyId}/advancedstats | Teams Advanced Stats
*AdvancedStatsApi* | [**teams_wy_id_matches_match_wy_id_advancedstats_get**](docs/AdvancedStatsApi.md#teams_wy_id_matches_match_wy_id_advancedstats_get) | **GET** /teams/{wyId}/matches/{matchWyId}/advancedstats | Teams match advanced stats
*AreasApi* | [**areas_get**](docs/AreasApi.md#areas_get) | **GET** /areas | Areas
*CoachesApi* | [**coaches_wy_id_get**](docs/CoachesApi.md#coaches_wy_id_get) | **GET** /coaches/{wyId} | Coach
*CompetitionsApi* | [**competitions_get**](docs/CompetitionsApi.md#competitions_get) | **GET** /competitions | Competitions list
*CompetitionsApi* | [**competitions_wy_id_get**](docs/CompetitionsApi.md#competitions_wy_id_get) | **GET** /competitions/{wyId} | Competition detail
*CompetitionsApi* | [**competitions_wy_id_matches_get**](docs/CompetitionsApi.md#competitions_wy_id_matches_get) | **GET** /competitions/{wyId}/matches | Matches list
*CompetitionsApi* | [**competitions_wy_id_players_get**](docs/CompetitionsApi.md#competitions_wy_id_players_get) | **GET** /competitions/{wyId}/players | Players list
*CompetitionsApi* | [**competitions_wy_id_seasons_get**](docs/CompetitionsApi.md#competitions_wy_id_seasons_get) | **GET** /competitions/{wyId}/seasons | Seasons list
*CompetitionsApi* | [**competitions_wy_id_teams_get**](docs/CompetitionsApi.md#competitions_wy_id_teams_get) | **GET** /competitions/{wyId}/teams | Teams list
*EventsApi* | [**matches_wy_id_events_get**](docs/EventsApi.md#matches_wy_id_events_get) | **GET** /matches/{wyId}/events | MatchEvents
*ExtraApi* | [**updatedobjects_deleted_get**](docs/ExtraApi.md#updatedobjects_deleted_get) | **GET** /updatedobjects/deleted | Updated Objects deleted
*ExtraApi* | [**updatedobjects_updated_get**](docs/ExtraApi.md#updatedobjects_updated_get) | **GET** /updatedobjects/updated | Updated Objects updated
*MatchesApi* | [**matches_wy_id_directions_get**](docs/MatchesApi.md#matches_wy_id_directions_get) | **GET** /matches/{wyId}/directions | Match directions
*MatchesApi* | [**matches_wy_id_formations_get**](docs/MatchesApi.md#matches_wy_id_formations_get) | **GET** /matches/{wyId}/formations | Match formations
*MatchesApi* | [**matches_wy_id_get**](docs/MatchesApi.md#matches_wy_id_get) | **GET** /matches/{wyId} | Match detail
*PlayersApi* | [**players_wy_id_career_get**](docs/PlayersApi.md#players_wy_id_career_get) | **GET** /players/{wyId}/career | Players career
*PlayersApi* | [**players_wy_id_contractinfo_get**](docs/PlayersApi.md#players_wy_id_contractinfo_get) | **GET** /players/{wyId}/contractinfo | Players contract info
*PlayersApi* | [**players_wy_id_fixtures_get**](docs/PlayersApi.md#players_wy_id_fixtures_get) | **GET** /players/{wyId}/fixtures | Players fixtures
*PlayersApi* | [**players_wy_id_get**](docs/PlayersApi.md#players_wy_id_get) | **GET** /players/{wyId} | Player details
*PlayersApi* | [**players_wy_id_matches_get**](docs/PlayersApi.md#players_wy_id_matches_get) | **GET** /players/{wyId}/matches | Players matches
*PlayersApi* | [**players_wy_id_transfers_get**](docs/PlayersApi.md#players_wy_id_transfers_get) | **GET** /players/{wyId}/transfers | Players transfers
*RefereesApi* | [**referees_wy_id_get**](docs/RefereesApi.md#referees_wy_id_get) | **GET** /referees/{wyId} | Referee details
*RoundsApi* | [**rounds_wy_id_get**](docs/RoundsApi.md#rounds_wy_id_get) | **GET** /rounds/{wyId} | Rounds
*SearchApi* | [**search_get**](docs/SearchApi.md#search_get) | **GET** /search | Search
*SeasonsApi* | [**seasons_wy_id_assistmen_get**](docs/SeasonsApi.md#seasons_wy_id_assistmen_get) | **GET** /seasons/{wyId}/assistmen | Season assistmen
*SeasonsApi* | [**seasons_wy_id_career_get**](docs/SeasonsApi.md#seasons_wy_id_career_get) | **GET** /seasons/{wyId}/career | Seasons career
*SeasonsApi* | [**seasons_wy_id_fixtures_get**](docs/SeasonsApi.md#seasons_wy_id_fixtures_get) | **GET** /seasons/{wyId}/fixtures | Seasons fixtures
*SeasonsApi* | [**seasons_wy_id_get**](docs/SeasonsApi.md#seasons_wy_id_get) | **GET** /seasons/{wyId} | Season details
*SeasonsApi* | [**seasons_wy_id_matches_get**](docs/SeasonsApi.md#seasons_wy_id_matches_get) | **GET** /seasons/{wyId}/matches | Seasons matches
*SeasonsApi* | [**seasons_wy_id_players_get**](docs/SeasonsApi.md#seasons_wy_id_players_get) | **GET** /seasons/{wyId}/players | Seasons players
*SeasonsApi* | [**seasons_wy_id_scorers_get**](docs/SeasonsApi.md#seasons_wy_id_scorers_get) | **GET** /seasons/{wyId}/scorers | Season scorers
*SeasonsApi* | [**seasons_wy_id_standings_get**](docs/SeasonsApi.md#seasons_wy_id_standings_get) | **GET** /seasons/{wyId}/standings | Seasons standings
*SeasonsApi* | [**seasons_wy_id_teams_get**](docs/SeasonsApi.md#seasons_wy_id_teams_get) | **GET** /seasons/{wyId}/teams | Seasons teams
*SeasonsApi* | [**seasons_wy_id_transfers_get**](docs/SeasonsApi.md#seasons_wy_id_transfers_get) | **GET** /seasons/{wyId}/transfers | Seasons transfers
*TeamsApi* | [**teams_wy_id_career_get**](docs/TeamsApi.md#teams_wy_id_career_get) | **GET** /teams/{wyId}/career | Team careers
*TeamsApi* | [**teams_wy_id_fixtures_get**](docs/TeamsApi.md#teams_wy_id_fixtures_get) | **GET** /teams/{wyId}/fixtures | Teams fixtures
*TeamsApi* | [**teams_wy_id_get**](docs/TeamsApi.md#teams_wy_id_get) | **GET** /teams/{wyId} | Team details
*TeamsApi* | [**teams_wy_id_matches_get**](docs/TeamsApi.md#teams_wy_id_matches_get) | **GET** /teams/{wyId}/matches | Teams matches
*TeamsApi* | [**teams_wy_id_squad_get**](docs/TeamsApi.md#teams_wy_id_squad_get) | **GET** /teams/{wyId}/squad | Teams squad
*TeamsApi* | [**teams_wy_id_transfers_get**](docs/TeamsApi.md#teams_wy_id_transfers_get) | **GET** /teams/{wyId}/transfers | Teams transfers
*TrackingApi* | [**matches_wy_id_fulltracking_get**](docs/TrackingApi.md#matches_wy_id_fulltracking_get) | **GET** /matches/{wyId}/fulltracking | Broadcast tracking
*TrackingApi* | [**matches_wy_id_physicaldata_get**](docs/TrackingApi.md#matches_wy_id_physicaldata_get) | **GET** /matches/{wyId}/physicaldata | Match physical summary data
*VideosApi* | [**videos_match_id_get**](docs/VideosApi.md#videos_match_id_get) | **GET** /videos/{matchId} | Videos
*VideosApi* | [**videos_match_id_offsets_get**](docs/VideosApi.md#videos_match_id_offsets_get) | **GET** /videos/{matchId}/offsets | Videos offsets
*VideosApi* | [**videos_match_id_qualities_get**](docs/VideosApi.md#videos_match_id_qualities_get) | **GET** /videos/{matchId}/qualities | Videos qualities
*DefaultApi* | [**areas_options**](docs/DefaultApi.md#areas_options) | **OPTIONS** /areas | Areas
*DefaultApi* | [**coaches_wy_id_options**](docs/DefaultApi.md#coaches_wy_id_options) | **OPTIONS** /coaches/{wyId} | 
*DefaultApi* | [**competitions_options**](docs/DefaultApi.md#competitions_options) | **OPTIONS** /competitions | 
*DefaultApi* | [**competitions_wy_id_matches_options**](docs/DefaultApi.md#competitions_wy_id_matches_options) | **OPTIONS** /competitions/{wyId}/matches | 
*DefaultApi* | [**competitions_wy_id_options**](docs/DefaultApi.md#competitions_wy_id_options) | **OPTIONS** /competitions/{wyId} | 
*DefaultApi* | [**competitions_wy_id_players_options**](docs/DefaultApi.md#competitions_wy_id_players_options) | **OPTIONS** /competitions/{wyId}/players | 
*DefaultApi* | [**competitions_wy_id_seasons_options**](docs/DefaultApi.md#competitions_wy_id_seasons_options) | **OPTIONS** /competitions/{wyId}/seasons | 
*DefaultApi* | [**competitions_wy_id_teams_options**](docs/DefaultApi.md#competitions_wy_id_teams_options) | **OPTIONS** /competitions/{wyId}/teams | 
*DefaultApi* | [**matches_wy_id_advancedstats_options**](docs/DefaultApi.md#matches_wy_id_advancedstats_options) | **OPTIONS** /matches/{wyId}/advancedstats | 
*DefaultApi* | [**matches_wy_id_advancedstats_players_options**](docs/DefaultApi.md#matches_wy_id_advancedstats_players_options) | **OPTIONS** /matches/{wyId}/advancedstats/players | 
*DefaultApi* | [**matches_wy_id_directions_options**](docs/DefaultApi.md#matches_wy_id_directions_options) | **OPTIONS** /matches/{wyId}/directions | 
*DefaultApi* | [**matches_wy_id_events_options**](docs/DefaultApi.md#matches_wy_id_events_options) | **OPTIONS** /matches/{wyId}/events | 
*DefaultApi* | [**matches_wy_id_formations_options**](docs/DefaultApi.md#matches_wy_id_formations_options) | **OPTIONS** /matches/{wyId}/formations | 
*DefaultApi* | [**matches_wy_id_fulltracking_options**](docs/DefaultApi.md#matches_wy_id_fulltracking_options) | **OPTIONS** /matches/{wyId}/fulltracking | 
*DefaultApi* | [**matches_wy_id_options**](docs/DefaultApi.md#matches_wy_id_options) | **OPTIONS** /matches/{wyId} | 
*DefaultApi* | [**matches_wy_id_physicaldata_options**](docs/DefaultApi.md#matches_wy_id_physicaldata_options) | **OPTIONS** /matches/{wyId}/physicaldata | 
*DefaultApi* | [**players_wy_id_advancedstats_options**](docs/DefaultApi.md#players_wy_id_advancedstats_options) | **OPTIONS** /players/{wyId}/advancedstats | 
*DefaultApi* | [**players_wy_id_career_options**](docs/DefaultApi.md#players_wy_id_career_options) | **OPTIONS** /players/{wyId}/career | 
*DefaultApi* | [**players_wy_id_contractinfo_options**](docs/DefaultApi.md#players_wy_id_contractinfo_options) | **OPTIONS** /players/{wyId}/contractinfo | 
*DefaultApi* | [**players_wy_id_fixtures_options**](docs/DefaultApi.md#players_wy_id_fixtures_options) | **OPTIONS** /players/{wyId}/fixtures | 
*DefaultApi* | [**players_wy_id_matches_match_wy_id_advancedstats_options**](docs/DefaultApi.md#players_wy_id_matches_match_wy_id_advancedstats_options) | **OPTIONS** /players/{wyId}/matches/{matchWyId}/advancedstats | 
*DefaultApi* | [**players_wy_id_matches_match_wy_id_options**](docs/DefaultApi.md#players_wy_id_matches_match_wy_id_options) | **OPTIONS** /players/{wyId}/matches/{matchWyId} | 
*DefaultApi* | [**players_wy_id_matches_options**](docs/DefaultApi.md#players_wy_id_matches_options) | **OPTIONS** /players/{wyId}/matches | 
*DefaultApi* | [**players_wy_id_options**](docs/DefaultApi.md#players_wy_id_options) | **OPTIONS** /players/{wyId} | 
*DefaultApi* | [**players_wy_id_transfers_options**](docs/DefaultApi.md#players_wy_id_transfers_options) | **OPTIONS** /players/{wyId}/transfers | 
*DefaultApi* | [**referees_wy_id_options**](docs/DefaultApi.md#referees_wy_id_options) | **OPTIONS** /referees/{wyId} | 
*DefaultApi* | [**rounds_wy_id_options**](docs/DefaultApi.md#rounds_wy_id_options) | **OPTIONS** /rounds/{wyId} | 
*DefaultApi* | [**search_options**](docs/DefaultApi.md#search_options) | **OPTIONS** /search | 
*DefaultApi* | [**seasons_wy_id_assistmen_options**](docs/DefaultApi.md#seasons_wy_id_assistmen_options) | **OPTIONS** /seasons/{wyId}/assistmen | 
*DefaultApi* | [**seasons_wy_id_career_options**](docs/DefaultApi.md#seasons_wy_id_career_options) | **OPTIONS** /seasons/{wyId}/career | 
*DefaultApi* | [**seasons_wy_id_fixtures_options**](docs/DefaultApi.md#seasons_wy_id_fixtures_options) | **OPTIONS** /seasons/{wyId}/fixtures | 
*DefaultApi* | [**seasons_wy_id_matches_options**](docs/DefaultApi.md#seasons_wy_id_matches_options) | **OPTIONS** /seasons/{wyId}/matches | 
*DefaultApi* | [**seasons_wy_id_options**](docs/DefaultApi.md#seasons_wy_id_options) | **OPTIONS** /seasons/{wyId} | 
*DefaultApi* | [**seasons_wy_id_players_options**](docs/DefaultApi.md#seasons_wy_id_players_options) | **OPTIONS** /seasons/{wyId}/players | 
*DefaultApi* | [**seasons_wy_id_scorers_options**](docs/DefaultApi.md#seasons_wy_id_scorers_options) | **OPTIONS** /seasons/{wyId}/scorers | 
*DefaultApi* | [**seasons_wy_id_standings_options**](docs/DefaultApi.md#seasons_wy_id_standings_options) | **OPTIONS** /seasons/{wyId}/standings | 
*DefaultApi* | [**seasons_wy_id_teams_options**](docs/DefaultApi.md#seasons_wy_id_teams_options) | **OPTIONS** /seasons/{wyId}/teams | 
*DefaultApi* | [**seasons_wy_id_transfers_options**](docs/DefaultApi.md#seasons_wy_id_transfers_options) | **OPTIONS** /seasons/{wyId}/transfers | 
*DefaultApi* | [**teams_wy_id_advancedstats_options**](docs/DefaultApi.md#teams_wy_id_advancedstats_options) | **OPTIONS** /teams/{wyId}/advancedstats | 
*DefaultApi* | [**teams_wy_id_career_options**](docs/DefaultApi.md#teams_wy_id_career_options) | **OPTIONS** /teams/{wyId}/career | 
*DefaultApi* | [**teams_wy_id_fixtures_options**](docs/DefaultApi.md#teams_wy_id_fixtures_options) | **OPTIONS** /teams/{wyId}/fixtures | 
*DefaultApi* | [**teams_wy_id_matches_match_wy_id_advancedstats_options**](docs/DefaultApi.md#teams_wy_id_matches_match_wy_id_advancedstats_options) | **OPTIONS** /teams/{wyId}/matches/{matchWyId}/advancedstats | 
*DefaultApi* | [**teams_wy_id_matches_match_wy_id_options**](docs/DefaultApi.md#teams_wy_id_matches_match_wy_id_options) | **OPTIONS** /teams/{wyId}/matches/{matchWyId} | 
*DefaultApi* | [**teams_wy_id_matches_options**](docs/DefaultApi.md#teams_wy_id_matches_options) | **OPTIONS** /teams/{wyId}/matches | 
*DefaultApi* | [**teams_wy_id_options**](docs/DefaultApi.md#teams_wy_id_options) | **OPTIONS** /teams/{wyId} | 
*DefaultApi* | [**teams_wy_id_squad_options**](docs/DefaultApi.md#teams_wy_id_squad_options) | **OPTIONS** /teams/{wyId}/squad | 
*DefaultApi* | [**teams_wy_id_transfers_options**](docs/DefaultApi.md#teams_wy_id_transfers_options) | **OPTIONS** /teams/{wyId}/transfers | 
*DefaultApi* | [**updatedobjects_deleted_options**](docs/DefaultApi.md#updatedobjects_deleted_options) | **OPTIONS** /updatedobjects/deleted | 
*DefaultApi* | [**updatedobjects_updated_options**](docs/DefaultApi.md#updatedobjects_updated_options) | **OPTIONS** /updatedobjects/updated | 
*DefaultApi* | [**videos_match_id_offsets_options**](docs/DefaultApi.md#videos_match_id_offsets_options) | **OPTIONS** /videos/{matchId}/offsets | 
*DefaultApi* | [**videos_match_id_options**](docs/DefaultApi.md#videos_match_id_options) | **OPTIONS** /videos/{matchId} | 
*DefaultApi* | [**videos_match_id_qualities_options**](docs/DefaultApi.md#videos_match_id_qualities_options) | **OPTIONS** /videos/{matchId}/qualities | 


## Documentation For Models

 - [AResponseElementObject](docs/AResponseElementObject.md)
 - [AerialDuelDetails](docs/AerialDuelDetails.md)
 - [Area](docs/Area.md)
 - [AttackDetails](docs/AttackDetails.md)
 - [CarryDetails](docs/CarryDetails.md)
 - [CarryEndLocation](docs/CarryEndLocation.md)
 - [Coach](docs/Coach.md)
 - [CoachesFetch](docs/CoachesFetch.md)
 - [Competition](docs/Competition.md)
 - [CompetitionMatches](docs/CompetitionMatches.md)
 - [CompetitionPlayers](docs/CompetitionPlayers.md)
 - [CompetitionSeasons](docs/CompetitionSeasons.md)
 - [CompetitionTeams](docs/CompetitionTeams.md)
 - [Competitions](docs/Competitions.md)
 - [DestinationTeamDetails](docs/DestinationTeamDetails.md)
 - [ErrorCode400](docs/ErrorCode400.md)
 - [ErrorCode429](docs/ErrorCode429.md)
 - [ErrorCode500](docs/ErrorCode500.md)
 - [ErrorObject](docs/ErrorObject.md)
 - [EventLocation](docs/EventLocation.md)
 - [EventType](docs/EventType.md)
 - [FormationsFetch](docs/FormationsFetch.md)
 - [FormationsRelatedToTheEventSecondStartsec](docs/FormationsRelatedToTheEventSecondStartsec.md)
 - [FormationsRelatedToThePeriodMatchPeriod](docs/FormationsRelatedToThePeriodMatchPeriod.md)
 - [FormationsRelatedToTheTeamWithIDTeamId](docs/FormationsRelatedToTheTeamWithIDTeamId.md)
 - [GoalkeeperDetails](docs/GoalkeeperDetails.md)
 - [GroundDuelDetails](docs/GroundDuelDetails.md)
 - [GroupStandings](docs/GroupStandings.md)
 - [InformationAboutVideoOffsets](docs/InformationAboutVideoOffsets.md)
 - [InfractionDetails](docs/InfractionDetails.md)
 - [ListOfStatisticsAttacks](docs/ListOfStatisticsAttacks.md)
 - [ListOfStatisticsDefense](docs/ListOfStatisticsDefense.md)
 - [ListOfStatisticsDuels](docs/ListOfStatisticsDuels.md)
 - [ListOfStatisticsFlanks](docs/ListOfStatisticsFlanks.md)
 - [ListOfStatisticsGeneral](docs/ListOfStatisticsGeneral.md)
 - [ListOfStatisticsOpenPlay](docs/ListOfStatisticsOpenPlay.md)
 - [ListOfStatisticsPasses](docs/ListOfStatisticsPasses.md)
 - [ListOfStatisticsPossession](docs/ListOfStatisticsPossession.md)
 - [ListOfStatisticsTransitions](docs/ListOfStatisticsTransitions.md)
 - [MainRole](docs/MainRole.md)
 - [Match](docs/Match.md)
 - [MatchAdvancedStats](docs/MatchAdvancedStats.md)
 - [MatchAdvancedStatsAttacks](docs/MatchAdvancedStatsAttacks.md)
 - [MatchAdvancedStatsDefence](docs/MatchAdvancedStatsDefence.md)
 - [MatchAdvancedStatsDuels](docs/MatchAdvancedStatsDuels.md)
 - [MatchAdvancedStatsFlanks](docs/MatchAdvancedStatsFlanks.md)
 - [MatchAdvancedStatsGeneral](docs/MatchAdvancedStatsGeneral.md)
 - [MatchAdvancedStatsOpenPlay](docs/MatchAdvancedStatsOpenPlay.md)
 - [MatchAdvancedStatsPasses](docs/MatchAdvancedStatsPasses.md)
 - [MatchAdvancedStatsPossession](docs/MatchAdvancedStatsPossession.md)
 - [MatchAdvancedStatsTransitions](docs/MatchAdvancedStatsTransitions.md)
 - [MatchDirections](docs/MatchDirections.md)
 - [MatchDirectionsObject](docs/MatchDirectionsObject.md)
 - [MatchEvent](docs/MatchEvent.md)
 - [MatchEvents](docs/MatchEvents.md)
 - [MatchFormation](docs/MatchFormation.md)
 - [MatchFormations](docs/MatchFormations.md)
 - [MatchFullTracking](docs/MatchFullTracking.md)
 - [MatchPhysicalDataInner](docs/MatchPhysicalDataInner.md)
 - [MatchPhysicalDataInnerPlayersInner](docs/MatchPhysicalDataInnerPlayersInner.md)
 - [MatchPhysicalDataInnerPlayersInnerMetricsInner](docs/MatchPhysicalDataInnerPlayersInnerMetricsInner.md)
 - [MatchPhysicalDataInnerPlayersInnerMetricsInnerValuesInner](docs/MatchPhysicalDataInnerPlayersInnerMetricsInnerValuesInner.md)
 - [MatchPlayersAdvancedStats](docs/MatchPlayersAdvancedStats.md)
 - [MatchRefereesInner](docs/MatchRefereesInner.md)
 - [MatchTeamData](docs/MatchTeamData.md)
 - [MatchTeamsData](docs/MatchTeamsData.md)
 - [Meta](docs/Meta.md)
 - [Offset](docs/Offset.md)
 - [Offset1](docs/Offset1.md)
 - [Offset2](docs/Offset2.md)
 - [Offset3](docs/Offset3.md)
 - [Offset4](docs/Offset4.md)
 - [Offset5](docs/Offset5.md)
 - [Offsets](docs/Offsets.md)
 - [OpponentDetails](docs/OpponentDetails.md)
 - [OpponentDetails1](docs/OpponentDetails1.md)
 - [OpponentTeamDetails](docs/OpponentTeamDetails.md)
 - [OriginTeamDetails](docs/OriginTeamDetails.md)
 - [ParentTeam](docs/ParentTeam.md)
 - [PassDetails](docs/PassDetails.md)
 - [PassEndLocation](docs/PassEndLocation.md)
 - [PassRecipient](docs/PassRecipient.md)
 - [Player](docs/Player.md)
 - [PlayerAdvancedStats](docs/PlayerAdvancedStats.md)
 - [PlayerAdvancedStatsAverage](docs/PlayerAdvancedStatsAverage.md)
 - [PlayerAdvancedStatsPercent](docs/PlayerAdvancedStatsPercent.md)
 - [PlayerAdvancedStatsPosition](docs/PlayerAdvancedStatsPosition.md)
 - [PlayerAdvancedStatsTotal](docs/PlayerAdvancedStatsTotal.md)
 - [PlayerCareer](docs/PlayerCareer.md)
 - [PlayerContractinfo](docs/PlayerContractinfo.md)
 - [PlayerDetails](docs/PlayerDetails.md)
 - [PlayerFixtures](docs/PlayerFixtures.md)
 - [PlayerInjuries](docs/PlayerInjuries.md)
 - [PlayerMatchAdvancedStats](docs/PlayerMatchAdvancedStats.md)
 - [PlayerMatches](docs/PlayerMatches.md)
 - [PlayerTransfer](docs/PlayerTransfer.md)
 - [PlayersFetch](docs/PlayersFetch.md)
 - [PlayersListInner](docs/PlayersListInner.md)
 - [PositionOfThePlayer](docs/PositionOfThePlayer.md)
 - [PossessionDetails](docs/PossessionDetails.md)
 - [PossessionEndLocation](docs/PossessionEndLocation.md)
 - [PossessionStartLocation](docs/PossessionStartLocation.md)
 - [QualityUrl](docs/QualityUrl.md)
 - [Referee](docs/Referee.md)
 - [RelatedTeamsInner](docs/RelatedTeamsInner.md)
 - [Round](docs/Round.md)
 - [RoundData](docs/RoundData.md)
 - [SearchInner](docs/SearchInner.md)
 - [Season](docs/Season.md)
 - [SeasonAssistmen](docs/SeasonAssistmen.md)
 - [SeasonCareer](docs/SeasonCareer.md)
 - [SeasonFixtures](docs/SeasonFixtures.md)
 - [SeasonMatches](docs/SeasonMatches.md)
 - [SeasonPlayers](docs/SeasonPlayers.md)
 - [SeasonScorers](docs/SeasonScorers.md)
 - [SeasonStandings](docs/SeasonStandings.md)
 - [SeasonTeams](docs/SeasonTeams.md)
 - [SeasonTransfers](docs/SeasonTransfers.md)
 - [ShotDetails](docs/ShotDetails.md)
 - [SubstitutionFetch](docs/SubstitutionFetch.md)
 - [Team](docs/Team.md)
 - [TeamAdvancedStats](docs/TeamAdvancedStats.md)
 - [TeamAdvancedStatsAverage](docs/TeamAdvancedStatsAverage.md)
 - [TeamAdvancedStatsPercent](docs/TeamAdvancedStatsPercent.md)
 - [TeamAdvancedStatsTotal](docs/TeamAdvancedStatsTotal.md)
 - [TeamBenchedPlayersInner](docs/TeamBenchedPlayersInner.md)
 - [TeamCareer](docs/TeamCareer.md)
 - [TeamCoach](docs/TeamCoach.md)
 - [TeamDetails](docs/TeamDetails.md)
 - [TeamDetails1](docs/TeamDetails1.md)
 - [TeamFixtures](docs/TeamFixtures.md)
 - [TeamLineupBenchedSubstitutions](docs/TeamLineupBenchedSubstitutions.md)
 - [TeamLineupInner](docs/TeamLineupInner.md)
 - [TeamMatchAdvancedStats](docs/TeamMatchAdvancedStats.md)
 - [TeamMatches](docs/TeamMatches.md)
 - [TeamMatchesMatchesInner](docs/TeamMatchesMatchesInner.md)
 - [TeamSquad](docs/TeamSquad.md)
 - [TeamSubstitutionsInner](docs/TeamSubstitutionsInner.md)
 - [TeamTransfers](docs/TeamTransfers.md)
 - [TeamsDetails](docs/TeamsDetails.md)
 - [TeamsFetch](docs/TeamsFetch.md)
 - [TeamsStandingForTheGroup](docs/TeamsStandingForTheGroup.md)
 - [TheAppliedFiltersSchema](docs/TheAppliedFiltersSchema.md)
 - [TheAvailableFiltersObject](docs/TheAvailableFiltersObject.md)
 - [TheEntranceOfAPlayerAsASubstitute](docs/TheEntranceOfAPlayerAsASubstitute.md)
 - [TheExitOfAPlayerFromTheFieldRedCardsIncluded](docs/TheExitOfAPlayerFromTheFieldRedCardsIncluded.md)
 - [TheFullhdObject](docs/TheFullhdObject.md)
 - [TheHdObject](docs/TheHdObject.md)
 - [TheInjuryObject](docs/TheInjuryObject.md)
 - [TheItemsSchema](docs/TheItemsSchema.md)
 - [TheListOfMatchesInner](docs/TheListOfMatchesInner.md)
 - [TheListOfSeasonInner](docs/TheListOfSeasonInner.md)
 - [TheLqObject](docs/TheLqObject.md)
 - [TheMatchGoalObject](docs/TheMatchGoalObject.md)
 - [TheMatchObject](docs/TheMatchObject.md)
 - [TheMatchesObject](docs/TheMatchesObject.md)
 - [TheMatchesObject1](docs/TheMatchesObject1.md)
 - [TheMatchesObject2](docs/TheMatchesObject2.md)
 - [ThePlayerObject](docs/ThePlayerObject.md)
 - [ThePlayerObject1](docs/ThePlayerObject1.md)
 - [TheRefereeObject](docs/TheRefereeObject.md)
 - [TheResourceObject](docs/TheResourceObject.md)
 - [TheResourceObjectResourceId](docs/TheResourceObjectResourceId.md)
 - [TheSdObject](docs/TheSdObject.md)
 - [TheSeasonMatchObject](docs/TheSeasonMatchObject.md)
 - [TheSubstitutionThatHappenedAtStartSecSecondsElapsedFromTheStart](docs/TheSubstitutionThatHappenedAtStartSecSecondsElapsedFromTheStart.md)
 - [TheSubstitutionsRelatedToMatchPeriodMatchPeriod](docs/TheSubstitutionsRelatedToMatchPeriodMatchPeriod.md)
 - [TheSubstitutionsRelatedToTheTeamWithIDTeamId](docs/TheSubstitutionsRelatedToTheTeamWithIDTeamId.md)
 - [TheTeamCareerArrayInner](docs/TheTeamCareerArrayInner.md)
 - [TheTeamObject](docs/TheTeamObject.md)
 - [TheTeamsData](docs/TheTeamsData.md)
 - [TheTransferObject](docs/TheTransferObject.md)
 - [TheTransferObject1](docs/TheTransferObject1.md)
 - [TheVideoURL](docs/TheVideoURL.md)
 - [UpdatedObjectsDeleted](docs/UpdatedObjectsDeleted.md)
 - [UpdatedObjectsUpdated](docs/UpdatedObjectsUpdated.md)
 - [Video](docs/Video.md)
 - [VideoOffsets](docs/VideoOffsets.md)
 - [VideoQualities](docs/VideoQualities.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




