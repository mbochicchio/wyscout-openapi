# OpponentTeamDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formation** | **str** | Opponent formation used at the time of the event | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.opponent_team_details import OpponentTeamDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OpponentTeamDetails from a JSON string
opponent_team_details_instance = OpponentTeamDetails.from_json(json)
# print the JSON string representation of the object
print(OpponentTeamDetails.to_json())

# convert the object into a dict
opponent_team_details_dict = opponent_team_details_instance.to_dict()
# create an instance of OpponentTeamDetails from a dict
opponent_team_details_from_dict = OpponentTeamDetails.from_dict(opponent_team_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


