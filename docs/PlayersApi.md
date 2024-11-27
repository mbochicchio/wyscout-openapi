# openapi_client.PlayersApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_wy_id_career_get**](PlayersApi.md#players_wy_id_career_get) | **GET** /players/{wyId}/career | Players career
[**players_wy_id_contractinfo_get**](PlayersApi.md#players_wy_id_contractinfo_get) | **GET** /players/{wyId}/contractinfo | Players contract info
[**players_wy_id_fixtures_get**](PlayersApi.md#players_wy_id_fixtures_get) | **GET** /players/{wyId}/fixtures | Players fixtures
[**players_wy_id_get**](PlayersApi.md#players_wy_id_get) | **GET** /players/{wyId} | Player details
[**players_wy_id_matches_get**](PlayersApi.md#players_wy_id_matches_get) | **GET** /players/{wyId}/matches | Players matches
[**players_wy_id_transfers_get**](PlayersApi.md#players_wy_id_transfers_get) | **GET** /players/{wyId}/transfers | Players transfers


# **players_wy_id_career_get**
> PlayerCareer players_wy_id_career_get(wy_id, fetch=fetch, details=details, authorization=authorization)

Players career

Returns info about the given player career

### Example


```python
import openapi_client
from openapi_client.models.player_career import PlayerCareer
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
    api_instance = openapi_client.PlayersApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `player` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `team`, `competition`, `season` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Players career
        api_response = api_instance.players_wy_id_career_get(wy_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of PlayersApi->players_wy_id_career_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->players_wy_id_career_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;player&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;team&#x60;, &#x60;competition&#x60;, &#x60;season&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PlayerCareer**](PlayerCareer.md)

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

# **players_wy_id_contractinfo_get**
> PlayerContractinfo players_wy_id_contractinfo_get(wy_id, fetch=fetch, authorization=authorization)

Players contract info

Returns info about the given player contract

### Example


```python
import openapi_client
from openapi_client.models.player_contractinfo import PlayerContractinfo
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
    api_instance = openapi_client.PlayersApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `player` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Players contract info
        api_response = api_instance.players_wy_id_contractinfo_get(wy_id, fetch=fetch, authorization=authorization)
        print("The response of PlayersApi->players_wy_id_contractinfo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->players_wy_id_contractinfo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;player&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PlayerContractinfo**](PlayerContractinfo.md)

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

# **players_wy_id_fixtures_get**
> PlayerFixtures players_wy_id_fixtures_get(wy_id, to_date=to_date, from_date=from_date, authorization=authorization)

Players fixtures

Returns info about the given player matches fixtures

### Example


```python
import openapi_client
from openapi_client.models.player_fixtures import PlayerFixtures
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
    api_instance = openapi_client.PlayersApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    to_date = 'to_date_example' # str | Ending date in YYYY-MM-DD format (optional)
    from_date = 'from_date_example' # str | Starting date in YYYY-MM-DD format (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Players fixtures
        api_response = api_instance.players_wy_id_fixtures_get(wy_id, to_date=to_date, from_date=from_date, authorization=authorization)
        print("The response of PlayersApi->players_wy_id_fixtures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->players_wy_id_fixtures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **to_date** | **str**| Ending date in YYYY-MM-DD format | [optional] 
 **from_date** | **str**| Starting date in YYYY-MM-DD format | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PlayerFixtures**](PlayerFixtures.md)

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

# **players_wy_id_get**
> Player players_wy_id_get(wy_id, details=details, authorization=authorization)

Player details

Returns info about the given player

### Example


```python
import openapi_client
from openapi_client.models.player import Player
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
    api_instance = openapi_client.PlayersApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `currentTeam` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Player details
        api_response = api_instance.players_wy_id_get(wy_id, details=details, authorization=authorization)
        print("The response of PlayersApi->players_wy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->players_wy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;currentTeam&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Player**](Player.md)

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

# **players_wy_id_matches_get**
> PlayerMatches players_wy_id_matches_get(wy_id, season_id=season_id, fetch=fetch, authorization=authorization)

Players matches

Returns info about the given player matches

### Example


```python
import openapi_client
from openapi_client.models.player_matches import PlayerMatches
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
    api_instance = openapi_client.PlayersApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    season_id = 'season_id_example' # str | Relevant season id (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `player` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Players matches
        api_response = api_instance.players_wy_id_matches_get(wy_id, season_id=season_id, fetch=fetch, authorization=authorization)
        print("The response of PlayersApi->players_wy_id_matches_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->players_wy_id_matches_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **season_id** | **str**| Relevant season id | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;player&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PlayerMatches**](PlayerMatches.md)

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

# **players_wy_id_transfers_get**
> PlayerTransfer players_wy_id_transfers_get(wy_id, fetch=fetch, alternative=alternative, details=details, authorization=authorization)

Players transfers

Returns info about the given player transfers

### Example


```python
import openapi_client
from openapi_client.models.player_transfer import PlayerTransfer
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
    api_instance = openapi_client.PlayersApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `player` (optional)
    alternative = 'alternative_example' # str |  (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `teams` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Players transfers
        api_response = api_instance.players_wy_id_transfers_get(wy_id, fetch=fetch, alternative=alternative, details=details, authorization=authorization)
        print("The response of PlayersApi->players_wy_id_transfers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->players_wy_id_transfers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;player&#x60; | [optional] 
 **alternative** | **str**|  | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;teams&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PlayerTransfer**](PlayerTransfer.md)

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

