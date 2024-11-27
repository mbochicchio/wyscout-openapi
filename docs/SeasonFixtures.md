# SeasonFixtures

Retrieves all the matches for the given season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**matches** | [**List[TheMatchObject]**](TheMatchObject.md) |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.season_fixtures import SeasonFixtures

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonFixtures from a JSON string
season_fixtures_instance = SeasonFixtures.from_json(json)
# print the JSON string representation of the object
print(SeasonFixtures.to_json())

# convert the object into a dict
season_fixtures_dict = season_fixtures_instance.to_dict()
# create an instance of SeasonFixtures from a dict
season_fixtures_from_dict = SeasonFixtures.from_dict(season_fixtures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


