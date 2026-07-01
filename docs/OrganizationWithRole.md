# OrganizationWithRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from px0.models.organization_with_role import OrganizationWithRole

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationWithRole from a JSON string
organization_with_role_instance = OrganizationWithRole.from_json(json)
# print the JSON string representation of the object
print(OrganizationWithRole.to_json())

# convert the object into a dict
organization_with_role_dict = organization_with_role_instance.to_dict()
# create an instance of OrganizationWithRole from a dict
organization_with_role_from_dict = OrganizationWithRole.from_dict(organization_with_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


