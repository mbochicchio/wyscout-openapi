# TeamAdvancedStatsPercent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aerial_duels_won** | **int** |  | [optional] 
**defensive_duels_won** | **float** |  | [optional] 
**direct_free_kicks_on_target** | **float** |  | [optional] 
**duels_won** | **float** |  | [optional] 
**field_aerial_duels_won** | **int** |  | [optional] 
**gk_aerial_duels_won** | **int** | &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_saves** | **int** | A successful attempt from the goalkeeper to prevent a shot from being scored, &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_successful_exits** | **int** | &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**goal_conversion** | **float** | Shots converted into a goal | [optional] 
**head_shots_on_target** | **int** |  | [optional] 
**new_defensive_duels_won** | **int** |  | [optional] 
**new_duels_won** | **int** |  | [optional] 
**new_offensive_duels_won** | **int** |  | [optional] 
**new_successful_dribbles** | **int** |  | [optional] 
**offensive_duels_won** | **float** |  | [optional] 
**penalties_conversion** | **int** | Penalties converted into a goal | [optional] 
**shots_on_target** | **float** |  | [optional] 
**successful_back_passes** | **float** |  | [optional] 
**successful_crosses** | **float** |  | [optional] 
**successful_dribbles** | **float** |  | [optional] 
**successful_forward_passes** | **float** |  | [optional] 
**successful_key_passes** | **float** |  | [optional] 
**successful_lateral_passes** | **int** |  | [optional] 
**successful_linkup_plays** | **float** |  | [optional] 
**successful_long_passes** | **float** |  | [optional] 
**successful_passes** | **float** |  | [optional] 
**successful_passes_to_final_third** | **float** |  | [optional] 
**successful_shot_assists** | **int** |  | [optional] 
**successful_smart_passes** | **float** |  | [optional] 
**successful_through_passes** | **float** |  | [optional] 
**successful_touch_in_box** | **float** |  | [optional] 
**successful_vertical_passes** | **float** | &lt;i&gt;Deprecated&lt;i&gt;, same value as successfulLateralPasses | [optional] 
**win** | **float** |  | [optional] 
**yellow_cards_per_foul** | **int** |  | [optional] 

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


