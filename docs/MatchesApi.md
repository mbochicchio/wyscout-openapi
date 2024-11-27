# openapi_client.MatchesApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_wy_id_directions_get**](MatchesApi.md#matches_wy_id_directions_get) | **GET** /matches/{wyId}/directions | Match directions
[**matches_wy_id_formations_get**](MatchesApi.md#matches_wy_id_formations_get) | **GET** /matches/{wyId}/formations | Match formations
[**matches_wy_id_get**](MatchesApi.md#matches_wy_id_get) | **GET** /matches/{wyId} | Match detail


# **matches_wy_id_directions_get**
> MatchDirections matches_wy_id_directions_get(wy_id, authorization=authorization)

Match directions

Shows the direction of attack of both teams in each half of the game. With this information you can know the direction in which both teams are playing in each period of the match, which are:<ul><li>1st half</li><li>2nd half</li><li>1st half extra time</li><li>2nd half extra time</li></ul>

### Example


```python
import openapi_client
from openapi_client.models.match_directions import MatchDirections
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
    api_instance = openapi_client.MatchesApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Match directions
        api_response = api_instance.matches_wy_id_directions_get(wy_id, authorization=authorization)
        print("The response of MatchesApi->matches_wy_id_directions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_wy_id_directions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **authorization** | **str**|  | [optional] 

### Return type

[**MatchDirections**](MatchDirections.md)

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

# **matches_wy_id_formations_get**
> MatchFormations matches_wy_id_formations_get(wy_id, details=details, authorization=authorization)

Match formations

Retrieves information about a given match's formations

### Example


```python
import openapi_client
from openapi_client.models.match_formations import MatchFormations
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
    api_instance = openapi_client.MatchesApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `teams`, `players` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Match formations
        api_response = api_instance.matches_wy_id_formations_get(wy_id, details=details, authorization=authorization)
        print("The response of MatchesApi->matches_wy_id_formations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_wy_id_formations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;teams&#x60;, &#x60;players&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**MatchFormations**](MatchFormations.md)

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

# **matches_wy_id_get**
> Match matches_wy_id_get(wy_id, use_sides=use_sides, details=details, authorization=authorization)

Match detail

Returns info about the given match

### Example


```python
import openapi_client
from openapi_client.models.match import Match
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
    api_instance = openapi_client.MatchesApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    use_sides = 'use_sides_example' # str | Flag to change label (teamId –> home or teamId –> away) (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `coaches`, `players`, `teams`, `competition`, `round`, `season` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Match detail
        api_response = api_instance.matches_wy_id_get(wy_id, use_sides=use_sides, details=details, authorization=authorization)
        print("The response of MatchesApi->matches_wy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->matches_wy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **use_sides** | **str**| Flag to change label (teamId –&gt; home or teamId –&gt; away) | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;coaches&#x60;, &#x60;players&#x60;, &#x60;teams&#x60;, &#x60;competition&#x60;, &#x60;round&#x60;, &#x60;season&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Match**](Match.md)

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

