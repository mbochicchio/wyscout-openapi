# openapi_client.AdvancedStatsApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_wy_id_advancedstats_get**](AdvancedStatsApi.md#matches_wy_id_advancedstats_get) | **GET** /matches/{wyId}/advancedstats | Match Advanced Stats
[**matches_wy_id_advancedstats_players_get**](AdvancedStatsApi.md#matches_wy_id_advancedstats_players_get) | **GET** /matches/{wyId}/advancedstats/players | All players Match Advanced Stats
[**players_wy_id_advancedstats_get**](AdvancedStatsApi.md#players_wy_id_advancedstats_get) | **GET** /players/{wyId}/advancedstats | Player Advanced Stats
[**players_wy_id_matches_match_wy_id_advancedstats_get**](AdvancedStatsApi.md#players_wy_id_matches_match_wy_id_advancedstats_get) | **GET** /players/{wyId}/matches/{matchWyId}/advancedstats | Players match advanced stats
[**teams_wy_id_advancedstats_get**](AdvancedStatsApi.md#teams_wy_id_advancedstats_get) | **GET** /teams/{wyId}/advancedstats | Teams Advanced Stats
[**teams_wy_id_matches_match_wy_id_advancedstats_get**](AdvancedStatsApi.md#teams_wy_id_matches_match_wy_id_advancedstats_get) | **GET** /teams/{wyId}/matches/{matchWyId}/advancedstats | Teams match advanced stats


# **matches_wy_id_advancedstats_get**
> MatchAdvancedStats matches_wy_id_advancedstats_get(wy_id, use_sides=use_sides, details=details, authorization=authorization)

Match Advanced Stats

Returns advanced statistics of a given match

### Example


```python
import openapi_client
from openapi_client.models.match_advanced_stats import MatchAdvancedStats
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
    except Exception as e:
        print("Exception when calling AdvancedStatsApi->matches_wy_id_advancedstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **use_sides** | **str**| Flag to change label (&lt;teamId&gt; –&gt; home or &lt;teamId&gt; –&gt; away) | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;teams&#x60;, &#x60;match&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**MatchAdvancedStats**](MatchAdvancedStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Content-Type -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_wy_id_advancedstats_players_get**
> MatchPlayersAdvancedStats matches_wy_id_advancedstats_players_get(wy_id, fetch=fetch, details=details, authorization=authorization)

All players Match Advanced Stats

Returns advanced statistics of all players in a specific match

### Example


```python
import openapi_client
from openapi_client.models.match_players_advanced_stats import MatchPlayersAdvancedStats
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
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition`, `season`, `round`, `match` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `player` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # All players Match Advanced Stats
        api_response = api_instance.matches_wy_id_advancedstats_players_get(wy_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of AdvancedStatsApi->matches_wy_id_advancedstats_players_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedStatsApi->matches_wy_id_advancedstats_players_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60;, &#x60;round&#x60;, &#x60;match&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;player&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**MatchPlayersAdvancedStats**](MatchPlayersAdvancedStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Content-Type -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_wy_id_advancedstats_get**
> PlayerAdvancedStats players_wy_id_advancedstats_get(comp_id, wy_id, round_id=round_id, match_day=match_day, authorization=authorization, season_id=season_id, fetch=fetch, details=details)

Player Advanced Stats

Returns advanced statistics of a given player in a specific competition season. Overall, the statistics provided are relative to the selected season, and not to a specific team. By default the season is set to the current one

### Example


```python
import openapi_client
from openapi_client.models.player_advanced_stats import PlayerAdvancedStats
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
    comp_id = 'comp_id_example' # str | Competition wyId
    wy_id = 'wy_id_example' # str | Relevant content id
    round_id = 'round_id_example' # str | Relevant round id (optional)
    match_day = 'match_day_example' # str | If present, only match data for a single day are returned (optional)
    authorization = 'authorization_example' # str |  (optional)
    season_id = 'season_id_example' # str | Relevant season id (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition`, `season`, `round` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `player` (optional)

    try:
        # Player Advanced Stats
        api_response = api_instance.players_wy_id_advancedstats_get(comp_id, wy_id, round_id=round_id, match_day=match_day, authorization=authorization, season_id=season_id, fetch=fetch, details=details)
        print("The response of AdvancedStatsApi->players_wy_id_advancedstats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedStatsApi->players_wy_id_advancedstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comp_id** | **str**| Competition wyId | 
 **wy_id** | **str**| Relevant content id | 
 **round_id** | **str**| Relevant round id | [optional] 
 **match_day** | **str**| If present, only match data for a single day are returned | [optional] 
 **authorization** | **str**|  | [optional] 
 **season_id** | **str**| Relevant season id | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60;, &#x60;round&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;player&#x60; | [optional] 

### Return type

[**PlayerAdvancedStats**](PlayerAdvancedStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Content-Type -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_wy_id_matches_match_wy_id_advancedstats_get**
> PlayerMatchAdvancedStats players_wy_id_matches_match_wy_id_advancedstats_get(wy_id, match_wy_id, fetch=fetch, details=details, authorization=authorization)

Players match advanced stats

Returns advanced statistics of a given player in a specific match

### Example


```python
import openapi_client
from openapi_client.models.player_match_advanced_stats import PlayerMatchAdvancedStats
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
    match_wy_id = 'match_wy_id_example' # str | Relevant match id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition`, `season`, `round`, `match` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `player` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Players match advanced stats
        api_response = api_instance.players_wy_id_matches_match_wy_id_advancedstats_get(wy_id, match_wy_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of AdvancedStatsApi->players_wy_id_matches_match_wy_id_advancedstats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedStatsApi->players_wy_id_matches_match_wy_id_advancedstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **match_wy_id** | **str**| Relevant match id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60;, &#x60;round&#x60;, &#x60;match&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;player&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PlayerMatchAdvancedStats**](PlayerMatchAdvancedStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Content-Type -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_wy_id_advancedstats_get**
> TeamAdvancedStats teams_wy_id_advancedstats_get(comp_id, wy_id, round_id=round_id, match_day=match_day, authorization=authorization, season_id=season_id, fetch=fetch, details=details)

Teams Advanced Stats

Returns advanced statistics of a given team in a specific competition season. By default the season is set to the current one.

### Example


```python
import openapi_client
from openapi_client.models.team_advanced_stats import TeamAdvancedStats
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
    comp_id = 'comp_id_example' # str | Competition wyId
    wy_id = 'wy_id_example' # str | Relevant content id
    round_id = 'round_id_example' # str | Relevant round id (optional)
    match_day = 'match_day_example' # str | If present, only match data for a single day are returned (optional)
    authorization = 'authorization_example' # str |  (optional)
    season_id = 'season_id_example' # str | Relevant season id (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition`, `season`, `round` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `team` (optional)

    try:
        # Teams Advanced Stats
        api_response = api_instance.teams_wy_id_advancedstats_get(comp_id, wy_id, round_id=round_id, match_day=match_day, authorization=authorization, season_id=season_id, fetch=fetch, details=details)
        print("The response of AdvancedStatsApi->teams_wy_id_advancedstats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedStatsApi->teams_wy_id_advancedstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comp_id** | **str**| Competition wyId | 
 **wy_id** | **str**| Relevant content id | 
 **round_id** | **str**| Relevant round id | [optional] 
 **match_day** | **str**| If present, only match data for a single day are returned | [optional] 
 **authorization** | **str**|  | [optional] 
 **season_id** | **str**| Relevant season id | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60;, &#x60;round&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;team&#x60; | [optional] 

### Return type

[**TeamAdvancedStats**](TeamAdvancedStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_wy_id_matches_match_wy_id_advancedstats_get**
> TeamMatchAdvancedStats teams_wy_id_matches_match_wy_id_advancedstats_get(wy_id, match_wy_id, fetch=fetch, details=details, authorization=authorization)

Teams match advanced stats

Retrieves information about a given match's statistics

### Example


```python
import openapi_client
from openapi_client.models.team_match_advanced_stats import TeamMatchAdvancedStats
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
    match_wy_id = 'match_wy_id_example' # str | Relevant match id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition`, `season`, `round` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `team` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Teams match advanced stats
        api_response = api_instance.teams_wy_id_matches_match_wy_id_advancedstats_get(wy_id, match_wy_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of AdvancedStatsApi->teams_wy_id_matches_match_wy_id_advancedstats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedStatsApi->teams_wy_id_matches_match_wy_id_advancedstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **match_wy_id** | **str**| Relevant match id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60;, &#x60;round&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;team&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TeamMatchAdvancedStats**](TeamMatchAdvancedStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Content-Type -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

