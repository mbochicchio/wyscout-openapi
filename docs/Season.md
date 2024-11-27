# Season

Retrieves information about a given season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;details&#x3D;competition&#x60; | [optional] 
**competition_id** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**name** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.season import Season

# TODO update the JSON string below
json = "{}"
# create an instance of Season from a JSON string
season_instance = Season.from_json(json)
# print the JSON string representation of the object
print(Season.to_json())

# convert the object into a dict
season_dict = season_instance.to_dict()
# create an instance of Season from a dict
season_from_dict = Season.from_dict(season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


