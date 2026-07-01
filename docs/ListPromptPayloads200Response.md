# ListPromptPayloads200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payloads** | [**List[PromptPayload]**](PromptPayload.md) |  | 

## Example

```python
from px0.models.list_prompt_payloads200_response import ListPromptPayloads200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPromptPayloads200Response from a JSON string
list_prompt_payloads200_response_instance = ListPromptPayloads200Response.from_json(json)
# print the JSON string representation of the object
print(ListPromptPayloads200Response.to_json())

# convert the object into a dict
list_prompt_payloads200_response_dict = list_prompt_payloads200_response_instance.to_dict()
# create an instance of ListPromptPayloads200Response from a dict
list_prompt_payloads200_response_from_dict = ListPromptPayloads200Response.from_dict(list_prompt_payloads200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


