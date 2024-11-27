# Match

Retrieves information about a given match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;details&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**var_date** | **str** |  | [optional] 
**dateutc** | **str** |  | [optional] 
**duration** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Duration&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Regular&lt;/td&gt;&lt;td&gt;The match is over at regulation&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;GoldenGoal&lt;/td&gt;&lt;td&gt;The match is over with a golden goal during extra time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;SilverGoal&lt;/td&gt;&lt;td&gt;The match is over after the first extra time period&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ExtraTime&lt;/td&gt;&lt;td&gt;The match is over after extra time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Penalties&lt;/td&gt;&lt;td&gt;The match is over after penalties&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gameweek** | **int** |  | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**has_data_available** | **bool** |  | [optional] 
**label** | **str** | homeTeam – awayTeam, homeScore-awayScore | [optional] 
**referees** | [**List[MatchRefereesInner]**](MatchRefereesInner.md) |  | [optional] 
**round** | [**Round**](Round.md) | Available with querystring param &#x60;details&#x3D;round&#x60; | [optional] 
**round_id** | **int** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;details&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Cancelled&lt;/td&gt;&lt;td&gt;The match has been cancelled&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Fixture&lt;/td&gt;&lt;td&gt;The match has yet to come&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Played&lt;/td&gt;&lt;td&gt;The match has officially over&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Playing&lt;/td&gt;&lt;td&gt;The match is currently underway&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Postponed&lt;/td&gt;&lt;td&gt;The match has been postponed and no new date and time is available yet&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Suspended&lt;/td&gt;&lt;td&gt;The match has been suspended and no new date and time is available yet&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Awarded&lt;/td&gt;&lt;td&gt;The match has been awarded&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**teams_data** | [**MatchTeamsData**](MatchTeamsData.md) |  | [optional] 
**venue** | **str** |  | [optional] 
**winner** | **int** | If no winner is present, value will be &#x60;0&#x60; | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match import Match

# TODO update the JSON string below
json = "{}"
# create an instance of Match from a JSON string
match_instance = Match.from_json(json)
# print the JSON string representation of the object
print(Match.to_json())

# convert the object into a dict
match_dict = match_instance.to_dict()
# create an instance of Match from a dict
match_from_dict = Match.from_dict(match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


