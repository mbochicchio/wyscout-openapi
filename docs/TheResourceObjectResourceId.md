# TheResourceObjectResourceId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpha2code** | **str** |  | [optional] 
**alpha3code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**birth_area** | [**Area**](Area.md) |  | [optional] 
**birth_date** | **str** |  | [optional] 
**current_team** | [**Team**](Team.md) | Available with querystring param &#x60;details&#x3D;currentTeam&#x60; | [optional] 
**current_team_id** | **int** | Unique ID of the club team this player is currently playing for | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Gender&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;male&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;female&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gsm_id** | **int** | This field is no more used and it will be soon deprecated | [optional] 
**image_data_url** | **str** | Team picture URL | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**passport_area** | [**Area**](Area.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**status** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;active&lt;/td&gt;&lt;td&gt;The referee is currently active&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;retired&lt;/td&gt;&lt;td&gt;The referee has retired&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;died&lt;/td&gt;&lt;td&gt;The referee is dead&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**wy_id** | **int** |  | [optional] 
**area** | [**Area**](Area.md) |  | [optional] 
**category** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Category&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;default&lt;/td&gt;&lt;td&gt;The team competes in competitions with no age limitations&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;youth&lt;/td&gt;&lt;td&gt;The team competes in youth competitions&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**division_level** | **int** | From 1 (highest) to 5 (lowest) (0 &#x3D; no info) | [optional] 
**format** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Format&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Domestic cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Domestic league&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Domestic super cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;International cup&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;International super cup&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**type** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Type&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;club&lt;/td&gt;&lt;td&gt;This competition is reserved to club teams&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;international&lt;/td&gt;&lt;td&gt;This competition is reserved to national teams&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**competition** | [**Competition**](Competition.md) | Available with querystring param &#x60;details&#x3D;competition&#x60; | [optional] 
**competition_id** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**dateutc** | **str** |  | [optional] 
**duration** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Duration&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;Regular&lt;/td&gt;&lt;td&gt;The match is over at regulation&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;GoldenGoal&lt;/td&gt;&lt;td&gt;The match is over with a golden goal during extra time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;SilverGoal&lt;/td&gt;&lt;td&gt;The match is over after the first extra time period&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ExtraTime&lt;/td&gt;&lt;td&gt;The match is over after extra time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Penalties&lt;/td&gt;&lt;td&gt;The match is over after penalties&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**gameweek** | **int** |  | [optional] 
**has_data_available** | **bool** |  | [optional] 
**label** | **str** | homeTeam – awayTeam, homeScore-awayScore | [optional] 
**referees** | [**List[MatchRefereesInner]**](MatchRefereesInner.md) |  | [optional] 
**round** | [**Round**](Round.md) | Available with querystring param &#x60;details&#x3D;round&#x60; | [optional] 
**round_id** | **int** |  | [optional] 
**season** | [**Season**](Season.md) | Available with querystring param &#x60;details&#x3D;season&#x60; | [optional] 
**season_id** | **int** |  | [optional] 
**teams_data** | [**MatchTeamsData**](MatchTeamsData.md) |  | [optional] 
**venue** | **str** |  | [optional] 
**winner** | **int** | If no winner is present, value will be &#x60;0&#x60; | [optional] 
**elements** | [**List[AResponseElementObject]**](AResponseElementObject.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**career** | [**List[TheTeamCareerArrayInner]**](TheTeamCareerArrayInner.md) |  | [optional] 
**player** | [**Player**](Player.md) | Available with querystring param &#x60;fetch&#x3D;player&#x60; | [optional] 
**injuries** | [**List[TheInjuryObject]**](TheInjuryObject.md) |  | [optional] 
**current_national_team_id** | **int** | Unique ID of the national team this player is currently playing for (if exists) | [optional] 
**foot** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Foot&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;right&lt;/td&gt;&lt;td&gt;Uses right foot as main foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;left&lt;/td&gt;&lt;td&gt;Uses left foot as main foot&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;both&lt;/td&gt;&lt;td&gt;Uses both left and right foot indifferently&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**height** | **int** |  | [optional] 
**role** | [**MainRole**](MainRole.md) |  | [optional] 
**weight** | **int** |  | [optional] 
**end_date** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**team** | [**Team**](Team.md) | Available with querystring param &#x60;fetch&#x3D;team&#x60; | [optional] 
**children** | [**List[RelatedTeamsInner]**](RelatedTeamsInner.md) | This field is present if team has related teams | [optional] 
**city** | **str** |  | [optional] 
**official_name** | **str** |  | [optional] 
**parent** | [**ParentTeam**](ParentTeam.md) |  | [optional] 
**transfer** | [**List[TheTransferObject1]**](TheTransferObject1.md) | List of transfers related to a given player | [optional] 

## Example

```python
from openapi_client.models.the_resource_object_resource_id import TheResourceObjectResourceId

# TODO update the JSON string below
json = "{}"
# create an instance of TheResourceObjectResourceId from a JSON string
the_resource_object_resource_id_instance = TheResourceObjectResourceId.from_json(json)
# print the JSON string representation of the object
print(TheResourceObjectResourceId.to_json())

# convert the object into a dict
the_resource_object_resource_id_dict = the_resource_object_resource_id_instance.to_dict()
# create an instance of TheResourceObjectResourceId from a dict
the_resource_object_resource_id_from_dict = TheResourceObjectResourceId.from_dict(the_resource_object_resource_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


