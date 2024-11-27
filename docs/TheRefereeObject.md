# TheRefereeObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referee_id** | **int** |  | [optional] 
**role** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Role&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;referee&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;firstAssistant&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;secondAssistant&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;fourthOfficial&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.the_referee_object import TheRefereeObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheRefereeObject from a JSON string
the_referee_object_instance = TheRefereeObject.from_json(json)
# print the JSON string representation of the object
print(TheRefereeObject.to_json())

# convert the object into a dict
the_referee_object_dict = the_referee_object_instance.to_dict()
# create an instance of TheRefereeObject from a dict
the_referee_object_from_dict = TheRefereeObject.from_dict(the_referee_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


