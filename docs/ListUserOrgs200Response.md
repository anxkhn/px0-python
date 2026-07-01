# ListUserOrgs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[OrganizationWithRole]**](OrganizationWithRole.md) |  | [optional] 

## Example

```python
from px0.models.list_user_orgs200_response import ListUserOrgs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserOrgs200Response from a JSON string
list_user_orgs200_response_instance = ListUserOrgs200Response.from_json(json)
# print the JSON string representation of the object
print(ListUserOrgs200Response.to_json())

# convert the object into a dict
list_user_orgs200_response_dict = list_user_orgs200_response_instance.to_dict()
# create an instance of ListUserOrgs200Response from a dict
list_user_orgs200_response_from_dict = ListUserOrgs200Response.from_dict(list_user_orgs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


