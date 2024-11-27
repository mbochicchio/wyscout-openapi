# TeamMatchesMatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition_id** | **int** |  | [optional] 
**var_date** | **str** |  | [optional] 
**dateutc** | **str** |  | [optional] 
**gameweek** | **int** |  | [optional] 
**label** | **str** | homeTeam – awayTeam, homeScore-awayScore | [optional] 
**match_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Fixture&lt;/td&gt;&lt;td&gt;The match has yet to come&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Played&lt;/td&gt;&lt;td&gt;The match is over&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.team_matches_matches_inner import TeamMatchesMatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMatchesMatchesInner from a JSON string
team_matches_matches_inner_instance = TeamMatchesMatchesInner.from_json(json)
# print the JSON string representation of the object
print(TeamMatchesMatchesInner.to_json())

# convert the object into a dict
team_matches_matches_inner_dict = team_matches_matches_inner_instance.to_dict()
# create an instance of TeamMatchesMatchesInner from a dict
team_matches_matches_inner_from_dict = TeamMatchesMatchesInner.from_dict(team_matches_matches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


