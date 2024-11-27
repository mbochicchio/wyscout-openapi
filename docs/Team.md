# Team

Data about the given team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | [**Area**](Area.md) |  | [optional] 
**category** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Category&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;default&lt;/td&gt;&lt;td&gt;The team competes in competitions with no age limitations&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;youth&lt;/td&gt;&lt;td&gt;The team competes in youth competitions&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**children** | [**List[RelatedTeamsInner]**](RelatedTeamsInner.md) | This field is present if team has related teams | [optional] 
**city** | **str** |  | [optional] 
**gender** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Gender&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;male&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;female&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**image_data_url** | **str** | Team picture URL | [optional] 
**name** | **str** |  | [optional] 
**official_name** | **str** |  | [optional] 
**parent** | [**ParentTeam**](ParentTeam.md) |  | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Type&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;club&lt;/td&gt;&lt;td&gt;The team competes in club competitions&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;national&lt;/td&gt;&lt;td&gt;The team competes in national competitions&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


