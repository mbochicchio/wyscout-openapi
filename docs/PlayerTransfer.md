# PlayerTransfer

Returns info about the given players transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**Player**](Player.md) | Available with querystring param &#x60;fetch&#x3D;player&#x60; | [optional] 
**transfer** | [**List[TheTransferObject1]**](TheTransferObject1.md) | List of transfers related to a given player | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.player_transfer import PlayerTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerTransfer from a JSON string
player_transfer_instance = PlayerTransfer.from_json(json)
# print the JSON string representation of the object
print(PlayerTransfer.to_json())

# convert the object into a dict
player_transfer_dict = player_transfer_instance.to_dict()
# create an instance of PlayerTransfer from a dict
player_transfer_from_dict = PlayerTransfer.from_dict(player_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


