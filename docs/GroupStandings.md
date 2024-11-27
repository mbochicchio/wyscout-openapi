# GroupStandings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TeamsStandingForTheGroup]**](TeamsStandingForTheGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_standings import GroupStandings

# TODO update the JSON string below
json = "{}"
# create an instance of GroupStandings from a JSON string
group_standings_instance = GroupStandings.from_json(json)
# print the JSON string representation of the object
print(GroupStandings.to_json())

# convert the object into a dict
group_standings_dict = group_standings_instance.to_dict()
# create an instance of GroupStandings from a dict
group_standings_from_dict = GroupStandings.from_dict(group_standings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


