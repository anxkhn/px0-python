# APIKeyCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique API Key identifier. | 
**name** | **str** | Human-readable name of the key. | 
**key** | **str** | The fully generated secure raw API Key string. This is returned ONLY ONCE. | 
**key_prefix** | **str** | Identifying prefix of the key. | 
**operation** | **str** |  | 
**created_at** | **datetime** | Timestamp of creation. | 

## Example

```python
from px0.models.api_key_created_response import APIKeyCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreatedResponse from a JSON string
api_key_created_response_instance = APIKeyCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(APIKeyCreatedResponse.to_json())

# convert the object into a dict
api_key_created_response_dict = api_key_created_response_instance.to_dict()
# create an instance of APIKeyCreatedResponse from a dict
api_key_created_response_from_dict = APIKeyCreatedResponse.from_dict(api_key_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


