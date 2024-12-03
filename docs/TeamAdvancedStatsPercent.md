# TeamAdvancedStatsPercent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aerial_duels_won** | **float** |  | [optional] 
**defensive_duels_won** | **float** |  | [optional] 
**direct_free_kicks_on_target** | **float** |  | [optional] 
**duels_won** | **float** |  | [optional] 
**field_aerial_duels_won** | **float** |  | [optional] 
**gk_aerial_duels_won** | **float** | &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_saves** | **float** | A successful attempt from the goalkeeper to prevent a shot from being scored, &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_successful_exits** | **float** | &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**goal_conversion** | **float** | Shots converted into a goal | [optional] 
**head_shots_on_target** | **float** |  | [optional] 
**new_defensive_duels_won** | **float** |  | [optional] 
**new_duels_won** | **float** |  | [optional] 
**new_offensive_duels_won** | **float** |  | [optional] 
**new_successful_dribbles** | **float** |  | [optional] 
**offensive_duels_won** | **float** |  | [optional] 
**penalties_conversion** | **float** | Penalties converted into a goal | [optional] 
**shots_on_target** | **float** |  | [optional] 
**successful_back_passes** | **float** |  | [optional] 
**successful_crosses** | **float** |  | [optional] 
**successful_dribbles** | **float** |  | [optional] 
**successful_forward_passes** | **float** |  | [optional] 
**successful_key_passes** | **float** |  | [optional] 
**successful_lateral_passes** | **float** |  | [optional] 
**successful_linkup_plays** | **float** |  | [optional] 
**successful_long_passes** | **float** |  | [optional] 
**successful_passes** | **float** |  | [optional] 
**successful_passes_to_final_third** | **float** |  | [optional] 
**successful_shot_assists** | **float** |  | [optional] 
**successful_smart_passes** | **float** |  | [optional] 
**successful_through_passes** | **float** |  | [optional] 
**successful_touch_in_box** | **float** |  | [optional] 
**successful_vertical_passes** | **float** | &lt;i&gt;Deprecated&lt;i&gt;, same value as successfulLateralPasses | [optional] 
**win** | **float** |  | [optional] 
**yellow_cards_per_foul** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.team_advanced_stats_percent import TeamAdvancedStatsPercent

# TODO update the JSON string below
json = "{}"
# create an instance of TeamAdvancedStatsPercent from a JSON string
team_advanced_stats_percent_instance = TeamAdvancedStatsPercent.from_json(json)
# print the JSON string representation of the object
print(TeamAdvancedStatsPercent.to_json())

# convert the object into a dict
team_advanced_stats_percent_dict = team_advanced_stats_percent_instance.to_dict()
# create an instance of TeamAdvancedStatsPercent from a dict
team_advanced_stats_percent_from_dict = TeamAdvancedStatsPercent.from_dict(team_advanced_stats_percent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


