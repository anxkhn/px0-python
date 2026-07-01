# PromptVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique version identifier. | 
**prompt_id** | **str** | Reference to parent Prompt ID. | 
**version** | **int** | Incrementing sequence number of the version. | 
**template** | **str** | The template syntax code with Go template parameters. | 
**status** | **str** | Active lifecycle status of this template version. | 
**created_at** | **datetime** |  | 
**published_at** | **datetime** | Timestamp when status was set to live. Null if draft. | [optional] 
**tags** | **List[str]** | List of tag strings attached to this version. | 

## Example

```python
from px0.models.prompt_version import PromptVersion

# TODO update the JSON string below
json = "{}"
# create an instance of PromptVersion from a JSON string
prompt_version_instance = PromptVersion.from_json(json)
# print the JSON string representation of the object
print(PromptVersion.to_json())

# convert the object into a dict
prompt_version_dict = prompt_version_instance.to_dict()
# create an instance of PromptVersion from a dict
prompt_version_from_dict = PromptVersion.from_dict(prompt_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


