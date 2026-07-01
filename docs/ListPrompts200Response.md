# ListPrompts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompts** | [**List[Prompt]**](Prompt.md) |  | 

## Example

```python
from px0.models.list_prompts200_response import ListPrompts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPrompts200Response from a JSON string
list_prompts200_response_instance = ListPrompts200Response.from_json(json)
# print the JSON string representation of the object
print(ListPrompts200Response.to_json())

# convert the object into a dict
list_prompts200_response_dict = list_prompts200_response_instance.to_dict()
# create an instance of ListPrompts200Response from a dict
list_prompts200_response_from_dict = ListPrompts200Response.from_dict(list_prompts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


