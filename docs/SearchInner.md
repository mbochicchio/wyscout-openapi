# SearchInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | [**Area**](Area.md) |  | [optional] 
**category** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Category&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;default&lt;/td&gt;&lt;td&gt;The team competes in competitions with no age limitations&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;youth&lt;/td&gt;&lt;td&gt;The team competes in youth competitions&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**division_level** | **int** | From 1 (highest) to 5 (lowest) (0 &#x3D; no info) | [optional] 
**format** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Format&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Domestic cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Domestic league&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Domestic super cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;International cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;International super cup&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gender** | **str** | male, female | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Type&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;club&lt;/td&gt;&lt;td&gt;This competition is reserved to club teams&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;international&lt;/td&gt;&lt;td&gt;This competition is reserved to national teams&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**wy_id** | **int** |  | [optional] 
**children** | [**List[RelatedTeamsInner]**](RelatedTeamsInner.md) | This field is present if team has related teams | [optional] 
**city** | **str** |  | [optional] 
**image_data_url** | **str** | Available with querystring param &#x60;imageDataURL&#x3D;true&#x60; | [optional] 
**official_name** | **str** |  | [optional] 
**parent** | [**ParentTeam**](ParentTeam.md) |  | [optional] 
**birth_area** | [**Area**](Area.md) |  | [optional] 
**birth_date** | **str** |  | [optional] 
**current_national_team_id** | **int** | Unique ID of the national team this player is currently playing for (if exists) | [optional] 
**current_team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;currentTeam&#x60; | [optional] 
**current_team_id** | **int** | Unique ID of the club team this player is currently playing for | [optional] 
**first_name** | **str** |  | [optional] 
**foot** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Foot&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;right&lt;/td&gt;&lt;td&gt;Uses right foot as main foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;left&lt;/td&gt;&lt;td&gt;Uses left foot as main foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;both&lt;/td&gt;&lt;td&gt;Uses both left and right foot indifferently&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**height** | **int** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**passport_area** | [**Area**](Area.md) |  | [optional] 
**role** | [**MainRole**](MainRole.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;active&lt;/td&gt;&lt;td&gt;The referee is currently active&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;retired&lt;/td&gt;&lt;td&gt;The referee has retired&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;died&lt;/td&gt;&lt;td&gt;The referee is dead&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**weight** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.search_inner import SearchInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchInner from a JSON string
search_inner_instance = SearchInner.from_json(json)
# print the JSON string representation of the object
print(SearchInner.to_json())

# convert the object into a dict
search_inner_dict = search_inner_instance.to_dict()
# create an instance of SearchInner from a dict
search_inner_from_dict = SearchInner.from_dict(search_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


