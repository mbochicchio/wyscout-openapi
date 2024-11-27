# CarryDetails

Available when event is a carry with the ball

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_location** | [**CarryEndLocation**](CarryEndLocation.md) |  | [optional] 
**progression** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.carry_details import CarryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CarryDetails from a JSON string
carry_details_instance = CarryDetails.from_json(json)
# print the JSON string representation of the object
print(CarryDetails.to_json())

# convert the object into a dict
carry_details_dict = carry_details_instance.to_dict()
# create an instance of CarryDetails from a dict
carry_details_from_dict = CarryDetails.from_dict(carry_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


