# TeamFixtures

Retrieves all the fixtures matches for the given team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[TheMatchesObject2]**](TheMatchesObject2.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_fixtures import TeamFixtures

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFixtures from a JSON string
team_fixtures_instance = TeamFixtures.from_json(json)
# print the JSON string representation of the object
print(TeamFixtures.to_json())

# convert the object into a dict
team_fixtures_dict = team_fixtures_instance.to_dict()
# create an instance of TeamFixtures from a dict
team_fixtures_from_dict = TeamFixtures.from_dict(team_fixtures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


