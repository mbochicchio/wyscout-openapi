# PlayerMatches

Returns info about the given player matches

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[TheMatchesObject1]**](TheMatchesObject1.md) |  | [optional] 
**player** | [**Player**](Player.md) | Available with querystring param &#x60;fetch&#x3D;player&#x60; | [optional] 

## Example

```python
from openapi_client.models.player_matches import PlayerMatches

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMatches from a JSON string
player_matches_instance = PlayerMatches.from_json(json)
# print the JSON string representation of the object
print(PlayerMatches.to_json())

# convert the object into a dict
player_matches_dict = player_matches_instance.to_dict()
# create an instance of PlayerMatches from a dict
player_matches_from_dict = PlayerMatches.from_dict(player_matches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


