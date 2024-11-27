# TheTeamCareerArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;details&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**goal_against** | **int** |  | [optional] 
**goal_pro** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**match_draw** | **int** |  | [optional] 
**match_lost** | **int** |  | [optional] 
**match_total** | **int** |  | [optional] 
**match_won** | **int** |  | [optional] 
**points** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**round_name** | **str** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;details&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_team_career_array_inner import TheTeamCareerArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of TheTeamCareerArrayInner from a JSON string
the_team_career_array_inner_instance = TheTeamCareerArrayInner.from_json(json)
# print the JSON string representation of the object
print(TheTeamCareerArrayInner.to_json())

# convert the object into a dict
the_team_career_array_inner_dict = the_team_career_array_inner_instance.to_dict()
# create an instance of TheTeamCareerArrayInner from a dict
the_team_career_array_inner_from_dict = TheTeamCareerArrayInner.from_dict(the_team_career_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


