# ListOfStatisticsTransitions

Transition is an event where one team loses or recovers the Ball possession.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**MatchAdvancedStatsTransitions**](MatchAdvancedStatsTransitions.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_of_statistics_transitions import ListOfStatisticsTransitions

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfStatisticsTransitions from a JSON string
list_of_statistics_transitions_instance = ListOfStatisticsTransitions.from_json(json)
# print the JSON string representation of the object
print(ListOfStatisticsTransitions.to_json())

# convert the object into a dict
list_of_statistics_transitions_dict = list_of_statistics_transitions_instance.to_dict()
# create an instance of ListOfStatisticsTransitions from a dict
list_of_statistics_transitions_from_dict = ListOfStatisticsTransitions.from_dict(list_of_statistics_transitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


