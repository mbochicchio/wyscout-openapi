# SeasonMatches

Returns the list of matches played in the given season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[TheSeasonMatchObject]**](TheSeasonMatchObject.md) |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 

## Example

```python
from openapi_client.models.season_matches import SeasonMatches

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonMatches from a JSON string
season_matches_instance = SeasonMatches.from_json(json)
# print the JSON string representation of the object
print(SeasonMatches.to_json())

# convert the object into a dict
season_matches_dict = season_matches_instance.to_dict()
# create an instance of SeasonMatches from a dict
season_matches_from_dict = SeasonMatches.from_dict(season_matches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


