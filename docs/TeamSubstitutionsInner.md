# TeamSubstitutionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **str** | Not available in Updated Objects endpoint | [optional] 
**minute** | **int** |  | [optional] 
**player_in** | **int** |  | [optional] 
**player_out** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.team_substitutions_inner import TeamSubstitutionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSubstitutionsInner from a JSON string
team_substitutions_inner_instance = TeamSubstitutionsInner.from_json(json)
# print the JSON string representation of the object
print(TeamSubstitutionsInner.to_json())

# convert the object into a dict
team_substitutions_inner_dict = team_substitutions_inner_instance.to_dict()
# create an instance of TeamSubstitutionsInner from a dict
team_substitutions_inner_from_dict = TeamSubstitutionsInner.from_dict(team_substitutions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


