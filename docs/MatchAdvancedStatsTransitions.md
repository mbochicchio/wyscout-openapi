# MatchAdvancedStatsTransitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses_high** | **int** |  | [optional] 
**losses_low** | **int** |  | [optional] 
**losses_medium** | **int** |  | [optional] 
**losses_total** | **int** |  | [optional] 
**opponent_half_recoveries** | **int** |  | [optional] 
**own_half_losses** | **int** |  | [optional] 
**recoveries_high** | **int** |  | [optional] 
**recoveries_low** | **int** |  | [optional] 
**recoveries_medium** | **int** |  | [optional] 
**recoveries_total** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_transitions import MatchAdvancedStatsTransitions

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsTransitions from a JSON string
match_advanced_stats_transitions_instance = MatchAdvancedStatsTransitions.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsTransitions.to_json())

# convert the object into a dict
match_advanced_stats_transitions_dict = match_advanced_stats_transitions_instance.to_dict()
# create an instance of MatchAdvancedStatsTransitions from a dict
match_advanced_stats_transitions_from_dict = MatchAdvancedStatsTransitions.from_dict(match_advanced_stats_transitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


