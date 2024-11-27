# MatchFullTracking

Returns link to JSON file containing Broadcast Tracking (X,Y) location data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_download_url** | **str** |  | [optional] 
**wy_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.match_full_tracking import MatchFullTracking

# TODO update the JSON string below
json = "{}"
# create an instance of MatchFullTracking from a JSON string
match_full_tracking_instance = MatchFullTracking.from_json(json)
# print the JSON string representation of the object
print(MatchFullTracking.to_json())

# convert the object into a dict
match_full_tracking_dict = match_full_tracking_instance.to_dict()
# create an instance of MatchFullTracking from a dict
match_full_tracking_from_dict = MatchFullTracking.from_dict(match_full_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


