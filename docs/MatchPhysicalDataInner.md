# MatchPhysicalDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **str** |  | [optional] 
**players** | [**List[MatchPhysicalDataInnerPlayersInner]**](MatchPhysicalDataInnerPlayersInner.md) |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.match_physical_data_inner import MatchPhysicalDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatchPhysicalDataInner from a JSON string
match_physical_data_inner_instance = MatchPhysicalDataInner.from_json(json)
# print the JSON string representation of the object
print(MatchPhysicalDataInner.to_json())

# convert the object into a dict
match_physical_data_inner_dict = match_physical_data_inner_instance.to_dict()
# create an instance of MatchPhysicalDataInner from a dict
match_physical_data_inner_from_dict = MatchPhysicalDataInner.from_dict(match_physical_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


