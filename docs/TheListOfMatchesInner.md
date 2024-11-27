# TheListOfMatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition_id** | **int** |  | [optional] 
**var_date** | **str** |  | [optional] 
**dateutc** | **str** |  | [optional] 
**gameweek** | **int** |  | [optional] 
**label** | **str** | homeTeam – awayTeam, homeScore - awayScore | [optional] 
**match_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Fixture&lt;/td&gt;&lt;td&gt;The match has yet to kick-off and a date and time has been defined&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Played&lt;/td&gt;&lt;td&gt;The match has played&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.the_list_of_matches_inner import TheListOfMatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TheListOfMatchesInner from a JSON string
the_list_of_matches_inner_instance = TheListOfMatchesInner.from_json(json)
# print the JSON string representation of the object
print(TheListOfMatchesInner.to_json())

# convert the object into a dict
the_list_of_matches_inner_dict = the_list_of_matches_inner_instance.to_dict()
# create an instance of TheListOfMatchesInner from a dict
the_list_of_matches_inner_from_dict = TheListOfMatchesInner.from_dict(the_list_of_matches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


