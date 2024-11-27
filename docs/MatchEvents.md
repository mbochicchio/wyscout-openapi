# MatchEvents



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[AResponseElementObject]**](AResponseElementObject.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.match_events import MatchEvents

# TODO update the JSON string below
json = "{}"
# create an instance of MatchEvents from a JSON string
match_events_instance = MatchEvents.from_json(json)
# print the JSON string representation of the object
print(MatchEvents.to_json())

# convert the object into a dict
match_events_dict = match_events_instance.to_dict()
# create an instance of MatchEvents from a dict
match_events_from_dict = MatchEvents.from_dict(match_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


