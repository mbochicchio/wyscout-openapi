# AResponseElementObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaches** | [**CoachesFetch**](CoachesFetch.md) |  | [optional] 
**events** | [**List[MatchEvent]**](MatchEvent.md) |  | [optional] 
**formations** | [**FormationsFetch**](FormationsFetch.md) |  | [optional] 
**match** | [**Match**](Match.md) | Available with querystring param &#x60;fetch&#x3D;match&#x60; | [optional] 
**players** | [**PlayersFetch**](PlayersFetch.md) |  | [optional] 
**referees** | [**List[TheRefereeObject]**](TheRefereeObject.md) | Available with querystring param &#x60;fetch&#x3D;referees&#x60; | [optional] 
**substitutions** | [**SubstitutionFetch**](SubstitutionFetch.md) |  | [optional] 
**teams** | [**TeamsFetch**](TeamsFetch.md) |  | [optional] 

## Example

```python
from openapi_client.models.a_response_element_object import AResponseElementObject

# TODO update the JSON string below
json = "{}"
# create an instance of AResponseElementObject from a JSON string
a_response_element_object_instance = AResponseElementObject.from_json(json)
# print the JSON string representation of the object
print(AResponseElementObject.to_json())

# convert the object into a dict
a_response_element_object_dict = a_response_element_object_instance.to_dict()
# create an instance of AResponseElementObject from a dict
a_response_element_object_from_dict = AResponseElementObject.from_dict(a_response_element_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


