# MatchFormations

Retrieves information about a given match's formations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**List[MatchFormation]**](MatchFormation.md) |  | [optional] 
**home** | [**List[MatchFormation]**](MatchFormation.md) |  | [optional] 

## Example

```python
from openapi_client.models.match_formations import MatchFormations

# TODO update the JSON string below
json = "{}"
# create an instance of MatchFormations from a JSON string
match_formations_instance = MatchFormations.from_json(json)
# print the JSON string representation of the object
print(MatchFormations.to_json())

# convert the object into a dict
match_formations_dict = match_formations_instance.to_dict()
# create an instance of MatchFormations from a dict
match_formations_from_dict = MatchFormations.from_dict(match_formations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


