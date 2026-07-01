# CreateTeam201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from px0.models.create_team201_response import CreateTeam201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeam201Response from a JSON string
create_team201_response_instance = CreateTeam201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTeam201Response.to_json())

# convert the object into a dict
create_team201_response_dict = create_team201_response_instance.to_dict()
# create an instance of CreateTeam201Response from a dict
create_team201_response_from_dict = CreateTeam201Response.from_dict(create_team201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


