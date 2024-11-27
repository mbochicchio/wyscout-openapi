# MatchAdvancedStatsDuels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aerial_duels** | **int** | When two or more players from opposing teams jump to compete for the ball | [optional] 
**aerial_duels_successful** | **int** |  | [optional] 
**challenge_intensity** | **float** | Number of defensive actions (defensive duels, loose ball duels, interceptions, tackles) per minute of opponent ball possession | [optional] 
**defensive_duels** | **int** | When a player attempts to dispossess an opposition player to stop an attack progressing | [optional] 
**defensive_duels_successful** | **int** |  | [optional] 
**dribbles** | **int** | An attempt to move past an opposing player whilst trying to maintain possession of the ball | [optional] 
**dribbles_successful** | **int** |  | [optional] 
**duels** | **int** | A challenge between two players to gain control of the ball, progress with the ball or change its direction | [optional] 
**duels_successful** | **int** |  | [optional] 
**ground_duels** | **int** |  | [optional] 
**ground_duels_successful** | **int** |  | [optional] 
**loose_ball_duels** | **int** | A duel for a loose ball, when no team has clear ball possession | [optional] 
**loose_ball_duels_successful** | **int** |  | [optional] 
**offensive_duels** | **int** | A ground Duel for the player in possession of the ball | [optional] 
**offensive_duels_successful** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_advanced_stats_duels import MatchAdvancedStatsDuels

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAdvancedStatsDuels from a JSON string
match_advanced_stats_duels_instance = MatchAdvancedStatsDuels.from_json(json)
# print the JSON string representation of the object
print(MatchAdvancedStatsDuels.to_json())

# convert the object into a dict
match_advanced_stats_duels_dict = match_advanced_stats_duels_instance.to_dict()
# create an instance of MatchAdvancedStatsDuels from a dict
match_advanced_stats_duels_from_dict = MatchAdvancedStatsDuels.from_dict(match_advanced_stats_duels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


