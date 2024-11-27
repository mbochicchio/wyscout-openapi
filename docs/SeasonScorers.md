# SeasonScorers

Returns info about the given season scorers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) |  | [optional] 
**competition_id** | **int** |  | [optional] 
**players** | [**List[ThePlayerObject1]**](ThePlayerObject1.md) |  | [optional] 
**season** | [**Season**](Season.md) |  | [optional] 
**season_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.season_scorers import SeasonScorers

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonScorers from a JSON string
season_scorers_instance = SeasonScorers.from_json(json)
# print the JSON string representation of the object
print(SeasonScorers.to_json())

# convert the object into a dict
season_scorers_dict = season_scorers_instance.to_dict()
# create an instance of SeasonScorers from a dict
season_scorers_from_dict = SeasonScorers.from_dict(season_scorers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


