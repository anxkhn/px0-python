# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique user identifier. | 
**email** | **str** | Email address of the user. | 
**is_verified** | **bool** | Whether the user&#39;s email has been verified. | 
**is_admin** | **bool** | Whether the user is an admin. | 
**created_at** | **datetime** | Timestamp when the user was created. | 

## Example

```python
from px0.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


