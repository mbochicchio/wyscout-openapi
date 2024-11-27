# TeamsStandingForTheGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition_id** | **int** |  | [optional] 
**game_draw** | **int** |  | [optional] 
**game_lost** | **int** |  | [optional] 
**game_total** | **int** |  | [optional] 
**game_won** | **int** |  | [optional] 
**goal_against** | **int** |  | [optional] 
**goal_pro** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**points** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**round_name** | **str** |  | [optional] 
**season_id** | **int** |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;team&#x60; | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.teams_standing_for_the_group import TeamsStandingForTheGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsStandingForTheGroup from a JSON string
teams_standing_for_the_group_instance = TeamsStandingForTheGroup.from_json(json)
# print the JSON string representation of the object
print(TeamsStandingForTheGroup.to_json())

# convert the object into a dict
teams_standing_for_the_group_dict = teams_standing_for_the_group_instance.to_dict()
# create an instance of TeamsStandingForTheGroup from a dict
teams_standing_for_the_group_from_dict = TeamsStandingForTheGroup.from_dict(teams_standing_for_the_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


