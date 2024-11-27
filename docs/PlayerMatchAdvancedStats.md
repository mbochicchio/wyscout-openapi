# PlayerMatchAdvancedStats

Returns advanced statistics of a given player in a specific match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | [**PlayerAdvancedStatsAverage**](PlayerAdvancedStatsAverage.md) |  | [optional] 
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**match** | [**Match**](Match.md) | Available with querystring param &#x60;fetch&#x3D;match&#x60; | [optional] 
**match_id** | **int** |  | [optional] 
**percent** | [**PlayerAdvancedStatsPercent**](PlayerAdvancedStatsPercent.md) |  | [optional] 
**player** | [**Player**](Player.md) | Available with querystring param &#x60;details&#x3D;player&#x60; | [optional] 
**player_id** | **int** |  | [optional] 
**positions** | [**List[PlayerAdvancedStatsPosition]**](PlayerAdvancedStatsPosition.md) |  | [optional] 
**round** | [**Round**](Round.md) | Available with querystring param &#x60;fetch&#x3D;round&#x60; | [optional] 
**round_id** | **int** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**total** | [**PlayerAdvancedStatsTotal**](PlayerAdvancedStatsTotal.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_match_advanced_stats import PlayerMatchAdvancedStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMatchAdvancedStats from a JSON string
player_match_advanced_stats_instance = PlayerMatchAdvancedStats.from_json(json)
# print the JSON string representation of the object
print(PlayerMatchAdvancedStats.to_json())

# convert the object into a dict
player_match_advanced_stats_dict = player_match_advanced_stats_instance.to_dict()
# create an instance of PlayerMatchAdvancedStats from a dict
player_match_advanced_stats_from_dict = PlayerMatchAdvancedStats.from_dict(player_match_advanced_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


