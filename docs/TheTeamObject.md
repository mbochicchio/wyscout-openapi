# TheTeamObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;teams&#x60; | [optional] 
**team_id** | **int** |  | [optional] 
**total_draws** | **int** |  | [optional] 
**total_goals_against** | **int** |  | [optional] 
**total_goals_for** | **int** |  | [optional] 
**total_losses** | **int** |  | [optional] 
**total_played** | **int** |  | [optional] 
**total_points** | **int** |  | [optional] 
**total_wins** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_team_object import TheTeamObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheTeamObject from a JSON string
the_team_object_instance = TheTeamObject.from_json(json)
# print the JSON string representation of the object
print(TheTeamObject.to_json())

# convert the object into a dict
the_team_object_dict = the_team_object_instance.to_dict()
# create an instance of TheTeamObject from a dict
the_team_object_from_dict = TheTeamObject.from_dict(the_team_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


