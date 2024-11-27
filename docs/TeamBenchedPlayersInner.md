# TeamBenchedPlayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **str** | Not available in Updated Objects endpoint | [optional] 
**goals** | **str** |  | [optional] 
**own_goals** | **str** |  | [optional] 
**player** | [**Player**](Player.md) | Available with param &#x60;details&#x3D;players&#x60; | [optional] 
**player_id** | **int** |  | [optional] 
**red_cards** | **str** |  | [optional] 
**shirt_number** | **str** |  | [optional] 
**yellow_cards** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.team_benched_players_inner import TeamBenchedPlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamBenchedPlayersInner from a JSON string
team_benched_players_inner_instance = TeamBenchedPlayersInner.from_json(json)
# print the JSON string representation of the object
print(TeamBenchedPlayersInner.to_json())

# convert the object into a dict
team_benched_players_inner_dict = team_benched_players_inner_instance.to_dict()
# create an instance of TeamBenchedPlayersInner from a dict
team_benched_players_inner_from_dict = TeamBenchedPlayersInner.from_dict(team_benched_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


