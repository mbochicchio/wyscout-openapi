# TeamLineupBenchedSubstitutions

Available if field `hasFormation=1`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bench** | [**List[TeamBenchedPlayersInner]**](TeamBenchedPlayersInner.md) |  | [optional] 
**lineup** | [**List[TeamLineupInner]**](TeamLineupInner.md) |  | [optional] 
**substitutions** | [**List[TeamSubstitutionsInner]**](TeamSubstitutionsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_lineup_benched_substitutions import TeamLineupBenchedSubstitutions

# TODO update the JSON string below
json = "{}"
# create an instance of TeamLineupBenchedSubstitutions from a JSON string
team_lineup_benched_substitutions_instance = TeamLineupBenchedSubstitutions.from_json(json)
# print the JSON string representation of the object
print(TeamLineupBenchedSubstitutions.to_json())

# convert the object into a dict
team_lineup_benched_substitutions_dict = team_lineup_benched_substitutions_instance.to_dict()
# create an instance of TeamLineupBenchedSubstitutions from a dict
team_lineup_benched_substitutions_from_dict = TeamLineupBenchedSubstitutions.from_dict(team_lineup_benched_substitutions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


