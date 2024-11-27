# openapi_client.TeamsApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_wy_id_career_get**](TeamsApi.md#teams_wy_id_career_get) | **GET** /teams/{wyId}/career | Team careers
[**teams_wy_id_fixtures_get**](TeamsApi.md#teams_wy_id_fixtures_get) | **GET** /teams/{wyId}/fixtures | Teams fixtures
[**teams_wy_id_get**](TeamsApi.md#teams_wy_id_get) | **GET** /teams/{wyId} | Team details
[**teams_wy_id_matches_get**](TeamsApi.md#teams_wy_id_matches_get) | **GET** /teams/{wyId}/matches | Teams matches
[**teams_wy_id_squad_get**](TeamsApi.md#teams_wy_id_squad_get) | **GET** /teams/{wyId}/squad | Teams squad
[**teams_wy_id_transfers_get**](TeamsApi.md#teams_wy_id_transfers_get) | **GET** /teams/{wyId}/transfers | Teams transfers


# **teams_wy_id_career_get**
> TeamCareer teams_wy_id_career_get(wy_id, fetch=fetch, details=details, authorization=authorization)

Team careers

Returns all the team career information

### Example


```python
import openapi_client
from openapi_client.models.team_career import TeamCareer
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
    api_instance = openapi_client.TeamsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `team` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `season`, `competition` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Team careers
        api_response = api_instance.teams_wy_id_career_get(wy_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of TeamsApi->teams_wy_id_career_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_wy_id_career_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;team&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;season&#x60;, &#x60;competition&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TeamCareer**](TeamCareer.md)

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

# **teams_wy_id_fixtures_get**
> TeamFixtures teams_wy_id_fixtures_get(wy_id, to_date=to_date, from_date=from_date, authorization=authorization)

Teams fixtures

Retrieves all the fixtures matches for the given team.

### Example


```python
import openapi_client
from openapi_client.models.team_fixtures import TeamFixtures
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
    api_instance = openapi_client.TeamsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    to_date = 'to_date_example' # str | Ending date in YYYY-MM-DD format (optional)
    from_date = 'from_date_example' # str | Starting date in YYYY-MM-DD format (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Teams fixtures
        api_response = api_instance.teams_wy_id_fixtures_get(wy_id, to_date=to_date, from_date=from_date, authorization=authorization)
        print("The response of TeamsApi->teams_wy_id_fixtures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_wy_id_fixtures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **to_date** | **str**| Ending date in YYYY-MM-DD format | [optional] 
 **from_date** | **str**| Starting date in YYYY-MM-DD format | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TeamFixtures**](TeamFixtures.md)

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

# **teams_wy_id_get**
> Team teams_wy_id_get(wy_id, authorization=authorization)

Team details

Returns info about the given team

### Example


```python
import openapi_client
from openapi_client.models.team import Team
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
    api_instance = openapi_client.TeamsApi(api_client)
    wy_id = 'wy_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Team details
        api_response = api_instance.teams_wy_id_get(wy_id, authorization=authorization)
        print("The response of TeamsApi->teams_wy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_wy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**Team**](Team.md)

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

# **teams_wy_id_matches_get**
> TeamMatches teams_wy_id_matches_get(wy_id, season_id=season_id, fetch=fetch, authorization=authorization)

Teams matches

Returns the list of matches played by the given team

### Example


```python
import openapi_client
from openapi_client.models.team_matches import TeamMatches
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
    api_instance = openapi_client.TeamsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    season_id = 'season_id_example' # str | Relevant season id (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `team` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Teams matches
        api_response = api_instance.teams_wy_id_matches_get(wy_id, season_id=season_id, fetch=fetch, authorization=authorization)
        print("The response of TeamsApi->teams_wy_id_matches_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_wy_id_matches_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **season_id** | **str**| Relevant season id | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;team&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TeamMatches**](TeamMatches.md)

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

# **teams_wy_id_squad_get**
> TeamSquad teams_wy_id_squad_get(wy_id, season_id=season_id, fetch=fetch, authorization=authorization)

Teams squad

Returns the list of players currently playing for the given team

### Example


```python
import openapi_client
from openapi_client.models.team_squad import TeamSquad
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
    api_instance = openapi_client.TeamsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    season_id = 'season_id_example' # str | Relevant season id (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `team` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Teams squad
        api_response = api_instance.teams_wy_id_squad_get(wy_id, season_id=season_id, fetch=fetch, authorization=authorization)
        print("The response of TeamsApi->teams_wy_id_squad_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_wy_id_squad_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **season_id** | **str**| Relevant season id | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;team&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TeamSquad**](TeamSquad.md)

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

# **teams_wy_id_transfers_get**
> TeamTransfers teams_wy_id_transfers_get(wy_id, to_date=to_date, details=details, from_date=from_date, authorization=authorization)

Teams transfers

Retrieves all the transfer's information for the given team

### Example


```python
import openapi_client
from openapi_client.models.team_transfers import TeamTransfers
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
    api_instance = openapi_client.TeamsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    to_date = 'to_date_example' # str | Ending date in YYYY-MM-DD format (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `teams`, `player` (optional)
    from_date = 'from_date_example' # str | Starting date in YYYY-MM-DD format (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Teams transfers
        api_response = api_instance.teams_wy_id_transfers_get(wy_id, to_date=to_date, details=details, from_date=from_date, authorization=authorization)
        print("The response of TeamsApi->teams_wy_id_transfers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_wy_id_transfers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **to_date** | **str**| Ending date in YYYY-MM-DD format | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;teams&#x60;, &#x60;player&#x60; | [optional] 
 **from_date** | **str**| Starting date in YYYY-MM-DD format | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TeamTransfers**](TeamTransfers.md)

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

