# TheMatchGoalObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute** | **int** |  | [optional] 
**period** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Period&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;FirstHalf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;SecondHalf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ExtraFirstHalf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ExtraSecondHalf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Shootout&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**player** | [**Player**](Player.md) | Available with querystring param &#x60;details&#x3D;players&#x60; | [optional] 
**player_id** | **int** |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;teams&#x60; | [optional] 
**team_id** | **int** |  | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Type&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;goal&lt;/td&gt;&lt;td&gt;Generic goal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;own&lt;/td&gt;&lt;td&gt;Own goal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;penalty&lt;/td&gt;&lt;td&gt;Penalty goal&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.the_match_goal_object import TheMatchGoalObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheMatchGoalObject from a JSON string
the_match_goal_object_instance = TheMatchGoalObject.from_json(json)
# print the JSON string representation of the object
print(TheMatchGoalObject.to_json())

# convert the object into a dict
the_match_goal_object_dict = the_match_goal_object_instance.to_dict()
# create an instance of TheMatchGoalObject from a dict
the_match_goal_object_from_dict = TheMatchGoalObject.from_dict(the_match_goal_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


