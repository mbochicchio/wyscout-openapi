# MatchPhysicalDataInnerPlayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**metrics** | [**List[MatchPhysicalDataInnerPlayersInnerMetricsInner]**](MatchPhysicalDataInnerPlayersInnerMetricsInner.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.match_physical_data_inner_players_inner import MatchPhysicalDataInnerPlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatchPhysicalDataInnerPlayersInner from a JSON string
match_physical_data_inner_players_inner_instance = MatchPhysicalDataInnerPlayersInner.from_json(json)
# print the JSON string representation of the object
print(MatchPhysicalDataInnerPlayersInner.to_json())

# convert the object into a dict
match_physical_data_inner_players_inner_dict = match_physical_data_inner_players_inner_instance.to_dict()
# create an instance of MatchPhysicalDataInnerPlayersInner from a dict
match_physical_data_inner_players_inner_from_dict = MatchPhysicalDataInnerPlayersInner.from_dict(match_physical_data_inner_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


