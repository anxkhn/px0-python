# px0.TeamMembershipsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_member**](TeamMembershipsApi.md#add_team_member) | **POST** /v1/teams/{id}/members | Add Team Member
[**create_join_request**](TeamMembershipsApi.md#create_join_request) | **POST** /v1/teams/{id}/join-requests | Request to Join Team
[**get_admin_inbox**](TeamMembershipsApi.md#get_admin_inbox) | **GET** /v1/me/inbox | Get Admin Inbox
[**list_team_members**](TeamMembershipsApi.md#list_team_members) | **GET** /v1/teams/{id}/members | List Team Members
[**remove_team_member**](TeamMembershipsApi.md#remove_team_member) | **DELETE** /v1/teams/{id}/members/{userID} | Remove Team Member
[**resolve_join_request**](TeamMembershipsApi.md#resolve_join_request) | **PUT** /v1/join-requests/{id} | Resolve Join Request
[**update_team_member_role**](TeamMembershipsApi.md#update_team_member_role) | **PUT** /v1/teams/{id}/members/{userID}/role | Update Team Member Role


# **add_team_member**
> add_team_member(id, add_team_member_request)

Add Team Member

Adds a user to a team. Requires admin privileges.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.add_team_member_request import AddTeamMemberRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.TeamMembershipsApi(api_client)
    id = 'id_example' # str | 
    add_team_member_request = px0.AddTeamMemberRequest() # AddTeamMemberRequest | 

    try:
        # Add Team Member
        api_instance.add_team_member(id, add_team_member_request)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->add_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **add_team_member_request** | [**AddTeamMemberRequest**](AddTeamMemberRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_join_request**
> TeamJoinRequest create_join_request(id)

Request to Join Team

Creates a pending request for the authenticated user to join a specific team.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.team_join_request import TeamJoinRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.TeamMembershipsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Request to Join Team
        api_response = api_instance.create_join_request(id)
        print("The response of TeamMembershipsApi->create_join_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->create_join_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TeamJoinRequest**](TeamJoinRequest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Join request created successfully |  -  |
**400** | Bad Request (already a member) |  -  |
**401** | Unauthorized |  -  |
**404** | Team Not Found |  -  |
**409** | Conflict (already has a pending request) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_inbox**
> GetAdminInbox200Response get_admin_inbox()

Get Admin Inbox

Returns a list of pending join requests that the authenticated user is authorized to approve or reject.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.get_admin_inbox200_response import GetAdminInbox200Response
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.TeamMembershipsApi(api_client)

    try:
        # Get Admin Inbox
        api_response = api_instance.get_admin_inbox()
        print("The response of TeamMembershipsApi->get_admin_inbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->get_admin_inbox: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAdminInbox200Response**](GetAdminInbox200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of pending join requests |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_members**
> ListTeamMembers200Response list_team_members(id, page=page)

List Team Members

Returns a paginated list of members for a given team. Requires at least viewer access.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_team_members200_response import ListTeamMembers200Response
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.TeamMembershipsApi(api_client)
    id = 'id_example' # str | 
    page = 1 # int |  (optional) (default to 1)

    try:
        # List Team Members
        api_response = api_instance.list_team_members(id, page=page)
        print("The response of TeamMembershipsApi->list_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->list_team_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**ListTeamMembers200Response**](ListTeamMembers200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of members |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_team_member**
> remove_team_member(id, user_id)

Remove Team Member

Removes a user from a team. Requires admin privileges.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.TeamMembershipsApi(api_client)
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove Team Member
        api_instance.remove_team_member(id, user_id)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->remove_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_join_request**
> TeamJoinRequest resolve_join_request(id, resolve_join_request_request)

Resolve Join Request

Approves or rejects a pending join request.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.resolve_join_request_request import ResolveJoinRequestRequest
from px0.models.team_join_request import TeamJoinRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.TeamMembershipsApi(api_client)
    id = 'id_example' # str | 
    resolve_join_request_request = px0.ResolveJoinRequestRequest() # ResolveJoinRequestRequest | 

    try:
        # Resolve Join Request
        api_response = api_instance.resolve_join_request(id, resolve_join_request_request)
        print("The response of TeamMembershipsApi->resolve_join_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->resolve_join_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **resolve_join_request_request** | [**ResolveJoinRequestRequest**](ResolveJoinRequestRequest.md)|  | 

### Return type

[**TeamJoinRequest**](TeamJoinRequest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resolved request details |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (not authorized to approve) |  -  |
**404** | Join Request Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_member_role**
> UpdateTeamMemberRole200Response update_team_member_role(id, user_id, update_team_member_role_request)

Update Team Member Role

Updates a team member's role. Requires team admin privileges.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.update_team_member_role200_response import UpdateTeamMemberRole200Response
from px0.models.update_team_member_role_request import UpdateTeamMemberRoleRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.TeamMembershipsApi(api_client)
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | 
    update_team_member_role_request = px0.UpdateTeamMemberRoleRequest() # UpdateTeamMemberRoleRequest | 

    try:
        # Update Team Member Role
        api_response = api_instance.update_team_member_role(id, user_id, update_team_member_role_request)
        print("The response of TeamMembershipsApi->update_team_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->update_team_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 
 **update_team_member_role_request** | [**UpdateTeamMemberRoleRequest**](UpdateTeamMemberRoleRequest.md)|  | 

### Return type

[**UpdateTeamMemberRole200Response**](UpdateTeamMemberRole200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

