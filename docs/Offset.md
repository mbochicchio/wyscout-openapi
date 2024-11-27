# Offset

Information about a video offset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | [optional] 
**start** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.offset import Offset

# TODO update the JSON string below
json = "{}"
# create an instance of Offset from a JSON string
offset_instance = Offset.from_json(json)
# print the JSON string representation of the object
print(Offset.to_json())

# convert the object into a dict
offset_dict = offset_instance.to_dict()
# create an instance of Offset from a dict
offset_from_dict = Offset.from_dict(offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


