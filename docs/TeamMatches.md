# TeamMatches

Returns the list of matches played by the given team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[TeamMatchesMatchesInner]**](TeamMatchesMatchesInner.md) |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;fetch&#x3D;team&#x60; | [optional] 

## Example

```python
from openapi_client.models.team_matches import TeamMatches

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMatches from a JSON string
team_matches_instance = TeamMatches.from_json(json)
# print the JSON string representation of the object
print(TeamMatches.to_json())

# convert the object into a dict
team_matches_dict = team_matches_instance.to_dict()
# create an instance of TeamMatches from a dict
team_matches_from_dict = TeamMatches.from_dict(team_matches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


