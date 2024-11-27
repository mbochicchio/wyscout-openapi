# OpponentDetails1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.opponent_details1 import OpponentDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of OpponentDetails1 from a JSON string
opponent_details1_instance = OpponentDetails1.from_json(json)
# print the JSON string representation of the object
print(OpponentDetails1.to_json())

# convert the object into a dict
opponent_details1_dict = opponent_details1_instance.to_dict()
# create an instance of OpponentDetails1 from a dict
opponent_details1_from_dict = OpponentDetails1.from_dict(opponent_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


