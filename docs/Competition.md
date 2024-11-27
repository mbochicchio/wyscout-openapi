# Competition

Retrieves information about a given competition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | [**Area**](Area.md) |  | [optional] 
**category** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Category&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;default&lt;/td&gt;&lt;td&gt;All players with no age restriction&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U13&lt;/td&gt;&lt;td&gt;All players under the age of 13&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U14&lt;/td&gt;&lt;td&gt;All players under the age of 14&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U15&lt;/td&gt;&lt;td&gt;All players under the age of 15&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U16&lt;/td&gt;&lt;td&gt;All players under the age of 16&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U17&lt;/td&gt;&lt;td&gt;All players under the age of 17&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U18&lt;/td&gt;&lt;td&gt;All players under the age of 18&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U19&lt;/td&gt;&lt;td&gt;All players under the age of 19&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U20&lt;/td&gt;&lt;td&gt;All players under the age of 20&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U21&lt;/td&gt;&lt;td&gt;All players under the age of 21&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;U23&lt;/td&gt;&lt;td&gt;All players under the age of 23&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**division_level** | **int** | From 1 (highest) to 5 (lowest) (0 &#x3D; no info) | [optional] 
**format** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Format&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Domestic cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Domestic league&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Domestic super cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;International cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;International super cup&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gender** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Gender&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;male&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;female&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Type&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;club&lt;/td&gt;&lt;td&gt;This competition is reserved to club teams&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;international&lt;/td&gt;&lt;td&gt;This competition is reserved to national teams&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.competition import Competition

# TODO update the JSON string below
json = "{}"
# create an instance of Competition from a JSON string
competition_instance = Competition.from_json(json)
# print the JSON string representation of the object
print(Competition.to_json())

# convert the object into a dict
competition_dict = competition_instance.to_dict()
# create an instance of Competition from a dict
competition_from_dict = Competition.from_dict(competition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


