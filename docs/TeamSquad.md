# TeamSquad

Returns the list of players currently playing for the given team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach** | [**List[Coach]**](Coach.md) |  | [optional] 
**squad** | [**List[Player]**](Player.md) |  | [optional] 
**staff** | [**List[Coach]**](Coach.md) |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;fetch&#x3D;team&#x60; | [optional] 

## Example

```python
from openapi_client.models.team_squad import TeamSquad

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSquad from a JSON string
team_squad_instance = TeamSquad.from_json(json)
# print the JSON string representation of the object
print(TeamSquad.to_json())

# convert the object into a dict
team_squad_dict = team_squad_instance.to_dict()
# create an instance of TeamSquad from a dict
team_squad_from_dict = TeamSquad.from_dict(team_squad_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


