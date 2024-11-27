# PlayerContractinfo

Returns info about the given player contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agencies** | **List[str]** |  | [optional] 
**contract_expiration** | **str** |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**player_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.player_contractinfo import PlayerContractinfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerContractinfo from a JSON string
player_contractinfo_instance = PlayerContractinfo.from_json(json)
# print the JSON string representation of the object
print(PlayerContractinfo.to_json())

# convert the object into a dict
player_contractinfo_dict = player_contractinfo_instance.to_dict()
# create an instance of PlayerContractinfo from a dict
player_contractinfo_from_dict = PlayerContractinfo.from_dict(player_contractinfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


