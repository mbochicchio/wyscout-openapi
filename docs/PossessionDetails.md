# PossessionDetails

Based on the type of the possession, some events would also additional payload with context for this possession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack** | [**AttackDetails**](AttackDetails.md) |  | [optional] 
**duration** | **str** |  | [optional] 
**end_location** | [**PossessionEndLocation**](PossessionEndLocation.md) |  | [optional] 
**event_index** | **int** |  | [optional] 
**events_number** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**start_location** | [**PossessionStartLocation**](PossessionStartLocation.md) |  | [optional] 
**team** | [**TeamDetails**](TeamDetails.md) |  | [optional] 
**types** | **List[str]** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Possible type values&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;corner&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;counterattack&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;set_piece_attack&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;attack&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;free_kick&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;direct_free_kick&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;penalty&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;throw_in&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;free_kick_cross&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;transition_low&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;transition_medium&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;transition_high&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.possession_details import PossessionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PossessionDetails from a JSON string
possession_details_instance = PossessionDetails.from_json(json)
# print the JSON string representation of the object
print(PossessionDetails.to_json())

# convert the object into a dict
possession_details_dict = possession_details_instance.to_dict()
# create an instance of PossessionDetails from a dict
possession_details_from_dict = PossessionDetails.from_dict(possession_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


