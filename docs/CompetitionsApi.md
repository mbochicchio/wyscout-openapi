# openapi_client.CompetitionsApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**competitions_get**](CompetitionsApi.md#competitions_get) | **GET** /competitions | Competitions list
[**competitions_wy_id_get**](CompetitionsApi.md#competitions_wy_id_get) | **GET** /competitions/{wyId} | Competition detail
[**competitions_wy_id_matches_get**](CompetitionsApi.md#competitions_wy_id_matches_get) | **GET** /competitions/{wyId}/matches | Matches list
[**competitions_wy_id_players_get**](CompetitionsApi.md#competitions_wy_id_players_get) | **GET** /competitions/{wyId}/players | Players list
[**competitions_wy_id_seasons_get**](CompetitionsApi.md#competitions_wy_id_seasons_get) | **GET** /competitions/{wyId}/seasons | Seasons list
[**competitions_wy_id_teams_get**](CompetitionsApi.md#competitions_wy_id_teams_get) | **GET** /competitions/{wyId}/teams | Teams list


# **competitions_get**
> Competitions competitions_get(area_id, authorization=authorization)

Competitions list

Returns a list of competitions for a given area

### Example


```python
import openapi_client
from openapi_client.models.competitions import Competitions
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
    api_instance = openapi_client.CompetitionsApi(api_client)
    area_id = 'area_id_example' # str | Area three-letters code
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Competitions list
        api_response = api_instance.competitions_get(area_id, authorization=authorization)
        print("The response of CompetitionsApi->competitions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionsApi->competitions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_id** | **str**| Area three-letters code | 
 **authorization** | **str**|  | [optional] 

### Return type

[**Competitions**](Competitions.md)

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

# **competitions_wy_id_get**
> Competition competitions_wy_id_get(wy_id, authorization=authorization)

Competition detail

Returns info about the given competition

### Example


```python
import openapi_client
from openapi_client.models.competition import Competition
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
    api_instance = openapi_client.CompetitionsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Competition detail
        api_response = api_instance.competitions_wy_id_get(wy_id, authorization=authorization)
        print("The response of CompetitionsApi->competitions_wy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionsApi->competitions_wy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **authorization** | **str**|  | [optional] 

### Return type

[**Competition**](Competition.md)

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

# **competitions_wy_id_matches_get**
> CompetitionMatches competitions_wy_id_matches_get(wy_id, fetch=fetch, authorization=authorization)

Matches list

Returns the list of matches of the given competition

### Example


```python
import openapi_client
from openapi_client.models.competition_matches import CompetitionMatches
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
    api_instance = openapi_client.CompetitionsApi(api_client)
    wy_id = 'wy_id_example' # str | Competition wyId
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Matches list
        api_response = api_instance.competitions_wy_id_matches_get(wy_id, fetch=fetch, authorization=authorization)
        print("The response of CompetitionsApi->competitions_wy_id_matches_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionsApi->competitions_wy_id_matches_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Competition wyId | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CompetitionMatches**](CompetitionMatches.md)

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

# **competitions_wy_id_players_get**
> CompetitionPlayers competitions_wy_id_players_get(wy_id, count=count, limit=limit, sort=sort, authorization=authorization, fetch=fetch, page=page, search=search, details=details, filter=filter)

Players list

Returns the list of players of the given competition

### Example


```python
import openapi_client
from openapi_client.models.competition_players import CompetitionPlayers
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
    api_instance = openapi_client.CompetitionsApi(api_client)
    wy_id = 'wy_id_example' # str | Competition wyId
    count = 'count_example' # str | Alias for limit argument (optional)
    limit = 'limit_example' # str | Allows to change the number of results for page (limited to max 100 results for single page) (optional)
    sort = 'sort_example' # str | Allows to sort resultset by given field and directions (optional)
    authorization = 'authorization_example' # str |  (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition` (optional)
    page = 'page_example' # str | Allows to change page (current page) from which the results are fetched (optional)
    search = 'search_example' # str | Allows to simple search and filter resultset by OR condition among defined search fields (optional)
    details = 'details_example' # str |  (optional)
    filter = 'filter_example' # str | Allows to simple filter resultset by AND and EQUAL condition on given field (optional)

    try:
        # Players list
        api_response = api_instance.competitions_wy_id_players_get(wy_id, count=count, limit=limit, sort=sort, authorization=authorization, fetch=fetch, page=page, search=search, details=details, filter=filter)
        print("The response of CompetitionsApi->competitions_wy_id_players_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionsApi->competitions_wy_id_players_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Competition wyId | 
 **count** | **str**| Alias for limit argument | [optional] 
 **limit** | **str**| Allows to change the number of results for page (limited to max 100 results for single page) | [optional] 
 **sort** | **str**| Allows to sort resultset by given field and directions | [optional] 
 **authorization** | **str**|  | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60; | [optional] 
 **page** | **str**| Allows to change page (current page) from which the results are fetched | [optional] 
 **search** | **str**| Allows to simple search and filter resultset by OR condition among defined search fields | [optional] 
 **details** | **str**|  | [optional] 
 **filter** | **str**| Allows to simple filter resultset by AND and EQUAL condition on given field | [optional] 

### Return type

[**CompetitionPlayers**](CompetitionPlayers.md)

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

# **competitions_wy_id_seasons_get**
> CompetitionSeasons competitions_wy_id_seasons_get(wy_id, fetch=fetch, active=active, authorization=authorization)

Seasons list

Returns the list of seasons of the given competition

### Example


```python
import openapi_client
from openapi_client.models.competition_seasons import CompetitionSeasons
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
    api_instance = openapi_client.CompetitionsApi(api_client)
    wy_id = 'wy_id_example' # str | Competition wyId
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition` (optional)
    active = 'active_example' # str | Flag to retrieve only active objects (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Seasons list
        api_response = api_instance.competitions_wy_id_seasons_get(wy_id, fetch=fetch, active=active, authorization=authorization)
        print("The response of CompetitionsApi->competitions_wy_id_seasons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionsApi->competitions_wy_id_seasons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Competition wyId | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60; | [optional] 
 **active** | **str**| Flag to retrieve only active objects | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CompetitionSeasons**](CompetitionSeasons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Headers -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Length -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_wy_id_teams_get**
> CompetitionTeams competitions_wy_id_teams_get(wy_id, fetch=fetch, authorization=authorization)

Teams list

Returns the list of teams of the given competition

### Example


```python
import openapi_client
from openapi_client.models.competition_teams import CompetitionTeams
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
    api_instance = openapi_client.CompetitionsApi(api_client)
    wy_id = 'wy_id_example' # str | Competition wyId
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Teams list
        api_response = api_instance.competitions_wy_id_teams_get(wy_id, fetch=fetch, authorization=authorization)
        print("The response of CompetitionsApi->competitions_wy_id_teams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionsApi->competitions_wy_id_teams_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Competition wyId | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CompetitionTeams**](CompetitionTeams.md)

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

