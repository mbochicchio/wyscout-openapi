# CompetitionSeasons

The list of seasons for a given competition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**seasons** | [**List[TheListOfSeasonInner]**](TheListOfSeasonInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.competition_seasons import CompetitionSeasons

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitionSeasons from a JSON string
competition_seasons_instance = CompetitionSeasons.from_json(json)
# print the JSON string representation of the object
print(CompetitionSeasons.to_json())

# convert the object into a dict
competition_seasons_dict = competition_seasons_instance.to_dict()
# create an instance of CompetitionSeasons from a dict
competition_seasons_from_dict = CompetitionSeasons.from_dict(competition_seasons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


