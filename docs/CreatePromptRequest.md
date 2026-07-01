# CreatePromptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from px0.models.create_prompt_request import CreatePromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePromptRequest from a JSON string
create_prompt_request_instance = CreatePromptRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePromptRequest.to_json())

# convert the object into a dict
create_prompt_request_dict = create_prompt_request_instance.to_dict()
# create an instance of CreatePromptRequest from a dict
create_prompt_request_from_dict = CreatePromptRequest.from_dict(create_prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


