# APIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique API Key identifier. | 
**name** | **str** | Human-readable name given to the API key. | 
**org_id** | **str** | UUID of the organization. | 
**team_id** | **str** | Optional UUID of the team. | [optional] 
**key_prefix** | **str** | First characters of the API Key used for visual identification. | 
**operation** | **str** | The scope of operations. | 
**created_at** | **datetime** | Timestamp when the API Key was created. | 
**last_used_at** | **datetime** | Timestamp when the API Key was last used. Null if never used. | [optional] 

## Example

```python
from px0.models.api_key import APIKey

# TODO update the JSON string below
json = "{}"
# create an instance of APIKey from a JSON string
api_key_instance = APIKey.from_json(json)
# print the JSON string representation of the object
print(APIKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of APIKey from a dict
api_key_from_dict = APIKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


