# openapi_client.EventsApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_wy_id_events_get**](EventsApi.md#matches_wy_id_events_get) | **GET** /matches/{wyId}/events | MatchEvents


# **matches_wy_id_events_get**
> MatchEvents matches_wy_id_events_get(wy_id, fetch=fetch, details=details, exclude=exclude, authorization=authorization)

MatchEvents

Retrieves information about a given match's events

### Example


```python
import openapi_client
from openapi_client.models.match_events import MatchEvents
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
    api_instance = openapi_client.EventsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `teams`, `players`, `match`, `coaches`, `referees`, `formations`, `substitutions` (optional)
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `tag` (optional)
    exclude = 'exclude_example' # str | List of objects to exclude from API output, separated by comma: `possessions`, `names`, `positions`, `formations` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # MatchEvents
        api_response = api_instance.matches_wy_id_events_get(wy_id, fetch=fetch, details=details, exclude=exclude, authorization=authorization)
        print("The response of EventsApi->matches_wy_id_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->matches_wy_id_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;teams&#x60;, &#x60;players&#x60;, &#x60;match&#x60;, &#x60;coaches&#x60;, &#x60;referees&#x60;, &#x60;formations&#x60;, &#x60;substitutions&#x60; | [optional] 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;tag&#x60; | [optional] 
 **exclude** | **str**| List of objects to exclude from API output, separated by comma: &#x60;possessions&#x60;, &#x60;names&#x60;, &#x60;positions&#x60;, &#x60;formations&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**MatchEvents**](MatchEvents.md)

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

