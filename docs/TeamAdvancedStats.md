# TeamAdvancedStats

Returns advanced statistics of a given player in a specific competition season. Overall, the statistics provided are relative to the selected season, and not to a specific team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | [**TeamAdvancedStatsAverage**](TeamAdvancedStatsAverage.md) |  | [optional] 
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**percent** | [**TeamAdvancedStatsPercent**](TeamAdvancedStatsPercent.md) |  | [optional] 
**round** | [**Round**](Round.md) | Available with querystring param &#x60;fetch&#x3D;round&#x60; | [optional] 
**round_id** | **int** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;team&#x60; | [optional] 
**team_id** | **int** |  | [optional] 
**total** | [**TeamAdvancedStatsTotal**](TeamAdvancedStatsTotal.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_advanced_stats import TeamAdvancedStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamAdvancedStats from a JSON string
team_advanced_stats_instance = TeamAdvancedStats.from_json(json)
# print the JSON string representation of the object
print(TeamAdvancedStats.to_json())

# convert the object into a dict
team_advanced_stats_dict = team_advanced_stats_instance.to_dict()
# create an instance of TeamAdvancedStats from a dict
team_advanced_stats_from_dict = TeamAdvancedStats.from_dict(team_advanced_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


