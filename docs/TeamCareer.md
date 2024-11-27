# TeamCareer

Retrieves all the team career information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**career** | [**List[TheTeamCareerArrayInner]**](TheTeamCareerArrayInner.md) |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;fetch&#x3D;team&#x60; | [optional] 

## Example

```python
from openapi_client.models.team_career import TeamCareer

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCareer from a JSON string
team_career_instance = TeamCareer.from_json(json)
# print the JSON string representation of the object
print(TeamCareer.to_json())

# convert the object into a dict
team_career_dict = team_career_instance.to_dict()
# create an instance of TeamCareer from a dict
team_career_from_dict = TeamCareer.from_dict(team_career_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


