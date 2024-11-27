# MatchAdvancedStatsPasses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **int** | The last action of a player from the goalscoring team, prior to the Goal being scored by a teammate, or an Own goal | [optional] 
**avg_pass_length** | **float** |  | [optional] 
**avg_pass_to_final_third_length** | **float** |  | [optional] 
**back_passes** | **int** |  | [optional] 
**back_passes_successful** | **int** |  | [optional] 
**crosses_blocked** | **int** | Not distinguished by height | [optional] 
**crosses_from_left_flank** | **int** |  | [optional] 
**crosses_from_left_flank_successful** | **int** |  | [optional] 
**crosses_from_right_flank** | **int** |  | [optional] 
**crosses_from_right_flank_successful** | **int** |  | [optional] 
**crosses_high** | **int** | Cross over waist height | [optional] 
**crosses_low** | **int** | Cross cross below waist height | [optional] 
**crosses_successful** | **int** |  | [optional] 
**crosses_total** | **int** | A ball played from the offensive flanks aimed towards a teammate in the area in front of the opponent’s goal | [optional] 
**deep_completed_passes** | **int** | A non-cross Pass that is targeted to the zone within 20 meters of the opponent’s goal | [optional] 
**deep_completed_passes_successful** | **int** |  | [optional] 
**forward_passes** | **int** |  | [optional] 
**forward_passes_successful** | **int** |  | [optional] 
**key_passes** | **int** | A pass that immediately creates a clear goal scoring opportunity for a teammate who in turn fails to score | [optional] 
**key_passes_successful** | **int** |  | [optional] 
**lateral_passes** | **int** | Passes in two 90° angles rotated by 45° facing sideways, longer than 12 meters | [optional] 
**lateral_passes_successful** | **int** |  | [optional] 
**long_passes** | **int** |  | [optional] 
**long_passes_successful** | **int** |  | [optional] 
**match_tempo** | **float** | Number of team passes per minute of pure ball possession | [optional] 
**pass_to_final_thirds** | **int** |  | [optional] 
**pass_to_final_thirds_successful** | **int** |  | [optional] 
**pass_to_penalty_areas** | **int** |  | [optional] 
**pass_to_penalty_areas_successful** | **int** |  | [optional] 
**passes** | **int** | An attempt to pass the ball to a teammate | [optional] 
**passes_successful** | **int** |  | [optional] 
**progressive_passes** | **int** | A forward pass that attempts to advance a team significantly closer to the opponent’s goal | [optional] 
**progressive_passes_successful** | **int** |  | [optional] 
**short_medium_passes** | **int** |  | [optional] 
**short_medium_passes_successful** | **int** |  | [optional] 
**shot_assists** | **int** | The last action of a player prior to a teammate having a Shot | [optional] 
**smart_passes** | **int** | A creative and penetrative pass that attempts to break the opposition&#39;s defensive lines to gain a significant advantage in attack | [optional] 
**smart_passes_successful** | **int** |  | [optional] 
**through_passes** | **int** | A pass played into the space behind the defensive line for a teammate to contest | [optional] 
**through_passes_successful** | **int** |  | [optional] 
**vertical_passes** | **int** | &lt;i&gt;Deprecated&lt;i&gt;, same value as lateralPasses | [optional] 
**vertical_passes_successful** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_passes import MatchAdvancedStatsPasses

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsPasses from a JSON string
match_advanced_stats_passes_instance = MatchAdvancedStatsPasses.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsPasses.to_json())

# convert the object into a dict
match_advanced_stats_passes_dict = match_advanced_stats_passes_instance.to_dict()
# create an instance of MatchAdvancedStatsPasses from a dict
match_advanced_stats_passes_from_dict = MatchAdvancedStatsPasses.from_dict(match_advanced_stats_passes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


