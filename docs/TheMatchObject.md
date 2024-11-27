# TheMatchObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | [**List[TheMatchGoalObject]**](TheMatchGoalObject.md) |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] 
**match_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_match_object import TheMatchObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheMatchObject from a JSON string
the_match_object_instance = TheMatchObject.from_json(json)
# print the JSON string representation of the object
print(TheMatchObject.to_json())

# convert the object into a dict
the_match_object_dict = the_match_object_instance.to_dict()
# create an instance of TheMatchObject from a dict
the_match_object_from_dict = TheMatchObject.from_dict(the_match_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


