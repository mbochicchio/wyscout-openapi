# TheAvailableFiltersObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advsearches** | **List[str]** |  | [optional] 
**fetches** | **List[str]** |  | [optional] 
**filters** | **List[str]** |  | [optional] 
**searches** | **List[str]** |  | [optional] 
**sorts** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.the_available_filters_object import TheAvailableFiltersObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheAvailableFiltersObject from a JSON string
the_available_filters_object_instance = TheAvailableFiltersObject.from_json(json)
# print the JSON string representation of the object
print(TheAvailableFiltersObject.to_json())

# convert the object into a dict
the_available_filters_object_dict = the_available_filters_object_instance.to_dict()
# create an instance of TheAvailableFiltersObject from a dict
the_available_filters_object_from_dict = TheAvailableFiltersObject.from_dict(the_available_filters_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


