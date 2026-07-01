# CreatePromptPayload201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | [**PromptPayload**](PromptPayload.md) |  | 

## Example

```python
from px0.models.create_prompt_payload201_response import CreatePromptPayload201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePromptPayload201Response from a JSON string
create_prompt_payload201_response_instance = CreatePromptPayload201Response.from_json(json)
# print the JSON string representation of the object
print(CreatePromptPayload201Response.to_json())

# convert the object into a dict
create_prompt_payload201_response_dict = create_prompt_payload201_response_instance.to_dict()
# create an instance of CreatePromptPayload201Response from a dict
create_prompt_payload201_response_from_dict = CreatePromptPayload201Response.from_dict(create_prompt_payload201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


