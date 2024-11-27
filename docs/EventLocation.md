# EventLocation

The locations are measured in percentages of the field, from 0 to 100. The (0, 0) point represents the left corner point near own goal, the (0, 100) point, the right corner point near own goal, the (100, 0), the left corner point near opponent goal, the (100, 100), the right corner point near opponent goal. The (50, 50) point is the center of the field. or events where location is not tagged, it can be set to null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** |  | [optional] 
**y** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.event_location import EventLocation

# TODO update the JSON string below
json = "{}"
# create an instance of EventLocation from a JSON string
event_location_instance = EventLocation.from_json(json)
# print the JSON string representation of the object
print(EventLocation.to_json())

# convert the object into a dict
event_location_dict = event_location_instance.to_dict()
# create an instance of EventLocation from a dict
event_location_from_dict = EventLocation.from_dict(event_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


