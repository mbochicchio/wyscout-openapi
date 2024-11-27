# TheMatchesObject


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
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.the_matches_object import TheMatchesObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheMatchesObject from a JSON string
the_matches_object_instance = TheMatchesObject.from_json(json)
# print the JSON string representation of the object
print(TheMatchesObject.to_json())

# convert the object into a dict
the_matches_object_dict = the_matches_object_instance.to_dict()
# create an instance of TheMatchesObject from a dict
the_matches_object_from_dict = TheMatchesObject.from_dict(the_matches_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


