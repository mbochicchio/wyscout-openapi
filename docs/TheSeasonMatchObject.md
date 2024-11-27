# TheSeasonMatchObject


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
from openapi_client.models.the_season_match_object import TheSeasonMatchObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheSeasonMatchObject from a JSON string
the_season_match_object_instance = TheSeasonMatchObject.from_json(json)
# print the JSON string representation of the object
print(TheSeasonMatchObject.to_json())

# convert the object into a dict
the_season_match_object_dict = the_season_match_object_instance.to_dict()
# create an instance of TheSeasonMatchObject from a dict
the_season_match_object_from_dict = TheSeasonMatchObject.from_dict(the_season_match_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


