# CreateAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name for the key. | 
**org_id** | **str** |  | 
**team_ids** | **List[str]** |  | [optional] 
**operation** | **str** |  | [optional] [default to 'read_render']

## Example

```python
from px0.models.create_api_key_request import CreateAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIKeyRequest from a JSON string
create_api_key_request_instance = CreateAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAPIKeyRequest.to_json())

# convert the object into a dict
create_api_key_request_dict = create_api_key_request_instance.to_dict()
# create an instance of CreateAPIKeyRequest from a dict
create_api_key_request_from_dict = CreateAPIKeyRequest.from_dict(create_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


