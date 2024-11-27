# UpdatedObjectsDeleted

Info about the recently deleted resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **List[int]** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.updated_objects_deleted import UpdatedObjectsDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedObjectsDeleted from a JSON string
updated_objects_deleted_instance = UpdatedObjectsDeleted.from_json(json)
# print the JSON string representation of the object
print(UpdatedObjectsDeleted.to_json())

# convert the object into a dict
updated_objects_deleted_dict = updated_objects_deleted_instance.to_dict()
# create an instance of UpdatedObjectsDeleted from a dict
updated_objects_deleted_from_dict = UpdatedObjectsDeleted.from_dict(updated_objects_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


