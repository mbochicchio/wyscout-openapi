# TheTransferObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | [optional] 
**announce_date** | **str** |  | [optional] 
**currency** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Currency&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;USD&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;EUR&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;GBP&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**end_date** | **str** |  | [optional] 
**from_team_id** | **int** |  | [optional] 
**from_team_name** | **str** |  | [optional] 
**player** | [**Player**](Player.md) | Available with querystring param &#x60;details&#x3D;player&#x60; | [optional] 
**player_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**teams_data** | [**TeamsDetails**](TeamsDetails.md) |  | [optional] 
**to_team_id** | **int** |  | [optional] 
**to_team_name** | **str** |  | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Transfer type&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Transfer&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Free Transfer&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Loan&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Back from Loan&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Free Agent&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Player Swap&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Trial&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.the_transfer_object import TheTransferObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheTransferObject from a JSON string
the_transfer_object_instance = TheTransferObject.from_json(json)
# print the JSON string representation of the object
print(TheTransferObject.to_json())

# convert the object into a dict
the_transfer_object_dict = the_transfer_object_instance.to_dict()
# create an instance of TheTransferObject from a dict
the_transfer_object_from_dict = TheTransferObject.from_dict(the_transfer_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


