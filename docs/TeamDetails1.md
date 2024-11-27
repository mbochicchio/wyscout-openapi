# TeamDetails1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formation** | **str** | Formation used at the time of the event | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.team_details1 import TeamDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDetails1 from a JSON string
team_details1_instance = TeamDetails1.from_json(json)
# print the JSON string representation of the object
print(TeamDetails1.to_json())

# convert the object into a dict
team_details1_dict = team_details1_instance.to_dict()
# create an instance of TeamDetails1 from a dict
team_details1_from_dict = TeamDetails1.from_dict(team_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


