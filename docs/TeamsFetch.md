# TeamsFetch

Available with querystring param `fetch=teams`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from openapi_client.models.teams_fetch import TeamsFetch

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsFetch from a JSON string
teams_fetch_instance = TeamsFetch.from_json(json)
# print the JSON string representation of the object
print(TeamsFetch.to_json())

# convert the object into a dict
teams_fetch_dict = teams_fetch_instance.to_dict()
# create an instance of TeamsFetch from a dict
teams_fetch_from_dict = TeamsFetch.from_dict(teams_fetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


