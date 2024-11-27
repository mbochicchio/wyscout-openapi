# DestinationTeamDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from openapi_client.models.destination_team_details import DestinationTeamDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationTeamDetails from a JSON string
destination_team_details_instance = DestinationTeamDetails.from_json(json)
# print the JSON string representation of the object
print(DestinationTeamDetails.to_json())

# convert the object into a dict
destination_team_details_dict = destination_team_details_instance.to_dict()
# create an instance of DestinationTeamDetails from a dict
destination_team_details_from_dict = DestinationTeamDetails.from_dict(destination_team_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


