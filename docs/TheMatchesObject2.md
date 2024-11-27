# TheMatchesObject2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition_id** | **int** |  | [optional] 
**var_date** | **str** |  | [optional] 
**dateutc** | **str** |  | [optional] 
**gameweek** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**match_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**season_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.the_matches_object2 import TheMatchesObject2

# TODO update the JSON string below
json = "{}"
# create an instance of TheMatchesObject2 from a JSON string
the_matches_object2_instance = TheMatchesObject2.from_json(json)
# print the JSON string representation of the object
print(TheMatchesObject2.to_json())

# convert the object into a dict
the_matches_object2_dict = the_matches_object2_instance.to_dict()
# create an instance of TheMatchesObject2 from a dict
the_matches_object2_from_dict = TheMatchesObject2.from_dict(the_matches_object2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


