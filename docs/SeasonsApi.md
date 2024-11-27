# openapi_client.SeasonsApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seasons_wy_id_assistmen_get**](SeasonsApi.md#seasons_wy_id_assistmen_get) | **GET** /seasons/{wyId}/assistmen | Season assistmen
[**seasons_wy_id_career_get**](SeasonsApi.md#seasons_wy_id_career_get) | **GET** /seasons/{wyId}/career | Seasons career
[**seasons_wy_id_fixtures_get**](SeasonsApi.md#seasons_wy_id_fixtures_get) | **GET** /seasons/{wyId}/fixtures | Seasons fixtures
[**seasons_wy_id_get**](SeasonsApi.md#seasons_wy_id_get) | **GET** /seasons/{wyId} | Season details
[**seasons_wy_id_matches_get**](SeasonsApi.md#seasons_wy_id_matches_get) | **GET** /seasons/{wyId}/matches | Seasons matches
[**seasons_wy_id_players_get**](SeasonsApi.md#seasons_wy_id_players_get) | **GET** /seasons/{wyId}/players | Seasons players
[**seasons_wy_id_scorers_get**](SeasonsApi.md#seasons_wy_id_scorers_get) | **GET** /seasons/{wyId}/scorers | Season scorers
[**seasons_wy_id_standings_get**](SeasonsApi.md#seasons_wy_id_standings_get) | **GET** /seasons/{wyId}/standings | Seasons standings
[**seasons_wy_id_teams_get**](SeasonsApi.md#seasons_wy_id_teams_get) | **GET** /seasons/{wyId}/teams | Seasons teams
[**seasons_wy_id_transfers_get**](SeasonsApi.md#seasons_wy_id_transfers_get) | **GET** /seasons/{wyId}/transfers | Seasons transfers


# **seasons_wy_id_assistmen_get**
> SeasonAssistmen seasons_wy_id_assistmen_get(wy_id, fetch=fetch, details=details, authorization=authorization)

Season assistmen

Returns info about the given season assistmen

### Example


```python
import openapi_client
from openapi_client.models.season_assistmen import SeasonAssistmen
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `season`, `competition` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `players`, `teams` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Season assistmen
        api_response = api_instance.seasons_wy_id_assistmen_get(wy_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_assistmen_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_assistmen_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;season&#x60;, &#x60;competition&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;players&#x60;, &#x60;teams&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**SeasonAssistmen**](SeasonAssistmen.md)

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

# **seasons_wy_id_career_get**
> SeasonCareer seasons_wy_id_career_get(wy_id, fetch=fetch, details=details, filters=filters, authorization=authorization)

Seasons career

Returns general performance information about all the teams for the given season

### Example


```python
import openapi_client
from openapi_client.models.season_career import SeasonCareer
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition`, `season` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `team`, `round` (optional)
    filters = 'filters_example' # str | <table><thead><tr><th>Object</th><th>Description</th></tr></thead><tbody><tr><td>gameWeek</td><td>If present, it returns standings for that gameweek</td></tr><tr><td>gameWeekInterval</td><td>If present, it returns standings for that gameweeks’ range Use: {\"gameWeekInterval\":{\"startWeek\":7,\"endWeek\":12}}</td></tr></tbody></table> (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Seasons career
        api_response = api_instance.seasons_wy_id_career_get(wy_id, fetch=fetch, details=details, filters=filters, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_career_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_career_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;team&#x60;, &#x60;round&#x60; | [optional] 
 **filters** | **str**| &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Object&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;gameWeek&lt;/td&gt;&lt;td&gt;If present, it returns standings for that gameweek&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gameWeekInterval&lt;/td&gt;&lt;td&gt;If present, it returns standings for that gameweeks’ range Use: {\&quot;gameWeekInterval\&quot;:{\&quot;startWeek\&quot;:7,\&quot;endWeek\&quot;:12}}&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**SeasonCareer**](SeasonCareer.md)

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

# **seasons_wy_id_fixtures_get**
> SeasonFixtures seasons_wy_id_fixtures_get(wy_id, to_date=to_date, fetch=fetch, details=details, from_date=from_date, authorization=authorization)

Seasons fixtures

Retrieves all the matches for the given season

### Example


```python
import openapi_client
from openapi_client.models.season_fixtures import SeasonFixtures
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    to_date = 'to_date_example' # str | Ending date in YYYY-MM-DD format (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `season` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `matches`, `players`, `teams` (optional)
    from_date = 'from_date_example' # str | Starting date in YYYY-MM-DD format (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Seasons fixtures
        api_response = api_instance.seasons_wy_id_fixtures_get(wy_id, to_date=to_date, fetch=fetch, details=details, from_date=from_date, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_fixtures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_fixtures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **to_date** | **str**| Ending date in YYYY-MM-DD format | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;season&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;matches&#x60;, &#x60;players&#x60;, &#x60;teams&#x60; | [optional] 
 **from_date** | **str**| Starting date in YYYY-MM-DD format | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**SeasonFixtures**](SeasonFixtures.md)

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

# **seasons_wy_id_get**
> Season seasons_wy_id_get(wy_id, details=details, authorization=authorization)

Season details

Returns info about the given season

### Example


```python
import openapi_client
from openapi_client.models.season import Season
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `competition` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Season details
        api_response = api_instance.seasons_wy_id_get(wy_id, details=details, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;competition&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Season**](Season.md)

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

# **seasons_wy_id_matches_get**
> SeasonMatches seasons_wy_id_matches_get(wy_id, fetch=fetch, authorization=authorization)

Seasons matches

Returns the list of matches played in the given season

### Example


```python
import openapi_client
from openapi_client.models.season_matches import SeasonMatches
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `season` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Seasons matches
        api_response = api_instance.seasons_wy_id_matches_get(wy_id, fetch=fetch, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_matches_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_matches_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;season&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**SeasonMatches**](SeasonMatches.md)

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

# **seasons_wy_id_players_get**
> SeasonPlayers seasons_wy_id_players_get(wy_id, count=count, limit=limit, sort=sort, authorization=authorization, fetch=fetch, page=page, search=search, details=details, filter=filter)

Seasons players

Returns the list of players who have played in the given season

### Example


```python
import openapi_client
from openapi_client.models.season_players import SeasonPlayers
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    count = 'count_example' # str | Alias for limit argument (optional)
    limit = 'limit_example' # str | Allows to change the number of results for page (limited to max 100 results for single page) (optional)
    sort = 'sort_example' # str | Allows to sort resultset by given field and directions (optional)
    authorization = 'authorization_example' # str |  (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `season` (optional)
    page = 'page_example' # str | Allows to change page (current page) from which the results are fetched (optional)
    search = 'search_example' # str | Allows to simple search and filter resultset by OR condition among defined search fields (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `currentTeam` (optional)
    filter = 'filter_example' # str | Allows to simple filter resultset by AND and EQUAL condition on given field (optional)

    try:
        # Seasons players
        api_response = api_instance.seasons_wy_id_players_get(wy_id, count=count, limit=limit, sort=sort, authorization=authorization, fetch=fetch, page=page, search=search, details=details, filter=filter)
        print("The response of SeasonsApi->seasons_wy_id_players_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_players_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **count** | **str**| Alias for limit argument | [optional] 
 **limit** | **str**| Allows to change the number of results for page (limited to max 100 results for single page) | [optional] 
 **sort** | **str**| Allows to sort resultset by given field and directions | [optional] 
 **authorization** | **str**|  | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;season&#x60; | [optional] 
 **page** | **str**| Allows to change page (current page) from which the results are fetched | [optional] 
 **search** | **str**| Allows to simple search and filter resultset by OR condition among defined search fields | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;currentTeam&#x60; | [optional] 
 **filter** | **str**| Allows to simple filter resultset by AND and EQUAL condition on given field | [optional] 

### Return type

[**SeasonPlayers**](SeasonPlayers.md)

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

# **seasons_wy_id_scorers_get**
> SeasonScorers seasons_wy_id_scorers_get(wy_id, fetch=fetch, details=details, authorization=authorization)

Season scorers

Returns info about the given season scorers

### Example


```python
import openapi_client
from openapi_client.models.season_scorers import SeasonScorers
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `season`, `competition` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `players`, `teams` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Season scorers
        api_response = api_instance.seasons_wy_id_scorers_get(wy_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_scorers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_scorers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;season&#x60;, &#x60;competition&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;players&#x60;, &#x60;teams&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**SeasonScorers**](SeasonScorers.md)

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

# **seasons_wy_id_standings_get**
> SeasonStandings seasons_wy_id_standings_get(wy_id, round_id=round_id, fetch=fetch, details=details, authorization=authorization)

Seasons standings

Returns the standings for the given season

### Example


```python
import openapi_client
from openapi_client.models.season_standings import SeasonStandings
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    round_id = 'round_id_example' # str | Relevant round id (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `competition`, `season` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `teams` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Seasons standings
        api_response = api_instance.seasons_wy_id_standings_get(wy_id, round_id=round_id, fetch=fetch, details=details, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_standings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_standings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **round_id** | **str**| Relevant round id | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;teams&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**SeasonStandings**](SeasonStandings.md)

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

# **seasons_wy_id_teams_get**
> SeasonTeams seasons_wy_id_teams_get(wy_id, fetch=fetch, authorization=authorization)

Seasons teams

Returns the list of teams in the given season. Please note: the call returns only the teams that already played at least one match in the season.

### Example


```python
import openapi_client
from openapi_client.models.season_teams import SeasonTeams
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `season` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Seasons teams
        api_response = api_instance.seasons_wy_id_teams_get(wy_id, fetch=fetch, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_teams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_teams_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;season&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**SeasonTeams**](SeasonTeams.md)

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

# **seasons_wy_id_transfers_get**
> SeasonTransfers seasons_wy_id_transfers_get(wy_id, to_date=to_date, details=details, from_date=from_date, authorization=authorization)

Seasons transfers

Retrieves all the transfer's information for the given season

### Example


```python
import openapi_client
from openapi_client.models.season_transfers import SeasonTransfers
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
    api_instance = openapi_client.SeasonsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    to_date = 'to_date_example' # str | Ending date in YYYY-MM-DD format (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `teams`, `player` (optional)
    from_date = 'from_date_example' # str | Starting date in YYYY-MM-DD format (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Seasons transfers
        api_response = api_instance.seasons_wy_id_transfers_get(wy_id, to_date=to_date, details=details, from_date=from_date, authorization=authorization)
        print("The response of SeasonsApi->seasons_wy_id_transfers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->seasons_wy_id_transfers_get: %s\n" % e)
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

[**SeasonTransfers**](SeasonTransfers.md)

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

