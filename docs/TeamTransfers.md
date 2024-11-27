# TeamTransfers



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer** | [**List[TheTransferObject]**](TheTransferObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_transfers import TeamTransfers

# TODO update the JSON string below
json = "{}"
# create an instance of TeamTransfers from a JSON string
team_transfers_instance = TeamTransfers.from_json(json)
# print the JSON string representation of the object
print(TeamTransfers.to_json())

# convert the object into a dict
team_transfers_dict = team_transfers_instance.to_dict()
# create an instance of TeamTransfers from a dict
team_transfers_from_dict = TeamTransfers.from_dict(team_transfers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


