# TriggerPasswordResetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from px0.models.trigger_password_reset_request import TriggerPasswordResetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerPasswordResetRequest from a JSON string
trigger_password_reset_request_instance = TriggerPasswordResetRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerPasswordResetRequest.to_json())

# convert the object into a dict
trigger_password_reset_request_dict = trigger_password_reset_request_instance.to_dict()
# create an instance of TriggerPasswordResetRequest from a dict
trigger_password_reset_request_from_dict = TriggerPasswordResetRequest.from_dict(trigger_password_reset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


