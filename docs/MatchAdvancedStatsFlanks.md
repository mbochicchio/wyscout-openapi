# MatchAdvancedStatsFlanks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center_attacks** | **int** |  | [optional] 
**center_xg** | **float** |  | [optional] 
**left_flank_attacks** | **int** |  | [optional] 
**left_flank_xg** | **float** |  | [optional] 
**right_flank_attacks** | **int** |  | [optional] 
**right_flank_xg** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_flanks import MatchAdvancedStatsFlanks

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsFlanks from a JSON string
match_advanced_stats_flanks_instance = MatchAdvancedStatsFlanks.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsFlanks.to_json())

# convert the object into a dict
match_advanced_stats_flanks_dict = match_advanced_stats_flanks_instance.to_dict()
# create an instance of MatchAdvancedStatsFlanks from a dict
match_advanced_stats_flanks_from_dict = MatchAdvancedStatsFlanks.from_dict(match_advanced_stats_flanks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


