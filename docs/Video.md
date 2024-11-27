# Video

Data about the given video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullhd** | [**QualityUrl**](QualityUrl.md) |  | [optional] 
**hd** | [**QualityUrl**](QualityUrl.md) |  | [optional] 
**lq** | [**QualityUrl**](QualityUrl.md) |  | [optional] 
**match_id** | **int** |  | [optional] 
**offsets** | [**InformationAboutVideoOffsets**](InformationAboutVideoOffsets.md) |  | [optional] 
**sd** | [**QualityUrl**](QualityUrl.md) |  | [optional] 

## Example

```python
from openapi_client.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print(Video.to_json())

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_from_dict = Video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


