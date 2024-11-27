# TeamLineupInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **str** | Not available in Updated Objects endpoint | [optional] 
**goals** | **str** |  | [optional] 
**own_goals** | **str** |  | [optional] 
**player** | [**Player**](Player.md) | Available with param &#x60;details&#x3D;players&#x60; | [optional] 
**player_id** | **int** |  | [optional] 
**red_cards** | **str** |  | [optional] 
**shirt_number** | **int** |  | [optional] 
**yellow_cards** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.team_lineup_inner import TeamLineupInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamLineupInner from a JSON string
team_lineup_inner_instance = TeamLineupInner.from_json(json)
# print the JSON string representation of the object
print(TeamLineupInner.to_json())

# convert the object into a dict
team_lineup_inner_dict = team_lineup_inner_instance.to_dict()
# create an instance of TeamLineupInner from a dict
team_lineup_inner_from_dict = TeamLineupInner.from_dict(team_lineup_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


