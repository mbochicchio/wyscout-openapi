# MatchAdvancedStatsGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_distance** | **float** |  | [optional] 
**corners** | **int** | A corner kick served as specified in law 17 IFAB Laws of the Game | [optional] 
**dribbles** | **int** | An attempt to move past an opposing player whilst trying to maintain possession of the ball | [optional] 
**fouls** | **int** | An offence committed by a player according to law 12 (1, 3) of the IFAB Laws of the Game | [optional] 
**fouls_suffered** | **int** | An offence committed on a player according to law 12 (1, 3) of the IFAB Laws of the Game | [optional] 
**free_kicks** | **int** | The execution of a free kick according to law 13 of the IFAB Laws of the Game | [optional] 
**goals** | **int** | A goal scored as specified in law 10.1 of the IFAB Laws of the Game | [optional] 
**left_throw_ins** | **int** |  | [optional] 
**offsides** | **int** | An offside as described in the law 11 of the IFAB Laws of the Game | [optional] 
**progressive_runs** | **int** | A continuous ball control by one player attempting to draw the team significantly closer to the opponent goal | [optional] 
**red_cards** | **int** | Disciplinary action by the referee that is indicated by showing a red card according to law 12.3 of the IFAB Laws of the Game | [optional] 
**right_throw_ins** | **int** |  | [optional] 
**shots** | **int** | An attempt towards the opposition&#39;s goal with the intention of scoring | [optional] 
**shots_blocked** | **int** |  | [optional] 
**shots_from_box** | **int** |  | [optional] 
**shots_from_box_on_target** | **int** |  | [optional] 
**shots_from_danger_zone** | **int** | Shooting from the danger zone. The danger area falls within the coordinates x &gt;&#x3D; 84.29 and y &gt;&#x3D; 36.29 and y &lt;&#x3D; 63.71 | [optional] 
**shots_on_post** | **int** |  | [optional] 
**shots_on_target** | **int** |  | [optional] 
**shots_outside_box** | **int** |  | [optional] 
**shots_outside_box_on_target** | **int** |  | [optional] 
**shots_wide** | **int** |  | [optional] 
**total_throw_ins** | **int** | A throw in served as specified in law 17 IFAB Laws of the Game | [optional] 
**touches_in_box** | **int** | An action (a Pass or a Touch) that happens in the opponent penalty area. Duels are excluded from this definition | [optional] 
**xg** | **float** | Expected goals (xG) is a predictive ML model used to assess the likelihood of scoring for every shot made in the game | [optional] 
**xg_per_shot** | **float** |  | [optional] 
**yellow_cards** | **int** | Disciplinary action by the referee that is indicated by showing a yellow card according to law 12.3 of the IFAB Laws of the Game | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_general import MatchAdvancedStatsGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsGeneral from a JSON string
match_advanced_stats_general_instance = MatchAdvancedStatsGeneral.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsGeneral.to_json())

# convert the object into a dict
match_advanced_stats_general_dict = match_advanced_stats_general_instance.to_dict()
# create an instance of MatchAdvancedStatsGeneral from a dict
match_advanced_stats_general_from_dict = MatchAdvancedStatsGeneral.from_dict(match_advanced_stats_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


