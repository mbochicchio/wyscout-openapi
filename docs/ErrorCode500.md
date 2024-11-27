# ErrorCode500

HTTP status error code 500

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorObject**](ErrorObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.error_code500 import ErrorCode500

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorCode500 from a JSON string
error_code500_instance = ErrorCode500.from_json(json)
# print the JSON string representation of the object
print(ErrorCode500.to_json())

# convert the object into a dict
error_code500_dict = error_code500_instance.to_dict()
# create an instance of ErrorCode500 from a dict
error_code500_from_dict = ErrorCode500.from_dict(error_code500_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


