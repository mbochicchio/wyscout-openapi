# Competitions

The list of competitions for a given area

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitions** | [**List[Competition]**](Competition.md) |  | [optional] 

## Example

```python
from openapi_client.models.competitions import Competitions

# TODO update the JSON string below
json = "{}"
# create an instance of Competitions from a JSON string
competitions_instance = Competitions.from_json(json)
# print the JSON string representation of the object
print(Competitions.to_json())

# convert the object into a dict
competitions_dict = competitions_instance.to_dict()
# create an instance of Competitions from a dict
competitions_from_dict = Competitions.from_dict(competitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


