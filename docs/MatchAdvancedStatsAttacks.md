# MatchAdvancedStatsAttacks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corners** | **int** |  | [optional] 
**corners_with_shot** | **int** |  | [optional] 
**counter_attacks** | **int** |  | [optional] 
**free_kicks** | **int** |  | [optional] 
**free_kicks_with_shot** | **int** |  | [optional] 
**positional_attack** | **int** |  | [optional] 
**positional_with_shots** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**with_shots** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_attacks import MatchAdvancedStatsAttacks

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsAttacks from a JSON string
match_advanced_stats_attacks_instance = MatchAdvancedStatsAttacks.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsAttacks.to_json())

# convert the object into a dict
match_advanced_stats_attacks_dict = match_advanced_stats_attacks_instance.to_dict()
# create an instance of MatchAdvancedStatsAttacks from a dict
match_advanced_stats_attacks_from_dict = MatchAdvancedStatsAttacks.from_dict(match_advanced_stats_attacks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


