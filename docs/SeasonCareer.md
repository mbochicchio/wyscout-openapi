# SeasonCareer

Retrieves all the team's information for the given season.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**rounds** | [**List[RoundData]**](RoundData.md) |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;fetch&#x3D;season&#x60; | [optional] 

## Example

```python
from openapi_client.models.season_career import SeasonCareer

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonCareer from a JSON string
season_career_instance = SeasonCareer.from_json(json)
# print the JSON string representation of the object
print(SeasonCareer.to_json())

# convert the object into a dict
season_career_dict = season_career_instance.to_dict()
# create an instance of SeasonCareer from a dict
season_career_from_dict = SeasonCareer.from_dict(season_career_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


