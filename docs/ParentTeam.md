# ParentTeam

This field is present if team has a parent team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.parent_team import ParentTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ParentTeam from a JSON string
parent_team_instance = ParentTeam.from_json(json)
# print the JSON string representation of the object
print(ParentTeam.to_json())

# convert the object into a dict
parent_team_dict = parent_team_instance.to_dict()
# create an instance of ParentTeam from a dict
parent_team_from_dict = ParentTeam.from_dict(parent_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


