# CompetitionMatches

The list of matches of the given competition in the current season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;fetch&#x3D;competition&#x60; | [optional] 
**matches** | [**List[TheListOfMatchesInner]**](TheListOfMatchesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.competition_matches import CompetitionMatches

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitionMatches from a JSON string
competition_matches_instance = CompetitionMatches.from_json(json)
# print the JSON string representation of the object
print(CompetitionMatches.to_json())

# convert the object into a dict
competition_matches_dict = competition_matches_instance.to_dict()
# create an instance of CompetitionMatches from a dict
competition_matches_from_dict = CompetitionMatches.from_dict(competition_matches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


