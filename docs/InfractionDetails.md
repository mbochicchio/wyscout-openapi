# InfractionDetails

Available when event is foul, yellow_card or red_card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opponent** | [**OpponentDetails1**](OpponentDetails1.md) |  | [optional] 
**red_card** | **bool** | If true this results in a red card | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Possible type values&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;hand_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;regular_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;violent_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;out_of_play_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;protest_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;time_lost_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;simulation_foul&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;late_card_foul&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**yellow_card** | **bool** | If true this results in a yellow card | [optional] 

## Example

```python
from openapi_client.models.infraction_details import InfractionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InfractionDetails from a JSON string
infraction_details_instance = InfractionDetails.from_json(json)
# print the JSON string representation of the object
print(InfractionDetails.to_json())

# convert the object into a dict
infraction_details_dict = infraction_details_instance.to_dict()
# create an instance of InfractionDetails from a dict
infraction_details_from_dict = InfractionDetails.from_dict(infraction_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


