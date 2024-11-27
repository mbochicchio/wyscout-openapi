# MatchDirections

Returns the direction of attack of both teams in each half of the game

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1_h** | [**MatchDirectionsObject**](MatchDirectionsObject.md) |  | [optional] 
**var_2_h** | [**MatchDirectionsObject**](MatchDirectionsObject.md) |  | [optional] 
**e1** | [**MatchDirectionsObject**](MatchDirectionsObject.md) |  | [optional] 
**e2** | [**MatchDirectionsObject**](MatchDirectionsObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.match_directions import MatchDirections

# TODO update the JSON string below
json = "{}"
# create an instance of MatchDirections from a JSON string
match_directions_instance = MatchDirections.from_json(json)
# print the JSON string representation of the object
print(MatchDirections.to_json())

# convert the object into a dict
match_directions_dict = match_directions_instance.to_dict()
# create an instance of MatchDirections from a dict
match_directions_from_dict = MatchDirections.from_dict(match_directions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


