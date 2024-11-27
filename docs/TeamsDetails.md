# TeamsDetails

Available with querystring param `details=teams`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_team** | [**OriginTeamDetails**](OriginTeamDetails.md) |  | [optional] 
**to_team** | [**DestinationTeamDetails**](DestinationTeamDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.teams_details import TeamsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsDetails from a JSON string
teams_details_instance = TeamsDetails.from_json(json)
# print the JSON string representation of the object
print(TeamsDetails.to_json())

# convert the object into a dict
teams_details_dict = teams_details_instance.to_dict()
# create an instance of TeamsDetails from a dict
teams_details_from_dict = TeamsDetails.from_dict(teams_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


