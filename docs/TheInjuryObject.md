# TheInjuryObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**games_missed** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**injury_localization** | **str** |  | [optional] 
**injury_side** | **str** |  | [optional] 
**injury_type** | **str** |  | [optional] 
**is_disease** | **int** |  | [optional] 
**player_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_injury_object import TheInjuryObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheInjuryObject from a JSON string
the_injury_object_instance = TheInjuryObject.from_json(json)
# print the JSON string representation of the object
print(TheInjuryObject.to_json())

# convert the object into a dict
the_injury_object_dict = the_injury_object_instance.to_dict()
# create an instance of TheInjuryObject from a dict
the_injury_object_from_dict = TheInjuryObject.from_dict(the_injury_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


