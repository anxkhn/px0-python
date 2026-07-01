# InboxItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**team_id** | **str** |  | 
**team_name** | **str** |  | 
**user_id** | **str** |  | 
**user_email** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from px0.models.inbox_item import InboxItem

# TODO update the JSON string below
json = "{}"
# create an instance of InboxItem from a JSON string
inbox_item_instance = InboxItem.from_json(json)
# print the JSON string representation of the object
print(InboxItem.to_json())

# convert the object into a dict
inbox_item_dict = inbox_item_instance.to_dict()
# create an instance of InboxItem from a dict
inbox_item_from_dict = InboxItem.from_dict(inbox_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


