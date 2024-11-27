# openapi_client.AreasApi

All URIs are relative to *https://apirest.wyscout.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areas_get**](AreasApi.md#areas_get) | **GET** /areas | Areas


# **areas_get**
> List[Area] areas_get(authorization=authorization)

Areas

Returns a list of areas. For area codes we use the ISO 3166-1 standard and the following additional custom areas codes: <table><thead><tr><th>name</th><th>id</th><th>alpha2code</th><th>alpha3code</th></tr></thead><tbody><tr><td>Asia</td><td >1</td><td>AS</td><td>XAS</td></tr><tr><td>Africa</td><td >2</td><td>AF</td><td>XAF</td></tr><tr><td>N/C America</td><td >3</td><td>NC</td><td>XNC</td></tr><tr><td>South America</td><td >4</td><td>SA</td><td>XSA</td></tr><tr><td>Oceania</td><td >5</td><td>OC</td><td>XOC</td></tr><tr><td>Europe</td><td >6</td><td>EU</td><td>XEU</td></tr><tr><td>Chinese Taipei</td><td >49</td><td>CT</td><td>XCT</td></tr><tr><td>England</td><td >67</td><td>EN</td><td>XEN</td></tr><tr><td>Northern Ireland</td><td >144</td><td>NI</td><td>XNI</td></tr><tr><td>Scotland</td><td >164</td><td>SC</td><td>XSC</td></tr><tr><td>Tahiti</td><td >187</td><td>TA</td><td>XTA</td></tr><tr><td>Wales</td><td >208</td><td>WA</td><td>XWA</td></tr><tr><td>Zanzibar</td><td >212</td><td>ZA</td><td>XZA</td></tr><tr><td>Timor-Leste</td><td >213</td><td>LS</td><td>XLS</td></tr><tr><td>Kosovo</td><td >228</td><td>KS</td><td>XKS</td></tr><tr><td>France, metropolitan</td><td >298</td><td>FX</td><td>XFX</td></tr><tr><td>Netherlands antilles</td><td >305</td><td>AN</td><td>XAN</td></tr><tr><td>World</td><td >320</td><td>WO</td><td>XWO</td></tr></tbody></table>

### Example


```python
import openapi_client
from openapi_client.models.area import Area
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
    api_instance = openapi_client.AreasApi(api_client)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Areas
        api_response = api_instance.areas_get(authorization=authorization)
        print("The response of AreasApi->areas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreasApi->areas_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

### Return type

[**List[Area]**](Area.md)

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

