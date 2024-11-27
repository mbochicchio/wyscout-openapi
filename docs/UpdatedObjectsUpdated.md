# UpdatedObjectsUpdated

Info about the recently updated resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**TheResourceObject**](TheResourceObject.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.updated_objects_updated import UpdatedObjectsUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedObjectsUpdated from a JSON string
updated_objects_updated_instance = UpdatedObjectsUpdated.from_json(json)
# print the JSON string representation of the object
print(UpdatedObjectsUpdated.to_json())

# convert the object into a dict
updated_objects_updated_dict = updated_objects_updated_instance.to_dict()
# create an instance of UpdatedObjectsUpdated from a dict
updated_objects_updated_from_dict = UpdatedObjectsUpdated.from_dict(updated_objects_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


