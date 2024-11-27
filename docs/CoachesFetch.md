# CoachesFetch

Available with querystring param `fetch=coaches`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**TeamCoach**](TeamCoach.md) |  | [optional] 

## Example

```python
from openapi_client.models.coaches_fetch import CoachesFetch

# TODO update the JSON string below
json = "{}"
# create an instance of CoachesFetch from a JSON string
coaches_fetch_instance = CoachesFetch.from_json(json)
# print the JSON string representation of the object
print(CoachesFetch.to_json())

# convert the object into a dict
coaches_fetch_dict = coaches_fetch_instance.to_dict()
# create an instance of CoachesFetch from a dict
coaches_fetch_from_dict = CoachesFetch.from_dict(coaches_fetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


