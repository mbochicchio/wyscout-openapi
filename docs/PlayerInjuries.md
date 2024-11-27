# PlayerInjuries

Returns info about the given player injuries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**injuries** | [**List[TheInjuryObject]**](TheInjuryObject.md) |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.player_injuries import PlayerInjuries

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerInjuries from a JSON string
player_injuries_instance = PlayerInjuries.from_json(json)
# print the JSON string representation of the object
print(PlayerInjuries.to_json())

# convert the object into a dict
player_injuries_dict = player_injuries_instance.to_dict()
# create an instance of PlayerInjuries from a dict
player_injuries_from_dict = PlayerInjuries.from_dict(player_injuries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


