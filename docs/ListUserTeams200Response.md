# ListUserTeams200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[Team]**](Team.md) |  | [optional] 

## Example

```python
from px0.models.list_user_teams200_response import ListUserTeams200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserTeams200Response from a JSON string
list_user_teams200_response_instance = ListUserTeams200Response.from_json(json)
# print the JSON string representation of the object
print(ListUserTeams200Response.to_json())

# convert the object into a dict
list_user_teams200_response_dict = list_user_teams200_response_instance.to_dict()
# create an instance of ListUserTeams200Response from a dict
list_user_teams200_response_from_dict = ListUserTeams200Response.from_dict(list_user_teams200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


