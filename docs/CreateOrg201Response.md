# CreateOrg201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from px0.models.create_org201_response import CreateOrg201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrg201Response from a JSON string
create_org201_response_instance = CreateOrg201Response.from_json(json)
# print the JSON string representation of the object
print(CreateOrg201Response.to_json())

# convert the object into a dict
create_org201_response_dict = create_org201_response_instance.to_dict()
# create an instance of CreateOrg201Response from a dict
create_org201_response_from_dict = CreateOrg201Response.from_dict(create_org201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


