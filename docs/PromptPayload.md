# PromptPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique payload identifier. | 
**prompt_id** | **str** | Reference to parent Prompt ID. | 
**name** | **str** | Optional name for this sample payload. | [optional] 
**variables** | **object** | Standard JSON object containing variable names and sample values. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from px0.models.prompt_payload import PromptPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PromptPayload from a JSON string
prompt_payload_instance = PromptPayload.from_json(json)
# print the JSON string representation of the object
print(PromptPayload.to_json())

# convert the object into a dict
prompt_payload_dict = prompt_payload_instance.to_dict()
# create an instance of PromptPayload from a dict
prompt_payload_from_dict = PromptPayload.from_dict(prompt_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


