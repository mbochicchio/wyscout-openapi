# ThePlayerObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **int** |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**player_id** | **int** |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_player_object import ThePlayerObject

# TODO update the JSON string below
json = "{}"
# create an instance of ThePlayerObject from a JSON string
the_player_object_instance = ThePlayerObject.from_json(json)
# print the JSON string representation of the object
print(ThePlayerObject.to_json())

# convert the object into a dict
the_player_object_dict = the_player_object_instance.to_dict()
# create an instance of ThePlayerObject from a dict
the_player_object_from_dict = ThePlayerObject.from_dict(the_player_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


