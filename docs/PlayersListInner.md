# PlayersListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**Player**](Player.md) |  | [optional] 
**player_id** | **int** |  | [optional] 
**position** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Name&lt;/th&gt;&lt;th&gt;Code&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Goalkeeper&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Back&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Centre Back&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Centre Back&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Back&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Winger&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Centre Midfielder&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Centre Midfielder&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Winger&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Second Striker&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Striker&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Attacking Midfielder&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Centre Midfielder&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Defensive Midfielder&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Centre Midfielder&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Defensive Midfielder&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Defensive Midfielder&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Attacking Midfielder&lt;/td&gt;&lt;td&gt;ramf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Attacking Midfielder&lt;/td&gt;&lt;td&gt;lamf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Wing Forward&lt;/td&gt;&lt;td&gt;rwf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Wing Forward&lt;/td&gt;&lt;td&gt;lwf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Centre Back (3 at the back)&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Centre Back&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Centre Back (3 at the back)&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Wingback&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Wingback&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Right Back (5 at the back)&lt;/td&gt;&lt;td&gt;rb5&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Left Back (5 at the back)&lt;/td&gt;&lt;td&gt;lb5&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 

## Example

```python
from openapi_client.models.players_list_inner import PlayersListInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlayersListInner from a JSON string
players_list_inner_instance = PlayersListInner.from_json(json)
# print the JSON string representation of the object
print(PlayersListInner.to_json())

# convert the object into a dict
players_list_inner_dict = players_list_inner_instance.to_dict()
# create an instance of PlayersListInner from a dict
players_list_inner_from_dict = PlayersListInner.from_dict(players_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


