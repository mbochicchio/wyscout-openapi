# openapi_client.VideosApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**videos_match_id_get**](VideosApi.md#videos_match_id_get) | **GET** /videos/{matchId} | Videos
[**videos_match_id_offsets_get**](VideosApi.md#videos_match_id_offsets_get) | **GET** /videos/{matchId}/offsets | Videos offsets
[**videos_match_id_qualities_get**](VideosApi.md#videos_match_id_qualities_get) | **GET** /videos/{matchId}/qualities | Videos qualities


# **videos_match_id_get**
> Video videos_match_id_get(match_id, start=start, fetch=fetch, quality=quality, authorization=authorization, end=end)

Videos

Returns links to match footage and info about the given video.  When used with \"start\" and \"end\" optional parameters the endpoint  allows to build custom video clips. Example: /videos/{matchId}?start=100&end=120    Our commercial model allows a max number of minutes of usage per month for accessing API Videos.     Please note: anytime the endpoint is called and the video links are generated the related amount of seconds will be counted, even if the user would not effectively click on the link.    Counters are on linking generation, not on effective video usage. You can check response headers for information about your current usage status.    In order not to consume minutes of videos when building videoclips, when you need to know video offset values or to check for the availability of a certain video quality, you can use videos/wyid/offsets and videos/wyid/qualities.     Please note: FullHD quality links require a specific commercial package.

### Example


```python
import openapi_client
from openapi_client.models.video import Video
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
    api_instance = openapi_client.VideosApi(api_client)
    match_id = 'match_id_example' # str | Relevant match id
    start = 'start_example' # str | Start second of the custom videoclip (optional)
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `match` (optional)
    quality = 'quality_example' # str | Returns a specific video quality only (lq, sd, hd, fullhd) (optional)
    authorization = 'authorization_example' # str |  (optional)
    end = 'end_example' # str | End second of the custom videoclip (optional)

    try:
        # Videos
        api_response = api_instance.videos_match_id_get(match_id, start=start, fetch=fetch, quality=quality, authorization=authorization, end=end)
        print("The response of VideosApi->videos_match_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_match_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| Relevant match id | 
 **start** | **str**| Start second of the custom videoclip | [optional] 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;match&#x60; | [optional] 
 **quality** | **str**| Returns a specific video quality only (lq, sd, hd, fullhd) | [optional] 
 **authorization** | **str**|  | [optional] 
 **end** | **str**| End second of the custom videoclip | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Content-Type -  <br>  * X-RateLimit-RemainingSeconds - Total number of seconds remaining in current billing period (month) <br>  * X-RateLimit-TotalSeconds - Total number of seconds consumed by the user in current billing period (month) <br>  * X-RateLimit-UserReset - When a new billing period will start and above counters will be reset <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**429** | 429 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **videos_match_id_offsets_get**
> VideoOffsets videos_match_id_offsets_get(match_id, fetch=fetch, authorization=authorization)

Videos offsets

Information about the given match video periods offsets

### Example


```python
import openapi_client
from openapi_client.models.video_offsets import VideoOffsets
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
    api_instance = openapi_client.VideosApi(api_client)
    match_id = 'match_id_example' # str | Relevant match id
    fetch = 'fetch_example' # str | List of related objects to be fetched, separated by comma: `match` (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Videos offsets
        api_response = api_instance.videos_match_id_offsets_get(match_id, fetch=fetch, authorization=authorization)
        print("The response of VideosApi->videos_match_id_offsets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_match_id_offsets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| Relevant match id | 
 **fetch** | **str**| List of related objects to be fetched, separated by comma: &#x60;match&#x60; | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**VideoOffsets**](VideoOffsets.md)

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

# **videos_match_id_qualities_get**
> VideoQualities videos_match_id_qualities_get(match_id, authorization=authorization)

Videos qualities

Information about the existing video qualities for a given match

### Example


```python
import openapi_client
from openapi_client.models.video_qualities import VideoQualities
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
    api_instance = openapi_client.VideosApi(api_client)
    match_id = 'match_id_example' # str | Relevant match id
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Videos qualities
        api_response = api_instance.videos_match_id_qualities_get(match_id, authorization=authorization)
        print("The response of VideosApi->videos_match_id_qualities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_match_id_qualities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| Relevant match id | 
 **authorization** | **str**|  | [optional] 

### Return type

[**VideoQualities**](VideoQualities.md)

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

