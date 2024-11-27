# AerialDuelDetails

Available when event is aerial duel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_touch** | **bool** | Aerial duel won. An aerial duel is considered won in favor of the player who touches the ball first, no matter what happens next. | [optional] 
**height** | **int** |  | [optional] 
**opponent** | [**OpponentDetails**](OpponentDetails.md) |  | [optional] 
**related_duel_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.aerial_duel_details import AerialDuelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AerialDuelDetails from a JSON string
aerial_duel_details_instance = AerialDuelDetails.from_json(json)
# print the JSON string representation of the object
print(AerialDuelDetails.to_json())

# convert the object into a dict
aerial_duel_details_dict = aerial_duel_details_instance.to_dict()
# create an instance of AerialDuelDetails from a dict
aerial_duel_details_from_dict = AerialDuelDetails.from_dict(aerial_duel_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


