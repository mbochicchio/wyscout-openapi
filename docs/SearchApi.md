# openapi_client.SearchApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](SearchApi.md#search_get) | **GET** /search | Search


# **search_get**
> List[SearchInner] search_get(query, obj_type, gender=gender, authorization=authorization)

Search

Returns a list of objects, matching the provided search string

### Example


```python
import openapi_client
from openapi_client.models.search_inner import SearchInner
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
    api_instance = openapi_client.SearchApi(api_client)
    query = 'query_example' # str | The string to be matched with the resource's name
    obj_type = 'obj_type_example' # str | Object to be retrieved (only the first type is considered): `competition`, `team`, `player`, `referee`
    gender = 'gender_example' # str | Object to be retrieved (only the first type is considered): `men`, `women` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Search
        api_response = api_instance.search_get(query, obj_type, gender=gender, authorization=authorization)
        print("The response of SearchApi->search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The string to be matched with the resource&#39;s name | 
 **obj_type** | **str**| Object to be retrieved (only the first type is considered): &#x60;competition&#x60;, &#x60;team&#x60;, &#x60;player&#x60;, &#x60;referee&#x60; | 
 **gender** | **str**| Object to be retrieved (only the first type is considered): &#x60;men&#x60;, &#x60;women&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**List[SearchInner]**](SearchInner.md)

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

