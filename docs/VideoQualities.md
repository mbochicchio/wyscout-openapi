# VideoQualities

Information about the existing qualities for a given video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullhd** | [**TheFullhdObject**](TheFullhdObject.md) |  | [optional] 
**hd** | [**TheHdObject**](TheHdObject.md) |  | [optional] 
**lq** | [**TheLqObject**](TheLqObject.md) |  | [optional] 
**match_id** | **int** |  | [optional] 
**sd** | [**TheSdObject**](TheSdObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.video_qualities import VideoQualities

# TODO update the JSON string below
json = "{}"
# create an instance of VideoQualities from a JSON string
video_qualities_instance = VideoQualities.from_json(json)
# print the JSON string representation of the object
print(VideoQualities.to_json())

# convert the object into a dict
video_qualities_dict = video_qualities_instance.to_dict()
# create an instance of VideoQualities from a dict
video_qualities_from_dict = VideoQualities.from_dict(video_qualities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


