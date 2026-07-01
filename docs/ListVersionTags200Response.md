# ListVersionTags200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[ListVersionTags200ResponseTagsInner]**](ListVersionTags200ResponseTagsInner.md) |  | 

## Example

```python
from px0.models.list_version_tags200_response import ListVersionTags200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListVersionTags200Response from a JSON string
list_version_tags200_response_instance = ListVersionTags200Response.from_json(json)
# print the JSON string representation of the object
print(ListVersionTags200Response.to_json())

# convert the object into a dict
list_version_tags200_response_dict = list_version_tags200_response_instance.to_dict()
# create an instance of ListVersionTags200Response from a dict
list_version_tags200_response_from_dict = ListVersionTags200Response.from_dict(list_version_tags200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


