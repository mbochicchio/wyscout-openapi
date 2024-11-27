# PlayerFixtures

Returns info about the given player fixture

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[TheMatchesObject]**](TheMatchesObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_fixtures import PlayerFixtures

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerFixtures from a JSON string
player_fixtures_instance = PlayerFixtures.from_json(json)
# print the JSON string representation of the object
print(PlayerFixtures.to_json())

# convert the object into a dict
player_fixtures_dict = player_fixtures_instance.to_dict()
# create an instance of PlayerFixtures from a dict
player_fixtures_from_dict = PlayerFixtures.from_dict(player_fixtures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


