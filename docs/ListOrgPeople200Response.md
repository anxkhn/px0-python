# ListOrgPeople200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | [**List[User]**](User.md) |  | 
**page** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from px0.models.list_org_people200_response import ListOrgPeople200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrgPeople200Response from a JSON string
list_org_people200_response_instance = ListOrgPeople200Response.from_json(json)
# print the JSON string representation of the object
print(ListOrgPeople200Response.to_json())

# convert the object into a dict
list_org_people200_response_dict = list_org_people200_response_instance.to_dict()
# create an instance of ListOrgPeople200Response from a dict
list_org_people200_response_from_dict = ListOrgPeople200Response.from_dict(list_org_people200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


