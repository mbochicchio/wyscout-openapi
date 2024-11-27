# AttackDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flank** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Possible flank values&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;center&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**with_goal** | **bool** | If true this is an attack with goal | [optional] 
**with_shot** | **bool** | If true this is an attack with shot | [optional] 
**with_shot_on_goal** | **bool** | If true this is an attack with shot on goal | [optional] 
**xg** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.attack_details import AttackDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AttackDetails from a JSON string
attack_details_instance = AttackDetails.from_json(json)
# print the JSON string representation of the object
print(AttackDetails.to_json())

# convert the object into a dict
attack_details_dict = attack_details_instance.to_dict()
# create an instance of AttackDetails from a dict
attack_details_from_dict = AttackDetails.from_dict(attack_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


