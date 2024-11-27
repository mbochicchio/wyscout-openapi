# CompetitionTeams

The list of teams of the given competition in the current season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**teams** | [**List[Team]**](Team.md) |  | [optional] 

## Example

```python
from openapi_client.models.competition_teams import CompetitionTeams

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitionTeams from a JSON string
competition_teams_instance = CompetitionTeams.from_json(json)
# print the JSON string representation of the object
print(CompetitionTeams.to_json())

# convert the object into a dict
competition_teams_dict = competition_teams_instance.to_dict()
# create an instance of CompetitionTeams from a dict
competition_teams_from_dict = CompetitionTeams.from_dict(competition_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


