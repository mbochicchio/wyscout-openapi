# openapi_client.ExtraApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updatedobjects_deleted_get**](ExtraApi.md#updatedobjects_deleted_get) | **GET** /updatedobjects/deleted | Updated Objects deleted
[**updatedobjects_updated_get**](ExtraApi.md#updatedobjects_updated_get) | **GET** /updatedobjects/updated | Updated Objects updated


# **updatedobjects_deleted_get**
> UpdatedObjectsDeleted updatedobjects_deleted_get(updated_since, type, count=count, limit=limit, page=page, authorization=authorization)

Updated Objects deleted

Info about the recently deleted resources.  Specific API call to keep track of deletes on our database objects on a daily basis.  You can go back for a max of 168 hours (1 week). The results are ordered by increasing date, with the first page containing the objects updated furthest in the past, and the last page returning the objects updated the most recently.  Where not differently specified, any time field refers to <i>Europe/Rome</i> timezone

### Example


```python
import openapi_client
from openapi_client.models.updated_objects_deleted import UpdatedObjectsDeleted
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
    api_instance = openapi_client.ExtraApi(api_client)
    updated_since = 'updated_since_example' # str | Filter resources by date in the format YYYY-MM-DD HH:MM:SS (example: 2018-02-09 18:00:00), you can go back for a max of 168 hours (1 week)
    type = 'type_example' # str | Resource type: `areas`, `coaches`, `competitions`, `matches`, `matchevents`, `playercareers`, `playerinjuries`, `players`, `referees`, `rounds`, `seasons`, `teamcareers`, `teams`, `transfers`
    count = 'count_example' # str | Alias for limit argument (optional)
    limit = 'limit_example' # str | Allows to change the number of results for page (limited to max 100 results for single page) (optional)
    page = 'page_example' # str | Allows to change page (current page) from which the results are fetched (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Updated Objects deleted
        api_response = api_instance.updatedobjects_deleted_get(updated_since, type, count=count, limit=limit, page=page, authorization=authorization)
        print("The response of ExtraApi->updatedobjects_deleted_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtraApi->updatedobjects_deleted_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_since** | **str**| Filter resources by date in the format YYYY-MM-DD HH:MM:SS (example: 2018-02-09 18:00:00), you can go back for a max of 168 hours (1 week) | 
 **type** | **str**| Resource type: &#x60;areas&#x60;, &#x60;coaches&#x60;, &#x60;competitions&#x60;, &#x60;matches&#x60;, &#x60;matchevents&#x60;, &#x60;playercareers&#x60;, &#x60;playerinjuries&#x60;, &#x60;players&#x60;, &#x60;referees&#x60;, &#x60;rounds&#x60;, &#x60;seasons&#x60;, &#x60;teamcareers&#x60;, &#x60;teams&#x60;, &#x60;transfers&#x60; | 
 **count** | **str**| Alias for limit argument | [optional] 
 **limit** | **str**| Allows to change the number of results for page (limited to max 100 results for single page) | [optional] 
 **page** | **str**| Allows to change page (current page) from which the results are fetched | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**UpdatedObjectsDeleted**](UpdatedObjectsDeleted.md)

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

# **updatedobjects_updated_get**
> UpdatedObjectsUpdated updatedobjects_updated_get(type, updated_since, count=count, limit=limit, authorization=authorization, page=page, empty_payload=empty_payload)

Updated Objects updated

Info about the recently updated resources.  Specific API call to keep track of updates on our database objects on a daily basis.  You can go back for a max of 168 hours (1 week). The payload of a week, especially for some tables, is huge, the ideal situation could be to call the updated objects even once every 1/2/3/4 hours or at least a few times throughout the day for every type of object you are interested in. The result however is paginated allowing you to iterate through the pages and obtain all updated objects in managable blocks.  The results are ordered by increasing date, with the first page containing the objects updated furthest in the past, and the last page returning the objects updated the most recently.  Where not differently specified, any time field refers to <i>Europe/Rome</i> timezone

### Example


```python
import openapi_client
from openapi_client.models.updated_objects_updated import UpdatedObjectsUpdated
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
    api_instance = openapi_client.ExtraApi(api_client)
    type = 'type_example' # str | Resource type: `areas`, `coaches`, `competitions`, `matches`, `matchevents`, `playercareers`, `playerinjuries`, `players`, `referees`, `rounds`, `seasons`, `teamcareers`, `teams`, `transfers`
    updated_since = 'updated_since_example' # str | Filter resources by date in the format YYYY-MM-DD HH:MM:SS (example: 2018-02-09 18:00:00), you can go back for a max of 168 hours (1 week)
    count = 'count_example' # str | Alias for limit argument (optional)
    limit = 'limit_example' # str | Allows to change the number of results for page (limited to max 100 results for single page) (optional)
    authorization = 'authorization_example' # str |  (optional)
    page = 'page_example' # str | Allows to change page (current page) from which the results are fetched (optional)
    empty_payload = 'empty_payload_example' # str | If true every resource id is returned without the respective payload (default is false) (optional)

    try:
        # Updated Objects updated
        api_response = api_instance.updatedobjects_updated_get(type, updated_since, count=count, limit=limit, authorization=authorization, page=page, empty_payload=empty_payload)
        print("The response of ExtraApi->updatedobjects_updated_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtraApi->updatedobjects_updated_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Resource type: &#x60;areas&#x60;, &#x60;coaches&#x60;, &#x60;competitions&#x60;, &#x60;matches&#x60;, &#x60;matchevents&#x60;, &#x60;playercareers&#x60;, &#x60;playerinjuries&#x60;, &#x60;players&#x60;, &#x60;referees&#x60;, &#x60;rounds&#x60;, &#x60;seasons&#x60;, &#x60;teamcareers&#x60;, &#x60;teams&#x60;, &#x60;transfers&#x60; | 
 **updated_since** | **str**| Filter resources by date in the format YYYY-MM-DD HH:MM:SS (example: 2018-02-09 18:00:00), you can go back for a max of 168 hours (1 week) | 
 **count** | **str**| Alias for limit argument | [optional] 
 **limit** | **str**| Allows to change the number of results for page (limited to max 100 results for single page) | [optional] 
 **authorization** | **str**|  | [optional] 
 **page** | **str**| Allows to change page (current page) from which the results are fetched | [optional] 
 **empty_payload** | **str**| If true every resource id is returned without the respective payload (default is false) | [optional] 

### Return type

[**UpdatedObjectsUpdated**](UpdatedObjectsUpdated.md)

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

