# openapi_client.RoundsApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rounds_wy_id_get**](RoundsApi.md#rounds_wy_id_get) | **GET** /rounds/{wyId} | Rounds


# **rounds_wy_id_get**
> Round rounds_wy_id_get(wy_id, details=details, authorization=authorization)

Rounds

Returns info about the given round

### Example


```python
import openapi_client
from openapi_client.models.round import Round
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
    api_instance = openapi_client.RoundsApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    details = 'details_example' # str | List of related objects to be detailed, separated by comma: `competition`, `season` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Rounds
        api_response = api_instance.rounds_wy_id_get(wy_id, details=details, authorization=authorization)
        print("The response of RoundsApi->rounds_wy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundsApi->rounds_wy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **details** | **str**| List of related objects to be detailed, separated by comma: &#x60;competition&#x60;, &#x60;season&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Round**](Round.md)

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

