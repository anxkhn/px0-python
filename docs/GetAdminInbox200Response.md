# GetAdminInbox200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbox** | [**List[InboxItem]**](InboxItem.md) |  | [optional] 

## Example

```python
from px0.models.get_admin_inbox200_response import GetAdminInbox200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdminInbox200Response from a JSON string
get_admin_inbox200_response_instance = GetAdminInbox200Response.from_json(json)
# print the JSON string representation of the object
print(GetAdminInbox200Response.to_json())

# convert the object into a dict
get_admin_inbox200_response_dict = get_admin_inbox200_response_instance.to_dict()
# create an instance of GetAdminInbox200Response from a dict
get_admin_inbox200_response_from_dict = GetAdminInbox200Response.from_dict(get_admin_inbox200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


