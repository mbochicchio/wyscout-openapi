# MatchEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aerial_duel** | [**AerialDuelDetails**](AerialDuelDetails.md) |  | [optional] 
**carry** | [**CarryDetails**](CarryDetails.md) |  | [optional] 
**ground_duel** | [**GroundDuelDetails**](GroundDuelDetails.md) |  | [optional] 
**id** | **int** |  | [optional] 
**infraction** | [**InfractionDetails**](InfractionDetails.md) |  | [optional] 
**location** | [**EventLocation**](EventLocation.md) |  | [optional] 
**match_id** | **int** |  | [optional] 
**match_period** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Period&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;1H&lt;/td&gt;&lt;td&gt;First Half Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;2H&lt;/td&gt;&lt;td&gt;Second Half Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;E1&lt;/td&gt;&lt;td&gt;First Extra Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;E2&lt;/td&gt;&lt;td&gt;Second Extra Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;P&lt;/td&gt;&lt;td&gt;Pentalties Time&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**match_timestamp** | **str** |  | [optional] 
**minute** | **int** |  | [optional] 
**opponent_team** | [**OpponentTeamDetails**](OpponentTeamDetails.md) |  | [optional] 
**var_pass** | [**PassDetails**](PassDetails.md) |  | [optional] 
**player** | [**PlayerDetails**](PlayerDetails.md) |  | [optional] 
**possession** | [**PossessionDetails**](PossessionDetails.md) |  | [optional] 
**related_event_id** | **int** |  | [optional] 
**second** | **int** |  | [optional] 
**shot** | [**ShotDetails**](ShotDetails.md) |  | [optional] 
**team** | [**TeamDetails1**](TeamDetails1.md) |  | [optional] 
**type** | [**EventType**](EventType.md) |  | [optional] 
**video_timestamp** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.match_event import MatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MatchEvent from a JSON string
match_event_instance = MatchEvent.from_json(json)
# print the JSON string representation of the object
print(MatchEvent.to_json())

# convert the object into a dict
match_event_dict = match_event_instance.to_dict()
# create an instance of MatchEvent from a dict
match_event_from_dict = MatchEvent.from_dict(match_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


