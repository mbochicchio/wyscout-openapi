# SeasonAssistmen

Returns info about the given season assistmen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) |  | [optional] 
**competition_id** | **int** |  | [optional] 
**players** | [**List[ThePlayerObject]**](ThePlayerObject.md) |  | [optional] 
**season** | [**Season**](Season.md) |  | [optional] 
**season_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.season_assistmen import SeasonAssistmen

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonAssistmen from a JSON string
season_assistmen_instance = SeasonAssistmen.from_json(json)
# print the JSON string representation of the object
print(SeasonAssistmen.to_json())

# convert the object into a dict
season_assistmen_dict = season_assistmen_instance.to_dict()
# create an instance of SeasonAssistmen from a dict
season_assistmen_from_dict = SeasonAssistmen.from_dict(season_assistmen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


