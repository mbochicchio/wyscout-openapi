# MatchAdvancedStats

Returns advanced statistics of a given match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacks** | [**ListOfStatisticsAttacks**](ListOfStatisticsAttacks.md) |  | [optional] 
**defence** | [**ListOfStatisticsDefense**](ListOfStatisticsDefense.md) |  | [optional] 
**duels** | [**ListOfStatisticsDuels**](ListOfStatisticsDuels.md) |  | [optional] 
**flanks** | [**ListOfStatisticsFlanks**](ListOfStatisticsFlanks.md) |  | [optional] 
**general** | [**ListOfStatisticsGeneral**](ListOfStatisticsGeneral.md) |  | [optional] 
**match** | [**Match**](Match.md) | Available with querystring param &#x60;details&#x3D;match&#x60; | [optional] 
**match_id** | **int** |  | [optional] 
**open_play** | [**ListOfStatisticsOpenPlay**](ListOfStatisticsOpenPlay.md) |  | [optional] 
**passes** | [**ListOfStatisticsPasses**](ListOfStatisticsPasses.md) |  | [optional] 
**possession** | [**ListOfStatisticsPossession**](ListOfStatisticsPossession.md) |  | [optional] 
**teams** | [**TeamsDetails**](TeamsDetails.md) |  | [optional] 
**transitions** | [**ListOfStatisticsTransitions**](ListOfStatisticsTransitions.md) |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats import MatchAdvancedStats

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStats from a JSON string
match_advanced_stats_instance = MatchAdvancedStats.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStats.to_json())

# convert the object into a dict
match_advanced_stats_dict = match_advanced_stats_instance.to_dict()
# create an instance of MatchAdvancedStats from a dict
match_advanced_stats_from_dict = MatchAdvancedStats.from_dict(match_advanced_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


