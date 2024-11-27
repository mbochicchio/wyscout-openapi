# SeasonTransfers

Retrieves all the transfer's information for the given season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer** | [**List[TheTransferObject]**](TheTransferObject.md) |  | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.season_transfers import SeasonTransfers

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonTransfers from a JSON string
season_transfers_instance = SeasonTransfers.from_json(json)
# print the JSON string representation of the object
print(SeasonTransfers.to_json())

# convert the object into a dict
season_transfers_dict = season_transfers_instance.to_dict()
# create an instance of SeasonTransfers from a dict
season_transfers_from_dict = SeasonTransfers.from_dict(season_transfers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


