# PassDetails

Available when event is a pass (and all events included in the pass definition), throw_in, goal_kick, corner (not shot) or free_kick (not free_kick_shot)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accurate** | **bool** | If true this is an accurate pass | [optional] 
**angle** | **int** | For angle, 0° represents a perfect forward pass (straight line towards the goal). Passes to the right will have positive values (90° pass is a pass strictly to the right), to the left, negative (-90° pass is a pass strictly to the left). Straight back passes will have the angle of 180°. Angle is specified in degrees, taking into account standard field dimensions | [optional] 
**end_location** | [**PassEndLocation**](PassEndLocation.md) |  | [optional] 
**length** | **float** | Length is specified in meters, taking into account standard field dimensions | [optional] 
**recipient** | [**PassRecipient**](PassRecipient.md) |  | [optional] 

## Example

```python
from openapi_client.models.pass_details import PassDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PassDetails from a JSON string
pass_details_instance = PassDetails.from_json(json)
# print the JSON string representation of the object
print(PassDetails.to_json())

# convert the object into a dict
pass_details_dict = pass_details_instance.to_dict()
# create an instance of PassDetails from a dict
pass_details_from_dict = PassDetails.from_dict(pass_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


