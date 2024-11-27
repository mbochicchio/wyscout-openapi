# VideoOffsets

Information about the given video periods offsets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | [**Match**](Match.md) |  | [optional] 
**offsets** | [**Offsets**](Offsets.md) |  | [optional] 

## Example

```python
from openapi_client.models.video_offsets import VideoOffsets

# TODO update the JSON string below
json = "{}"
# create an instance of VideoOffsets from a JSON string
video_offsets_instance = VideoOffsets.from_json(json)
# print the JSON string representation of the object
print(VideoOffsets.to_json())

# convert the object into a dict
video_offsets_dict = video_offsets_instance.to_dict()
# create an instance of VideoOffsets from a dict
video_offsets_from_dict = VideoOffsets.from_dict(video_offsets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


