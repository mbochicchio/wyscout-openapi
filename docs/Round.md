# Round

Retrieves information about a given round

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;details&#x3D;competition&#x60; | [optional] 
**competition_id** | **int** |  | [optional] 
**end_date** | **str** |  | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**name** | **str** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;details&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Type&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;table&lt;/td&gt;&lt;td&gt;The round contains a table (group or league table)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;cup&lt;/td&gt;&lt;td&gt;The round contains a cup structure (knock-out)&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.round import Round

# TODO update the JSON string below
json = "{}"
# create an instance of Round from a JSON string
round_instance = Round.from_json(json)
# print the JSON string representation of the object
print(Round.to_json())

# convert the object into a dict
round_dict = round_instance.to_dict()
# create an instance of Round from a dict
round_from_dict = Round.from_dict(round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


