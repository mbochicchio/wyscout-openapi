# MatchAdvancedStatsDefence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clearances** | **int** | An Action (generally a pass) when the player, while having other option, to pass or to hold the ball, is instead clearing it, either with a long pass forward without a precise target or for a throw in/corner kick, playing safe | [optional] 
**interceptions** | **int** | An act of player actively intercepting the ball by anticipating its movement when the opponent is shooting, passing or crossing | [optional] 
**ppda** | **float** | A metric to quantify high press intensity introduced by Colin Trainor in 2014 | [optional] 
**tackles** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_defence import MatchAdvancedStatsDefence

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsDefence from a JSON string
match_advanced_stats_defence_instance = MatchAdvancedStatsDefence.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsDefence.to_json())

# convert the object into a dict
match_advanced_stats_defence_dict = match_advanced_stats_defence_instance.to_dict()
# create an instance of MatchAdvancedStatsDefence from a dict
match_advanced_stats_defence_from_dict = MatchAdvancedStatsDefence.from_dict(match_advanced_stats_defence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


