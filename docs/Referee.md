# Referee

Returns info about the given referee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_area** | [**Area**](Area.md) |  | [optional] 
**birth_date** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** | male, female | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**image_data_url** | **str** | Available with querystring param &#x60;imageDataURL&#x3D;true&#x60; | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**passport_area** | [**Area**](Area.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;active&lt;/td&gt;&lt;td&gt;The referee is currently active&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;retired&lt;/td&gt;&lt;td&gt;The referee has retired&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;died&lt;/td&gt;&lt;td&gt;The referee is dead&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.referee import Referee

# TODO update the JSON string below
json = "{}"
# create an instance of Referee from a JSON string
referee_instance = Referee.from_json(json)
# print the JSON string representation of the object
print(Referee.to_json())

# convert the object into a dict
referee_dict = referee_instance.to_dict()
# create an instance of Referee from a dict
referee_from_dict = Referee.from_dict(referee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


