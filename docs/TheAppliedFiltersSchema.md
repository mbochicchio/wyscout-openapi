# TheAppliedFiltersSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advsearch** | **List[str]** |  | [optional] 
**fetch** | **List[str]** |  | [optional] 
**filter** | **List[str]** |  | [optional] 
**limit** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**search** | **str** |  | [optional] 
**sort** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.the_applied_filters_schema import TheAppliedFiltersSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TheAppliedFiltersSchema from a JSON string
the_applied_filters_schema_instance = TheAppliedFiltersSchema.from_json(json)
# print the JSON string representation of the object
print(TheAppliedFiltersSchema.to_json())

# convert the object into a dict
the_applied_filters_schema_dict = the_applied_filters_schema_instance.to_dict()
# create an instance of TheAppliedFiltersSchema from a dict
the_applied_filters_schema_from_dict = TheAppliedFiltersSchema.from_dict(the_applied_filters_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


