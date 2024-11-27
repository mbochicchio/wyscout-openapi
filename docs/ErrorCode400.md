# ErrorCode400

HTTP status error code 400

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorObject**](ErrorObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.error_code400 import ErrorCode400

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorCode400 from a JSON string
error_code400_instance = ErrorCode400.from_json(json)
# print the JSON string representation of the object
print(ErrorCode400.to_json())

# convert the object into a dict
error_code400_dict = error_code400_instance.to_dict()
# create an instance of ErrorCode400 from a dict
error_code400_from_dict = ErrorCode400.from_dict(error_code400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


