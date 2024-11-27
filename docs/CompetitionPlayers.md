# CompetitionPlayers

The list of players of the given competition in the current season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**players** | [**List[Player]**](Player.md) |  | [optional] 

## Example

```python
from openapi_client.models.competition_players import CompetitionPlayers

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitionPlayers from a JSON string
competition_players_instance = CompetitionPlayers.from_json(json)
# print the JSON string representation of the object
print(CompetitionPlayers.to_json())

# convert the object into a dict
competition_players_dict = competition_players_instance.to_dict()
# create an instance of CompetitionPlayers from a dict
competition_players_from_dict = CompetitionPlayers.from_dict(competition_players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


