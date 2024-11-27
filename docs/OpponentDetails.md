# OpponentDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.opponent_details import OpponentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OpponentDetails from a JSON string
opponent_details_instance = OpponentDetails.from_json(json)
# print the JSON string representation of the object
print(OpponentDetails.to_json())

# convert the object into a dict
opponent_details_dict = opponent_details_instance.to_dict()
# create an instance of OpponentDetails from a dict
opponent_details_from_dict = OpponentDetails.from_dict(opponent_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


