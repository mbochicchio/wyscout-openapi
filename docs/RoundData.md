# RoundData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[GroupStandings]**](GroupStandings.md) |  | [optional] 
**round** | [**Round**](Round.md) | Available with querystring param &#x60;details&#x3D;round&#x60; | [optional] 
**round_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.round_data import RoundData

# TODO update the JSON string below
json = "{}"
# create an instance of RoundData from a JSON string
round_data_instance = RoundData.from_json(json)
# print the JSON string representation of the object
print(RoundData.to_json())

# convert the object into a dict
round_data_dict = round_data_instance.to_dict()
# create an instance of RoundData from a dict
round_data_from_dict = RoundData.from_dict(round_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


