# ListVersions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[PromptVersion]**](PromptVersion.md) |  | 

## Example

```python
from px0.models.list_versions200_response import ListVersions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListVersions200Response from a JSON string
list_versions200_response_instance = ListVersions200Response.from_json(json)
# print the JSON string representation of the object
print(ListVersions200Response.to_json())

# convert the object into a dict
list_versions200_response_dict = list_versions200_response_instance.to_dict()
# create an instance of ListVersions200Response from a dict
list_versions200_response_from_dict = ListVersions200Response.from_dict(list_versions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


