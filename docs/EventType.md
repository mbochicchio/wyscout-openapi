# EventType

The event is identified by its primary and secondary types. The primary type is guaranteed to be present for all the events and has only one value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Primary event types&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;acceleration&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;clearance&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;corner&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;fairplay&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;free_kick&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;game_interruption&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;goal_kick&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;goalkeeper_exit&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;infraction&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;interception&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;offside&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;own_goal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;penalty&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pressing_attempt&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;received_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;shot_against&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;throw_in&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;touch&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;postmatch_penalty&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;postmatch_penalty_faced&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**secondary** | **List[str]** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Secondary event types&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;aerial_duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;assist&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;back_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ball_out&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;carry&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;conceded_goal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;counterpressing_recovery&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;cross&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;cross_blocked&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;deep_completed_cross&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;deep_completition&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;defensive_duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;dribble&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;dribbled_past_attempt&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;forward_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;foul_suffered&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;free_kick_cross&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;free_kick_shot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;goal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ground_duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;hand_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;head_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;head_shot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;key_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;lateral_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;linkup_play&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;long_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;loose_ball_duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;loss&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;offensive_duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;opportunity&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pass_into_penalty_area&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pass_to_final_third&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;penalty_conceded_goal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;penalty_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;penalty_goal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;penalty_save&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pressing_duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;progressive_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;progressive_run&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;recovery&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;red_card&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;save&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;save_with_reflex&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;second_assist&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;short_or_medium_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;shot_after_corner&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;shot_after_free_kick&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;shot_after_throw_in&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;shot_assist&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;shot_block&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;sliding_tackle&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;smart_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;third_assist&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;through_pass&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;touch_in_box&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;under_pressure&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;whistle&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;yellow_card&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;postmatch_penalty_saved&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;conceded_postmatch_penalty&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.event_type import EventType

# TODO update the JSON string below
json = "{}"
# create an instance of EventType from a JSON string
event_type_instance = EventType.from_json(json)
# print the JSON string representation of the object
print(EventType.to_json())

# convert the object into a dict
event_type_dict = event_type_instance.to_dict()
# create an instance of EventType from a dict
event_type_from_dict = EventType.from_dict(event_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


