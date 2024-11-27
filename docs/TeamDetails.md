# TeamDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formation** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.team_details import TeamDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDetails from a JSON string
team_details_instance = TeamDetails.from_json(json)
# print the JSON string representation of the object
print(TeamDetails.to_json())

# convert the object into a dict
team_details_dict = team_details_instance.to_dict()
# create an instance of TeamDetails from a dict
team_details_from_dict = TeamDetails.from_dict(team_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


