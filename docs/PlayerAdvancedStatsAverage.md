# PlayerAdvancedStatsAverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerations** | **float** | A run with the ball with a significant speed up | [optional] 
**aerial_duels** | **float** | When two or more players from opposing teams jump to compete for the ball | [optional] 
**assists** | **float** | The last action of a player from the goalscoring team, prior to the Goal being scored by a teammate, or an Own goal | [optional] 
**attacking_actions** | **float** |  | [optional] 
**back_passes** | **float** | An attempt to pass the ball back to a teammate | [optional] 
**ball_losses** | **float** | Any Action that ends a Possession of the current team | [optional] 
**ball_recoveries** | **float** | Any Action that ends a Possession of the opposition team (the last action of this possession is a Loss) and starts a Possession for current team | [optional] 
**clearances** | **float** | An Action (generally a pass) when the player, while having other option, to pass or to hold the ball, is instead clearing it, either with a long pass forward without a precise target or for a throw in/corner kick, playing safe | [optional] 
**corners** | **float** | A corner kick served as specified in law 17 IFAB Laws of the Game | [optional] 
**counterpressing_recoveries** | **float** | Any Recovery that ends a Possession of the opposition team with length less than 5 seconds | [optional] 
**crosses** | **float** | A ball played from the offensive flanks aimed towards a teammate in the area in front of the opponent’s goal | [optional] 
**dangerous_opponent_half_recoveries** | **float** | Ball’s recoveries in the opponent half that lead to a shot within 20s | [optional] 
**dangerous_own_half_losses** | **float** | Ball’s losses in his own half that lead to a shot within 20s | [optional] 
**defensive_actions** | **float** | An act of player actively intercepting the ball by anticipating its movement when the opponent is shooting, passing or crossing | [optional] 
**defensive_duels** | **float** | When a player attempts to dispossess an opposition player to stop an attack progressing | [optional] 
**defensive_duels_won** | **float** |  | [optional] 
**direct_free_kicks** | **float** |  | [optional] 
**direct_free_kicks_on_target** | **float** |  | [optional] 
**direct_red_cards** | **float** | Disciplinary action by the referee that is indicated by showing a red card according to law 12.3 of the IFAB Laws of the Game | [optional] 
**dribble_distance_from_opponent_goal** | **float** |  | [optional] 
**dribbles** | **float** | An attempt to move past an opposing player whilst trying to maintain possession of the ball | [optional] 
**dribbles_against** | **float** |  | [optional] 
**dribbles_against_won** | **float** |  | [optional] 
**duels** | **float** | A challenge between two players to gain control of the ball, progress with the ball or change its direction | [optional] 
**duels_won** | **float** |  | [optional] 
**field_aerial_duels** | **int** |  | [optional] 
**field_aerial_duels_won** | **int** |  | [optional] 
**forward_passes** | **float** | An attempt to pass the ball forward to a teammate | [optional] 
**fouls** | **float** | An offence committed by a player according to law 12 (1, 3) of the IFAB Laws of the Game | [optional] 
**fouls_suffered** | **float** | An offence committed on a player according to law 12 (1, 3) of the IFAB Laws of the Game | [optional] 
**free_kicks** | **float** | The execution of a free kick according to law 13 of the IFAB Laws of the Game | [optional] 
**free_kicks_on_target** | **float** |  | [optional] 
**gk_aerial_duels** | **int** | When two or more players from opposing teams jump to compete for the ball, &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_aerial_duels_won** | **int** | &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_conceded_goals** | **int** | A goal scored by an opponent as specified in law 10.1 of the IFAB Laws of the Game, &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_exits** | **int** | &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_saves** | **int** | A successful attempt from the goalkeeper to prevent a shot from being scored, &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_shots_against** | **int** | A shot on target faced by the goalkeeper, &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**gk_successful_exits** | **int** | &lt;i&gt;Only Goalkeeper&lt;/i&gt; | [optional] 
**goal_kicks** | **float** | A goal kick according to law 16 of the IFAB Laws of the Game | [optional] 
**goal_kicks_long** | **float** |  | [optional] 
**goal_kicks_short** | **float** |  | [optional] 
**goals** | **float** | A goal scored as specified in law 10.1 of the IFAB Laws of the Game | [optional] 
**head_shots** | **float** | An attempt towards the opposition&#39;s goal with the intention of scoring | [optional] 
**interceptions** | **float** | An act of player actively intercepting the ball by anticipating its movement when the opponent is shooting, passing or crossing | [optional] 
**key_passes** | **float** | A pass that immediately creates a clear goal scoring opportunity for a teammate who in turn fails to score | [optional] 
**lateral_passes** | **int** | Passes in two 90° angles rotated by 45° facing sideways, longer than 12 meters | [optional] 
**linkup_plays** | **float** | An action of an attacking player receiving a ball from a defender or a midfielder with his back to the opposite goal | [optional] 
**long_pass_length** | **float** |  | [optional] 
**long_passes** | **float** | A ground pass longer than 45 meters or a high pass longer than 25 meters | [optional] 
**loose_ball_duels** | **float** | A duel for a loose ball, when no team has clear ball possession | [optional] 
**loose_ball_duels_won** | **float** |  | [optional] 
**missed_balls** | **float** | Missed ball is a type of Touch when the player is trying to control the ball, but can’t reach it | [optional] 
**new_defensive_duels_won** | **int** |  | [optional] 
**new_duels_won** | **int** |  | [optional] 
**new_offensive_duels_won** | **int** |  | [optional] 
**new_successful_dribbles** | **int** |  | [optional] 
**offensive_duels** | **float** | A ground Duel for the player in possession of the ball | [optional] 
**offensive_duels_won** | **float** |  | [optional] 
**offsides** | **float** | An offside as described in the law 11 of the IFAB Laws of the Game | [optional] 
**opponent_half_recoveries** | **float** | Ball’s recoveries in the opponent half | [optional] 
**own_half_losses** | **float** | Ball’s losses in his own half | [optional] 
**pass_length** | **float** |  | [optional] 
**passes** | **float** | An attempt to pass the ball to a teammate | [optional] 
**passes_to_final_third** | **float** | Any pass that originates outside of the final third and the next ball touch occurs within the final third | [optional] 
**penalties** | **float** | A shot from a penalty kick as specified in law 14 of the IFAB Laws of the Game | [optional] 
**progressive_passes** | **float** | A forward pass that attempts to advance a team significantly closer to the opponent’s goal | [optional] 
**progressive_run** | **float** | A continuous ball control by one player attempting to draw the team significantly closer to the opponent goal | [optional] 
**received_pass** | **float** |  | [optional] 
**red_cards** | **float** | Disciplinary action by the referee that is indicated by showing a red card according to law 12.3 of the IFAB Laws of the Game | [optional] 
**second_assists** | **float** | The last action of a player from the goalscoring team, prior to an Assist by a teammate | [optional] 
**shot_assists** | **float** | The last action of a player prior to a teammate having a Shot | [optional] 
**shot_on_target_assists** | **float** | The last action of a player prior to a teammate having a Shot on target | [optional] 
**shots** | **float** | An attempt towards the opposition&#39;s goal with the intention of scoring | [optional] 
**shots_blocked** | **float** |  | [optional] 
**shots_on_target** | **float** |  | [optional] 
**sliding_tackles** | **float** | An aggressive slide on the ground in the legs of the opposition player with a clear intention to dispossess the opponent or to clear the ball out | [optional] 
**smart_passes** | **float** | A creative and penetrative pass that attempts to break the opposition&#39;s defensive lines to gain a significant advantage in attack | [optional] 
**successful_attacking_actions** | **float** |  | [optional] 
**successful_back_passes** | **float** |  | [optional] 
**successful_crosses** | **float** |  | [optional] 
**successful_defensive_action** | **float** |  | [optional] 
**successful_dribbles** | **float** |  | [optional] 
**successful_forward_passes** | **float** |  | [optional] 
**successful_goal_kicks** | **float** |  | [optional] 
**successful_key_passes** | **float** |  | [optional] 
**successful_lateral_passes** | **int** |  | [optional] 
**successful_linkup_plays** | **float** |  | [optional] 
**successful_long_passes** | **float** |  | [optional] 
**successful_passes** | **float** |  | [optional] 
**successful_passes_to_final_third** | **float** |  | [optional] 
**successful_penalties** | **float** |  | [optional] 
**successful_progressive_passes** | **float** |  | [optional] 
**successful_sliding_tackles** | **float** |  | [optional] 
**successful_smart_passes** | **float** |  | [optional] 
**successful_through_passes** | **float** |  | [optional] 
**successful_vertical_passes** | **float** | &lt;i&gt;Deprecated&lt;i&gt;, Same value as successfulLateralPasses | [optional] 
**third_assists** | **float** | The last action of a player from the goalscoring team, prior to a Second assist by a teammate | [optional] 
**through_passes** | **float** | A pass played into the space behind the defensive line for a teammate to contest | [optional] 
**touch_in_box** | **float** | An action (a Pass or a Touch) that happens in the opponent penalty area. Duels are excluded from this definition | [optional] 
**vertical_passes** | **float** | &lt;i&gt;Deprecated&lt;i&gt;, Same value as lateralPasses | [optional] 
**xg_assist** | **float** | Expected assist (xA) value for a pass is a value of expected goals (xG) or the shot that this pass led to | [optional] 
**xg_save** | **float** | A pre-shot xG value of a probability of the current shot (not necessarily on target) to be scored | [optional] 
**xg_shot** | **float** | Expected goals (xG) is a predictive ML model used to assess the likelihood of scoring for every shot made in the game | [optional] 
**yellow_cards** | **float** | Disciplinary action by the referee that is indicated by showing a yellow card according to law 12.3 of the IFAB Laws of the Game | [optional] 

## Example

```python
from openapi_client.models.player_advanced_stats_average import PlayerAdvancedStatsAverage

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerAdvancedStatsAverage from a JSON string
player_advanced_stats_average_instance = PlayerAdvancedStatsAverage.from_json(json)
# print the JSON string representation of the object
print(PlayerAdvancedStatsAverage.to_json())

# convert the object into a dict
player_advanced_stats_average_dict = player_advanced_stats_average_instance.to_dict()
# create an instance of PlayerAdvancedStatsAverage from a dict
player_advanced_stats_average_from_dict = PlayerAdvancedStatsAverage.from_dict(player_advanced_stats_average_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

