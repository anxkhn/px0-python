# DiffVersions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_version** | **int** |  | 
**to_version** | **int** |  | 
**from_template** | **str** |  | 
**to_template** | **str** |  | 
**diff** | **str** |  | 

## Example

```python
from px0.models.diff_versions200_response import DiffVersions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiffVersions200Response from a JSON string
diff_versions200_response_instance = DiffVersions200Response.from_json(json)
# print the JSON string representation of the object
print(DiffVersions200Response.to_json())

# convert the object into a dict
diff_versions200_response_dict = diff_versions200_response_instance.to_dict()
# create an instance of DiffVersions200Response from a dict
diff_versions200_response_from_dict = DiffVersions200Response.from_dict(diff_versions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


