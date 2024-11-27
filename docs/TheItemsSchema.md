# TheItemsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appearances** | **int** |  | [optional] 
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;details&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**goal** | **int** |  | [optional] 
**minutes_played** | **int** |  | [optional] 
**penalties** | **int** |  | [optional] 
**player_id** | **int** |  | [optional] 
**red_cards** | **int** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;details&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**shirt_number** | **int** |  | [optional] 
**substitute_in** | **int** |  | [optional] 
**substitute_on_bench** | **int** |  | [optional] 
**substitute_out** | **int** |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;team&#x60; | [optional] 
**team_id** | **int** |  | [optional] 
**yellow_card** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_items_schema import TheItemsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TheItemsSchema from a JSON string
the_items_schema_instance = TheItemsSchema.from_json(json)
# print the JSON string representation of the object
print(TheItemsSchema.to_json())

# convert the object into a dict
the_items_schema_dict = the_items_schema_instance.to_dict()
# create an instance of TheItemsSchema from a dict
the_items_schema_from_dict = TheItemsSchema.from_dict(the_items_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


