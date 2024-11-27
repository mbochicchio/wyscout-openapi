# Offsets

Information about a video offsets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1_h** | [**Offset**](Offset.md) |  | [optional] 
**var_2_h** | [**Offset**](Offset.md) |  | [optional] 
**e1** | [**Offset**](Offset.md) |  | [optional] 
**e2** | [**Offset**](Offset.md) |  | [optional] 
**p** | [**Offset**](Offset.md) |  | [optional] 

## Example

```python
from openapi_client.models.offsets import Offsets

# TODO update the JSON string below
json = "{}"
# create an instance of Offsets from a JSON string
offsets_instance = Offsets.from_json(json)
# print the JSON string representation of the object
print(Offsets.to_json())

# convert the object into a dict
offsets_dict = offsets_instance.to_dict()
# create an instance of Offsets from a dict
offsets_from_dict = Offsets.from_dict(offsets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


