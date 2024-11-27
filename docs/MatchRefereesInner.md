# MatchRefereesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referee** | [**Referee**](Referee.md) | Available with param &#x60;details&#x3D;referees&#x60; | [optional] 
**referee_id** | **int** |  | [optional] 
**role** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Role&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;referee&lt;/td&gt;&lt;td&gt;Main referee&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;firstAssistant&lt;/td&gt;&lt;td&gt;First assistant (linesman)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;secondAssistant&lt;/td&gt;&lt;td&gt;Second assistant (linesman)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;fourthOfficial&lt;/td&gt;&lt;td&gt;Fourth official&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;firstAdditionalAssistant&lt;/td&gt;&lt;td&gt;First additional assistant&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;secondAdditionalAssistant&lt;/td&gt;&lt;td&gt;Second additional assistant&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.match_referees_inner import MatchRefereesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRefereesInner from a JSON string
match_referees_inner_instance = MatchRefereesInner.from_json(json)
# print the JSON string representation of the object
print(MatchRefereesInner.to_json())

# convert the object into a dict
match_referees_inner_dict = match_referees_inner_instance.to_dict()
# create an instance of MatchRefereesInner from a dict
match_referees_inner_from_dict = MatchRefereesInner.from_dict(match_referees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


