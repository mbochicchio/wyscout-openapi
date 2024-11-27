# MatchPlayersAdvancedStats

Returns advanced statistics of all players in a specific match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | [**List[PlayerMatchAdvancedStats]**](PlayerMatchAdvancedStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.match_players_advanced_stats import MatchPlayersAdvancedStats

# TODO update the JSON string below
json = "{}"
# create an instance of MatchPlayersAdvancedStats from a JSON string
match_players_advanced_stats_instance = MatchPlayersAdvancedStats.from_json(json)
# print the JSON string representation of the object
print(MatchPlayersAdvancedStats.to_json())

# convert the object into a dict
match_players_advanced_stats_dict = match_players_advanced_stats_instance.to_dict()
# create an instance of MatchPlayersAdvancedStats from a dict
match_players_advanced_stats_from_dict = MatchPlayersAdvancedStats.from_dict(match_players_advanced_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


