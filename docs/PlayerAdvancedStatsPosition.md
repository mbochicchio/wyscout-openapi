# PlayerAdvancedStatsPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **float** |  | [optional] 
**position** | [**PositionOfThePlayer**](PositionOfThePlayer.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_advanced_stats_position import PlayerAdvancedStatsPosition

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerAdvancedStatsPosition from a JSON string
player_advanced_stats_position_instance = PlayerAdvancedStatsPosition.from_json(json)
# print the JSON string representation of the object
print(PlayerAdvancedStatsPosition.to_json())

# convert the object into a dict
player_advanced_stats_position_dict = player_advanced_stats_position_instance.to_dict()
# create an instance of PlayerAdvancedStatsPosition from a dict
player_advanced_stats_position_from_dict = PlayerAdvancedStatsPosition.from_dict(player_advanced_stats_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


