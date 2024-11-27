# MainRole

<table><thead><tr><th>Name</th><th>Code2</th><th>Code3</th></tr></thead><tbody><tr><td>Goalkeeper</td><td>GK</td><td>GKP</td></tr><tr><td>Defender</td><td>DF</td><td>DEF</td></tr><tr><td>Midfielder</td><td>MD</td><td>MID</td></tr><tr><td>Forward</td><td>FW</td><td>FWD</td></tr></tbody></table>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code2** | **str** |  | [optional] 
**code3** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.main_role import MainRole

# TODO update the JSON string below
json = "{}"
# create an instance of MainRole from a JSON string
main_role_instance = MainRole.from_json(json)
# print the JSON string representation of the object
print(MainRole.to_json())

# convert the object into a dict
main_role_dict = main_role_instance.to_dict()
# create an instance of MainRole from a dict
main_role_from_dict = MainRole.from_dict(main_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


