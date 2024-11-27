# PositionOfThePlayer

<table><thead><tr><th>Name</th><th>Code</th></tr></thead><tbody><tr><td>Goalkeeper</td><td>gk</td></tr><tr><td>Right Back</td><td>rb</td></tr><tr><td>Right Centre Back</td><td>rcb</td></tr><tr><td>Left Centre Back</td><td>lcb</td></tr><tr><td>Left Back</td><td>lb</td></tr><tr><td>Right Winger</td><td>rw</td></tr><tr><td>Right Centre Midfielder</td><td>rcmf</td></tr><tr><td>Left Centre Midfielder</td><td>lcmf</td></tr><tr><td>Left Winger</td><td>lw</td></tr><tr><td>Second Striker</td><td>ss</td></tr><tr><td>Striker</td><td>cf</td></tr><tr><td>Attacking Midfielder</td><td>amf</td></tr><tr><td>Right Centre Midfielder</td><td>rcmf3</td></tr><tr><td>Defensive Midfielder</td><td>dmf</td></tr><tr><td>Left Centre Midfielder</td><td>lcmf3</td></tr><tr><td>Right Defensive Midfielder</td><td>rdmf</td></tr><tr><td>Left Defensive Midfielder</td><td>ldmf</td></tr><tr><td>Right Attacking Midfielder</td><td>ramf</td></tr><tr><td>Left Attacking Midfielder</td><td>lamf</td></tr><tr><td>Right Wing Forward</td><td>rwf</td></tr><tr><td>Left Wing Forward</td><td>lwf</td></tr><tr><td>Right Centre Back (3 at the back)</td><td>rcb3</td></tr><tr><td>Centre Back</td><td>cb</td></tr><tr><td>Left Centre Back (3 at the back)</td><td>lcb3</td></tr><tr><td>Right Wingback</td><td>rwb</td></tr><tr><td>Left Wingback</td><td>lwb</td></tr><tr><td>Right Back (5 at the back)</td><td>rb5</td></tr><tr><td>Left Back (5 at the back)</td><td>lb5</td></tr></tbody></table>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.position_of_the_player import PositionOfThePlayer

# TODO update the JSON string below
json = "{}"
# create an instance of PositionOfThePlayer from a JSON string
position_of_the_player_instance = PositionOfThePlayer.from_json(json)
# print the JSON string representation of the object
print(PositionOfThePlayer.to_json())

# convert the object into a dict
position_of_the_player_dict = position_of_the_player_instance.to_dict()
# create an instance of PositionOfThePlayer from a dict
position_of_the_player_from_dict = PositionOfThePlayer.from_dict(position_of_the_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


