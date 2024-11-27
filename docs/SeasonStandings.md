# SeasonStandings

Retrieves all the standing's information for the given season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**round_id** | **int** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**teams** | [**List[TheTeamObject]**](TheTeamObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.season_standings import SeasonStandings

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonStandings from a JSON string
season_standings_instance = SeasonStandings.from_json(json)
# print the JSON string representation of the object
print(SeasonStandings.to_json())

# convert the object into a dict
season_standings_dict = season_standings_instance.to_dict()
# create an instance of SeasonStandings from a dict
season_standings_from_dict = SeasonStandings.from_dict(season_standings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


