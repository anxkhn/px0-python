# SetVersionTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Tag string (alphanumeric, dots, dashes, underscores). | 

## Example

```python
from px0.models.set_version_tag_request import SetVersionTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetVersionTagRequest from a JSON string
set_version_tag_request_instance = SetVersionTagRequest.from_json(json)
# print the JSON string representation of the object
print(SetVersionTagRequest.to_json())

# convert the object into a dict
set_version_tag_request_dict = set_version_tag_request_instance.to_dict()
# create an instance of SetVersionTagRequest from a dict
set_version_tag_request_from_dict = SetVersionTagRequest.from_dict(set_version_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


