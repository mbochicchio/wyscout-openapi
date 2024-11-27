# PlayerCareer

Info about the given player career

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**career** | [**List[TheItemsSchema]**](TheItemsSchema.md) |  | [optional] 
**player** | [**Player**](Player.md) | Available with querystring param &#x60;fetch&#x3D;player&#x60; | [optional] 

## Example

```python
from openapi_client.models.player_career import PlayerCareer

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerCareer from a JSON string
player_career_instance = PlayerCareer.from_json(json)
# print the JSON string representation of the object
print(PlayerCareer.to_json())

# convert the object into a dict
player_career_dict = player_career_instance.to_dict()
# create an instance of PlayerCareer from a dict
player_career_from_dict = PlayerCareer.from_dict(player_career_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


