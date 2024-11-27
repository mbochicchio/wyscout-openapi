# openapi_client.TrackingApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_wy_id_fulltracking_get**](TrackingApi.md#matches_wy_id_fulltracking_get) | **GET** /matches/{wyId}/fulltracking | Broadcast tracking
[**matches_wy_id_physicaldata_get**](TrackingApi.md#matches_wy_id_physicaldata_get) | **GET** /matches/{wyId}/physicaldata | Match physical summary data


# **matches_wy_id_fulltracking_get**
> MatchFullTracking matches_wy_id_fulltracking_get(wy_id, authorization=authorization)

Broadcast tracking

Returns link to JSON file containing Broadcast Tracking (X,Y) location data

### Example


```python
import openapi_client
from openapi_client.models.match_full_tracking import MatchFullTracking
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
    api_instance = openapi_client.TrackingApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Broadcast tracking
        api_response = api_instance.matches_wy_id_fulltracking_get(wy_id, authorization=authorization)
        print("The response of TrackingApi->matches_wy_id_fulltracking_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->matches_wy_id_fulltracking_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **authorization** | **str**|  | [optional] 

### Return type

[**MatchFullTracking**](MatchFullTracking.md)

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

# **matches_wy_id_physicaldata_get**
> List[MatchPhysicalDataInner] matches_wy_id_physicaldata_get(wy_id, authorization=authorization)

Match physical summary data

Returns a physical metrics summary for all the players of the given match (if available)

### Example


```python
import openapi_client
from openapi_client.models.match_physical_data_inner import MatchPhysicalDataInner
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
    api_instance = openapi_client.TrackingApi(api_client)
    wy_id = 'wy_id_example' # str | Relevant content id
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Match physical summary data
        api_response = api_instance.matches_wy_id_physicaldata_get(wy_id, authorization=authorization)
        print("The response of TrackingApi->matches_wy_id_physicaldata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->matches_wy_id_physicaldata_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**| Relevant content id | 
 **authorization** | **str**|  | [optional] 

### Return type

[**List[MatchPhysicalDataInner]**](MatchPhysicalDataInner.md)

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

