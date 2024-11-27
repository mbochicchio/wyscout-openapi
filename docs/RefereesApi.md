# openapi_client.RefereesApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**referees_wy_id_get**](RefereesApi.md#referees_wy_id_get) | **GET** /referees/{wyId} | Referee details


# **referees_wy_id_get**
> Referee referees_wy_id_get(wy_id, image_data_url=image_data_url, authorization=authorization)

Referee details

Returns info about the given referee

### Example


```python
import openapi_client
from openapi_client.models.referee import Referee
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
    api_instance = openapi_client.RefereesApi(api_client)
    wy_id = 'wy_id_example' # str | 
    image_data_url = 'image_data_url_example' # str | If true adds the base64 encoded referee image to the payload (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Referee details
        api_response = api_instance.referees_wy_id_get(wy_id, image_data_url=image_data_url, authorization=authorization)
        print("The response of RefereesApi->referees_wy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefereesApi->referees_wy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wy_id** | **str**|  | 
 **image_data_url** | **str**| If true adds the base64 encoded referee image to the payload | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Referee**](Referee.md)

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

