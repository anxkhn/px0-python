# px0.TeamsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](TeamsApi.md#create_team) | **POST** /v1/orgs/{orgID}/teams | Create Team
[**delete_team**](TeamsApi.md#delete_team) | **DELETE** /v1/teams/{id} | Delete Team
[**leave_team**](TeamsApi.md#leave_team) | **DELETE** /v1/me/teams/{teamID} | Leave Team
[**list_org_teams**](TeamsApi.md#list_org_teams) | **GET** /v1/orgs/{orgID}/teams | List Org Teams
[**list_user_teams**](TeamsApi.md#list_user_teams) | **GET** /v1/me/teams | List User Teams
[**update_team**](TeamsApi.md#update_team) | **PUT** /v1/teams/{id} | Update Team


# **create_team**
> CreateTeam201Response create_team(org_id, create_team_request)

Create Team

Creates a new team under a specific organization. Requires Org Admin privileges (admin on the Default Team). Team admins or editors of other custom teams are not authorized to create teams.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_team201_response import CreateTeam201Response
from px0.models.create_team_request import CreateTeamRequest
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
    api_instance = px0.TeamsApi(api_client)
    org_id = 'org_id_example' # str | 
    create_team_request = px0.CreateTeamRequest() # CreateTeamRequest | 

    try:
        # Create Team
        api_response = api_instance.create_team(org_id, create_team_request)
        print("The response of TeamsApi->create_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->create_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **create_team_request** | [**CreateTeamRequest**](CreateTeamRequest.md)|  | 

### Return type

[**CreateTeam201Response**](CreateTeam201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> delete_team(id)

Delete Team

Deletes an existing team. Requires Org Admin, Team Admin, or Team Editor privileges. Team Members (viewers) are not authorized.

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
    api_instance = px0.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Team
        api_instance.delete_team(id)
    except Exception as e:
        print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**204** | Team deleted successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_team**
> leave_team(team_id)

Leave Team

Allows the authenticated user to voluntarily leave a team they belong to.

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
    api_instance = px0.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Leave Team
        api_instance.leave_team(team_id)
    except Exception as e:
        print("Exception when calling TeamsApi->leave_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Left team successfully (No Content) |  -  |
**401** | Unauthorized |  -  |
**404** | Team not found or user not a member of the team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_teams**
> ListUserTeams200Response list_org_teams(org_id)

List Org Teams

Returns a list of all teams within the specified organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_user_teams200_response import ListUserTeams200Response
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
    api_instance = px0.TeamsApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # List Org Teams
        api_response = api_instance.list_org_teams(org_id)
        print("The response of TeamsApi->list_org_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->list_org_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**ListUserTeams200Response**](ListUserTeams200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of teams |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_teams**
> ListUserTeams200Response list_user_teams()

List User Teams

Returns a list of teams the authenticated user belongs to.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_user_teams200_response import ListUserTeams200Response
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
    api_instance = px0.TeamsApi(api_client)

    try:
        # List User Teams
        api_response = api_instance.list_user_teams()
        print("The response of TeamsApi->list_user_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->list_user_teams: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListUserTeams200Response**](ListUserTeams200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of teams |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> CreateTeam201Response update_team(id, update_team_request)

Update Team

Updates an existing team. Requires Org Admin, Team Admin, or Team Editor privileges. Team Members (viewers) are not authorized.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_team201_response import CreateTeam201Response
from px0.models.update_team_request import UpdateTeamRequest
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
    api_instance = px0.TeamsApi(api_client)
    id = 'id_example' # str | 
    update_team_request = px0.UpdateTeamRequest() # UpdateTeamRequest | 

    try:
        # Update Team
        api_response = api_instance.update_team(id, update_team_request)
        print("The response of TeamsApi->update_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->update_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_team_request** | [**UpdateTeamRequest**](UpdateTeamRequest.md)|  | 

### Return type

[**CreateTeam201Response**](CreateTeam201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

