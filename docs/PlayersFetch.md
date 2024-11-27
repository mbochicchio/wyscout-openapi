# PlayersFetch

Available with querystring param `fetch=players`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**List[Player]**](Player.md) |  | [optional] 

## Example

```python
from openapi_client.models.players_fetch import PlayersFetch

# TODO update the JSON string below
json = "{}"
# create an instance of PlayersFetch from a JSON string
players_fetch_instance = PlayersFetch.from_json(json)
# print the JSON string representation of the object
print(PlayersFetch.to_json())

# convert the object into a dict
players_fetch_dict = players_fetch_instance.to_dict()
# create an instance of PlayersFetch from a dict
players_fetch_from_dict = PlayersFetch.from_dict(players_fetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


