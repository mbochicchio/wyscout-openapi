# ListOfStatisticsPossession

A Possession is a sequence of events with the ball of the same team. Time where the ball is out of play (either out of field or, for example, setting up a set piece) is not counted as possession for any of the two teams. Opponent actions that do not constitute a meaningful ball possession, like lost duels, missed balls and rebounds that are immediately picked up, do not break possessions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**MatchAdvancedStatsPossession**](MatchAdvancedStatsPossession.md) |  | [optional] 
**dead_time** | **str** |  | [optional] 
**total_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_of_statistics_possession import ListOfStatisticsPossession

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfStatisticsPossession from a JSON string
list_of_statistics_possession_instance = ListOfStatisticsPossession.from_json(json)
# print the JSON string representation of the object
print(ListOfStatisticsPossession.to_json())

# convert the object into a dict
list_of_statistics_possession_dict = list_of_statistics_possession_instance.to_dict()
# create an instance of ListOfStatisticsPossession from a dict
list_of_statistics_possession_from_dict = ListOfStatisticsPossession.from_dict(list_of_statistics_possession_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


