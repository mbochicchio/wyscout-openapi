# ShotDetails

Available when event is a shot or a post-match penalty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_part** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Possible bodyPart values&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;left_foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;right_foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;head_or_other&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**goal_zone** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Label&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;bc&lt;/td&gt;&lt;td&gt;Shot blocked&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gb&lt;/td&gt;&lt;td&gt;Position: Goal low center&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gbr&lt;/td&gt;&lt;td&gt;Position: Goal low right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gc&lt;/td&gt;&lt;td&gt;Position: Goal center&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gl&lt;/td&gt;&lt;td&gt;Position: Goal center left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;glb&lt;/td&gt;&lt;td&gt;Position: Goal low left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gr&lt;/td&gt;&lt;td&gt;Position: Goal center right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gt&lt;/td&gt;&lt;td&gt;Position: Goal high center&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gtl&lt;/td&gt;&lt;td&gt;Position: Goal high left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;gtr&lt;/td&gt;&lt;td&gt;Position: Goal high right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;obr&lt;/td&gt;&lt;td&gt;Position: Out low right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ol&lt;/td&gt;&lt;td&gt;Position: Out center left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;olb&lt;/td&gt;&lt;td&gt;Position: Out low left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;or&lt;/td&gt;&lt;td&gt;Position: Out center right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ot&lt;/td&gt;&lt;td&gt;Position: Out high center&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;otl&lt;/td&gt;&lt;td&gt;Position: Out high left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;otr&lt;/td&gt;&lt;td&gt;Position: Out high right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pbr&lt;/td&gt;&lt;td&gt;Position: Post low right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pl&lt;/td&gt;&lt;td&gt;Position: Post center left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;plb&lt;/td&gt;&lt;td&gt;Position: Post low left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pr&lt;/td&gt;&lt;td&gt;Position: Post center right&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;pt&lt;/td&gt;&lt;td&gt;Position: Post high center&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ptl&lt;/td&gt;&lt;td&gt;Position: Post high left&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ptr&lt;/td&gt;&lt;td&gt;Position: Post high right&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**goalkeeper** | [**GoalkeeperDetails**](GoalkeeperDetails.md) |  | [optional] 
**goalkeeper_action_id** | **int** |  | [optional] 
**is_goal** | **bool** | If true this shot results in a goal | [optional] 
**on_target** | **bool** | If true this shot is on target | [optional] 
**post_shot_xg** | **float** |  | [optional] 
**xg** | **float** | Expected goals (xG) is a predictive ML model used to assess the likelihood of scoring for every shot made in the game | [optional] 

## Example

```python
from openapi_client.models.shot_details import ShotDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ShotDetails from a JSON string
shot_details_instance = ShotDetails.from_json(json)
# print the JSON string representation of the object
print(ShotDetails.to_json())

# convert the object into a dict
shot_details_dict = shot_details_instance.to_dict()
# create an instance of ShotDetails from a dict
shot_details_from_dict = ShotDetails.from_dict(shot_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


