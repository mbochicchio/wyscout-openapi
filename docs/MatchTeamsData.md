# MatchTeamsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_aid** | [**MatchTeamData**](MatchTeamData.md) | Use querystring param &#x60;useSides&#x3D;true&#x60; to change teamId label in &#x60;home&#x60; or &#x60;away&#x60; | [optional] 
**team_bid** | [**MatchTeamData**](MatchTeamData.md) | Use querystring param &#x60;useSides&#x3D;true&#x60; to change teamId label in &#x60;home&#x60; or &#x60;away&#x60; | [optional] 

## Example

```python
from openapi_client.models.match_teams_data import MatchTeamsData

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTeamsData from a JSON string
match_teams_data_instance = MatchTeamsData.from_json(json)
# print the JSON string representation of the object
print(MatchTeamsData.to_json())

# convert the object into a dict
match_teams_data_dict = match_teams_data_instance.to_dict()
# create an instance of MatchTeamsData from a dict
match_teams_data_from_dict = MatchTeamsData.from_dict(match_teams_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


