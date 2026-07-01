# CreatePromptPayloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **object** | JSON object containing variable names and sample values. | 

## Example

```python
from px0.models.create_prompt_payload_request import CreatePromptPayloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePromptPayloadRequest from a JSON string
create_prompt_payload_request_instance = CreatePromptPayloadRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePromptPayloadRequest.to_json())

# convert the object into a dict
create_prompt_payload_request_dict = create_prompt_payload_request_instance.to_dict()
# create an instance of CreatePromptPayloadRequest from a dict
create_prompt_payload_request_from_dict = CreatePromptPayloadRequest.from_dict(create_prompt_payload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


