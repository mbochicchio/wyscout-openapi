# ThePlayerObject1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | **int** |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**player_id** | **int** |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_player_object1 import ThePlayerObject1

# TODO update the JSON string below
json = "{}"
# create an instance of ThePlayerObject1 from a JSON string
the_player_object1_instance = ThePlayerObject1.from_json(json)
# print the JSON string representation of the object
print(ThePlayerObject1.to_json())

# convert the object into a dict
the_player_object1_dict = the_player_object1_instance.to_dict()
# create an instance of ThePlayerObject1 from a dict
the_player_object1_from_dict = ThePlayerObject1.from_dict(the_player_object1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


