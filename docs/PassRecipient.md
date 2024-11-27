# PassRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pass_recipient import PassRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of PassRecipient from a JSON string
pass_recipient_instance = PassRecipient.from_json(json)
# print the JSON string representation of the object
print(PassRecipient.to_json())

# convert the object into a dict
pass_recipient_dict = pass_recipient_instance.to_dict()
# create an instance of PassRecipient from a dict
pass_recipient_from_dict = PassRecipient.from_dict(pass_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


