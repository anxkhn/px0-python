# Prompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier. | 
**team_id** | **str** | Unique identifier of the team. | 
**slug** | **str** | Unique slug within the team. | 
**name** | **str** | Name of the prompt container. | 
**description** | **str** | Brief summary explaining the prompt purpose. | 
**status** | **str** | Current status of the prompt container (active, archived). | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from px0.models.prompt import Prompt

# TODO update the JSON string below
json = "{}"
# create an instance of Prompt from a JSON string
prompt_instance = Prompt.from_json(json)
# print the JSON string representation of the object
print(Prompt.to_json())

# convert the object into a dict
prompt_dict = prompt_instance.to_dict()
# create an instance of Prompt from a dict
prompt_from_dict = Prompt.from_dict(prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


