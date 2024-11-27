# PlayerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.player_details import PlayerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerDetails from a JSON string
player_details_instance = PlayerDetails.from_json(json)
# print the JSON string representation of the object
print(PlayerDetails.to_json())

# convert the object into a dict
player_details_dict = player_details_instance.to_dict()
# create an instance of PlayerDetails from a dict
player_details_from_dict = PlayerDetails.from_dict(player_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


