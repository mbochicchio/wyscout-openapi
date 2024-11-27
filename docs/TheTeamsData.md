# TheTeamsData

Available with querystring param `details=teams`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_team** | [**OriginTeamDetails**](OriginTeamDetails.md) |  | [optional] 
**to_team** | [**DestinationTeamDetails**](DestinationTeamDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.the_teams_data import TheTeamsData

# TODO update the JSON string below
json = "{}"
# create an instance of TheTeamsData from a JSON string
the_teams_data_instance = TheTeamsData.from_json(json)
# print the JSON string representation of the object
print(TheTeamsData.to_json())

# convert the object into a dict
the_teams_data_dict = the_teams_data_instance.to_dict()
# create an instance of TheTeamsData from a dict
the_teams_data_from_dict = TheTeamsData.from_dict(the_teams_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


