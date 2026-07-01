# TeamJoinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**team_id** | **str** |  | 
**user_id** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from px0.models.team_join_request import TeamJoinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamJoinRequest from a JSON string
team_join_request_instance = TeamJoinRequest.from_json(json)
# print the JSON string representation of the object
print(TeamJoinRequest.to_json())

# convert the object into a dict
team_join_request_dict = team_join_request_instance.to_dict()
# create an instance of TeamJoinRequest from a dict
team_join_request_from_dict = TeamJoinRequest.from_dict(team_join_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


