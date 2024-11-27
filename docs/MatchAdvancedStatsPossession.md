# MatchAdvancedStatsPossession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_possession_duration** | **str** |  | [optional] 
**minutes_of_possession1_15** | **str** |  | [optional] 
**minutes_of_possession106_120** | **str** |  | [optional] 
**minutes_of_possession16_30** | **str** |  | [optional] 
**minutes_of_possession31_45** | **str** |  | [optional] 
**minutes_of_possession46_60** | **str** |  | [optional] 
**minutes_of_possession61_75** | **str** |  | [optional] 
**minutes_of_possession76_90** | **str** |  | [optional] 
**minutes_of_possession91_105** | **str** |  | [optional] 
**possession1_15** | **int** |  | [optional] 
**possession106_120** | **int** |  | [optional] 
**possession16_30** | **int** |  | [optional] 
**possession31_45** | **int** |  | [optional] 
**possession46_60** | **int** |  | [optional] 
**possession61_75** | **int** |  | [optional] 
**possession76_90** | **int** |  | [optional] 
**possession91_105** | **int** |  | [optional] 
**possession_number** | **int** |  | [optional] 
**possession_percent** | **int** |  | [optional] 
**pure_possession_time** | **str** |  | [optional] 
**reaching_opponent_box** | **int** |  | [optional] 
**reaching_opponent_half** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_possession import MatchAdvancedStatsPossession

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsPossession from a JSON string
match_advanced_stats_possession_instance = MatchAdvancedStatsPossession.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsPossession.to_json())

# convert the object into a dict
match_advanced_stats_possession_dict = match_advanced_stats_possession_instance.to_dict()
# create an instance of MatchAdvancedStatsPossession from a dict
match_advanced_stats_possession_from_dict = MatchAdvancedStatsPossession.from_dict(match_advanced_stats_possession_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


