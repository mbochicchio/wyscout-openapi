# GoalkeeperDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.goalkeeper_details import GoalkeeperDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GoalkeeperDetails from a JSON string
goalkeeper_details_instance = GoalkeeperDetails.from_json(json)
# print the JSON string representation of the object
print(GoalkeeperDetails.to_json())

# convert the object into a dict
goalkeeper_details_dict = goalkeeper_details_instance.to_dict()
# create an instance of GoalkeeperDetails from a dict
goalkeeper_details_from_dict = GoalkeeperDetails.from_dict(goalkeeper_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


