# RenderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rendered** | **str** | Fully parsed template response with variable replacements. | 
**version** | **int** | Sequence version number that was executed. | 
**slug** | **str** | Unique prompt slug. | 
**tags** | **List[str]** | List of tag strings assigned to this version. | 

## Example

```python
from px0.models.render_response import RenderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponse from a JSON string
render_response_instance = RenderResponse.from_json(json)
# print the JSON string representation of the object
print(RenderResponse.to_json())

# convert the object into a dict
render_response_dict = render_response_instance.to_dict()
# create an instance of RenderResponse from a dict
render_response_from_dict = RenderResponse.from_dict(render_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


