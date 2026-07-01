# UpdatePromptPayloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional name for this sample payload. | [optional] 
**variables** | **object** | JSON object containing variable names and sample values. | [optional] 

## Example

```python
from px0.models.update_prompt_payload_request import UpdatePromptPayloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePromptPayloadRequest from a JSON string
update_prompt_payload_request_instance = UpdatePromptPayloadRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePromptPayloadRequest.to_json())

# convert the object into a dict
update_prompt_payload_request_dict = update_prompt_payload_request_instance.to_dict()
# create an instance of UpdatePromptPayloadRequest from a dict
update_prompt_payload_request_from_dict = UpdatePromptPayloadRequest.from_dict(update_prompt_payload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


