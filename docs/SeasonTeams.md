# SeasonTeams

Returns the list of teams in the given season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 
**teams** | [**List[Team]**](Team.md) |  | [optional] 

## Example

```python
from openapi_client.models.season_teams import SeasonTeams

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonTeams from a JSON string
season_teams_instance = SeasonTeams.from_json(json)
# print the JSON string representation of the object
print(SeasonTeams.to_json())

# convert the object into a dict
season_teams_dict = season_teams_instance.to_dict()
# create an instance of SeasonTeams from a dict
season_teams_from_dict = SeasonTeams.from_dict(season_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


