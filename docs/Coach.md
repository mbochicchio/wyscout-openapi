# Coach

Retrieves information about a given coach

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_area** | [**Area**](Area.md) |  | [optional] 
**birth_date** | **str** |  | [optional] 
**current_team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;currentTeam&#x60; | [optional] 
**current_team_id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Gender&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;male&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;female&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**image_data_url** | **str** | Coach picture URL | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**passport_area** | [**Area**](Area.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;active&lt;/td&gt;&lt;td&gt;The coach is currently active&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;retired&lt;/td&gt;&lt;td&gt;The coach has retired&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;died&lt;/td&gt;&lt;td&gt;The coach is dead&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.coach import Coach

# TODO update the JSON string below
json = "{}"
# create an instance of Coach from a JSON string
coach_instance = Coach.from_json(json)
# print the JSON string representation of the object
print(Coach.to_json())

# convert the object into a dict
coach_dict = coach_instance.to_dict()
# create an instance of Coach from a dict
coach_from_dict = Coach.from_dict(coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


