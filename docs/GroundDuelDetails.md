# GroundDuelDetails

Available when event is ground_duel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duel_type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Possible duel types&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;defensive_duel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;dribble&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;offensive_duel&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**kept_possession** | **bool** | If true this results in a kept possession | [optional] 
**opponent** | [**OpponentDetails1**](OpponentDetails1.md) |  | [optional] 
**progressed_with_ball** | **bool** | If true this progressed with ball | [optional] 
**recovered_possession** | **bool** | If true this results in a recovered possession | [optional] 
**related_duel_id** | **int** |  | [optional] 
**side** | **str** |  | [optional] 
**stopped_progress** | **bool** | If true this results in a stopped progression | [optional] 
**take_on** | **bool** | If true this results in a possession take on | [optional] 

## Example

```python
from openapi_client.models.ground_duel_details import GroundDuelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroundDuelDetails from a JSON string
ground_duel_details_instance = GroundDuelDetails.from_json(json)
# print the JSON string representation of the object
print(GroundDuelDetails.to_json())

# convert the object into a dict
ground_duel_details_dict = ground_duel_details_instance.to_dict()
# create an instance of GroundDuelDetails from a dict
ground_duel_details_from_dict = GroundDuelDetails.from_dict(ground_duel_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


