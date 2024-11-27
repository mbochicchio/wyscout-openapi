# MatchTeamData

Retrieves team data about a given match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach** | [**Coach**](Coach.md) | Available with param &#x60;details&#x3D;coaches&#x60; | [optional] 
**coach_id** | **int** |  | [optional] 
**formation** | [**TeamLineupBenchedSubstitutions**](TeamLineupBenchedSubstitutions.md) |  | [optional] 
**has_formation** | **int** |  | [optional] 
**score** | **int** |  | [optional] 
**score_et** | **int** |  | [optional] 
**score_ht** | **int** |  | [optional] 
**score_p** | **int** |  | [optional] 
**side** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Side&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;home&lt;/td&gt;&lt;td&gt;The team was the home team for the match&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;away&lt;/td&gt;&lt;td&gt;The team was the away team for the match&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;none&lt;/td&gt;&lt;td&gt;No side was determined for this team in the match&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_team_data import MatchTeamData

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTeamData from a JSON string
match_team_data_instance = MatchTeamData.from_json(json)
# print the JSON string representation of the object
print(MatchTeamData.to_json())

# convert the object into a dict
match_team_data_dict = match_team_data_instance.to_dict()
# create an instance of MatchTeamData from a dict
match_team_data_from_dict = MatchTeamData.from_dict(match_team_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


