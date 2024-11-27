# Player

Retrieves information about a given player

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_area** | [**Area**](Area.md) |  | [optional] 
**birth_date** | **str** |  | [optional] 
**current_national_team_id** | **int** | Unique ID of the national team this player is currently playing for (if exists) | [optional] 
**current_team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;currentTeam&#x60; | [optional] 
**current_team_id** | **int** | Unique ID of the club team this player is currently playing for | [optional] 
**first_name** | **str** |  | [optional] 
**foot** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Foot&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;right&lt;/td&gt;&lt;td&gt;Uses right foot as main foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;left&lt;/td&gt;&lt;td&gt;Uses left foot as main foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;both&lt;/td&gt;&lt;td&gt;Uses both left and right foot indifferently&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gender** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Gender&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;male&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;female&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**height** | **int** |  | [optional] 
**image_data_url** | **str** | Player picture URL | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**passport_area** | [**Area**](Area.md) |  | [optional] 
**role** | [**MainRole**](MainRole.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;active&lt;/td&gt;&lt;td&gt;The player is currently active&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;retired&lt;/td&gt;&lt;td&gt;The player has retired&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;died&lt;/td&gt;&lt;td&gt;The player is dead&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**weight** | **int** |  | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print(Player.to_json())

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_from_dict = Player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


