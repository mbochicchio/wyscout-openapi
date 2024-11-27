# FormationsFetch

Available with querystring param `fetch=formations`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**FormationsRelatedToTheTeamWithIDTeamId**](FormationsRelatedToTheTeamWithIDTeamId.md) |  | [optional] 

## Example

```python
from openapi_client.models.formations_fetch import FormationsFetch

# TODO update the JSON string below
json = "{}"
# create an instance of FormationsFetch from a JSON string
formations_fetch_instance = FormationsFetch.from_json(json)
# print the JSON string representation of the object
print(FormationsFetch.to_json())

# convert the object into a dict
formations_fetch_dict = formations_fetch_instance.to_dict()
# create an instance of FormationsFetch from a dict
formations_fetch_from_dict = FormationsFetch.from_dict(formations_fetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


