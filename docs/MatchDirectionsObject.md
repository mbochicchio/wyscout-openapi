# MatchDirectionsObject

An object containing the ids of the two teams classified by the relative direction of play

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_to_right_team_id** | **int** | The id of the team playing from the left to the right | [optional] 
**right_to_left_team_id** | **int** | The id of the team playing from the right to the left | [optional] 

## Example

```python
from openapi_client.models.match_directions_object import MatchDirectionsObject

# TODO update the JSON string below
json = "{}"
# create an instance of MatchDirectionsObject from a JSON string
match_directions_object_instance = MatchDirectionsObject.from_json(json)
# print the JSON string representation of the object
print(MatchDirectionsObject.to_json())

# convert the object into a dict
match_directions_object_dict = match_directions_object_instance.to_dict()
# create an instance of MatchDirectionsObject from a dict
match_directions_object_from_dict = MatchDirectionsObject.from_dict(match_directions_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


