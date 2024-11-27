# SeasonPlayers

Returns the list of players in the given season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**players** | [**List[Player]**](Player.md) |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 

## Example

```python
from openapi_client.models.season_players import SeasonPlayers

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonPlayers from a JSON string
season_players_instance = SeasonPlayers.from_json(json)
# print the JSON string representation of the object
print(SeasonPlayers.to_json())

# convert the object into a dict
season_players_dict = season_players_instance.to_dict()
# create an instance of SeasonPlayers from a dict
season_players_from_dict = SeasonPlayers.from_dict(season_players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


