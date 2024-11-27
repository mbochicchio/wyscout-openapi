# SubstitutionFetch

Available with querystring param `fetch=substitutions`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**TheSubstitutionsRelatedToTheTeamWithIDTeamId**](TheSubstitutionsRelatedToTheTeamWithIDTeamId.md) |  | [optional] 

## Example

```python
from openapi_client.models.substitution_fetch import SubstitutionFetch

# TODO update the JSON string below
json = "{}"
# create an instance of SubstitutionFetch from a JSON string
substitution_fetch_instance = SubstitutionFetch.from_json(json)
# print the JSON string representation of the object
print(SubstitutionFetch.to_json())

# convert the object into a dict
substitution_fetch_dict = substitution_fetch_instance.to_dict()
# create an instance of SubstitutionFetch from a dict
substitution_fetch_from_dict = SubstitutionFetch.from_dict(substitution_fetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


