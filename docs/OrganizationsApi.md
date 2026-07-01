# px0.OrganizationsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org**](OrganizationsApi.md#create_org) | **POST** /v1/orgs | Create Organization
[**delete_org**](OrganizationsApi.md#delete_org) | **DELETE** /v1/orgs/{id} | Delete Organization
[**list_org_people**](OrganizationsApi.md#list_org_people) | **GET** /v1/orgs/{orgID}/people | List Org People
[**list_user_orgs**](OrganizationsApi.md#list_user_orgs) | **GET** /v1/me/orgs | List User Organizations
[**remove_org_member**](OrganizationsApi.md#remove_org_member) | **DELETE** /v1/orgs/{orgID}/members/{userID} | Remove Member from Organization
[**update_org**](OrganizationsApi.md#update_org) | **PUT** /v1/orgs/{id} | Update Organization


# **create_org**
> CreateOrg201Response create_org(create_org_request)

Create Organization

Creates a new organization. Requires admin privileges.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_org201_response import CreateOrg201Response
from px0.models.create_org_request import CreateOrgRequest
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
    api_instance = px0.OrganizationsApi(api_client)
    create_org_request = px0.CreateOrgRequest() # CreateOrgRequest | 

    try:
        # Create Organization
        api_response = api_instance.create_org(create_org_request)
        print("The response of OrganizationsApi->create_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_org_request** | [**CreateOrgRequest**](CreateOrgRequest.md)|  | 

### Return type

[**CreateOrg201Response**](CreateOrg201Response.md)

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

# **delete_org**
> delete_org(id)

Delete Organization

Deletes an organization and all cascading dependencies. Requires Org Admin.

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
    api_instance = px0.OrganizationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Organization
        api_instance.delete_org(id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_org: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted successfully (No Content) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_people**
> ListOrgPeople200Response list_org_people(org_id, page=page, limit=limit)

List Org People

Returns a paginated list of distinct people who are members of any team in the organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_org_people200_response import ListOrgPeople200Response
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
    api_instance = px0.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Org People
        api_response = api_instance.list_org_people(org_id, page=page, limit=limit)
        print("The response of OrganizationsApi->list_org_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_org_people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**ListOrgPeople200Response**](ListOrgPeople200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of people |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Organization Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_orgs**
> ListUserOrgs200Response list_user_orgs()

List User Organizations

Returns a list of organizations the authenticated user belongs to.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_user_orgs200_response import ListUserOrgs200Response
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
    api_instance = px0.OrganizationsApi(api_client)

    try:
        # List User Organizations
        api_response = api_instance.list_user_orgs()
        print("The response of OrganizationsApi->list_user_orgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_user_orgs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListUserOrgs200Response**](ListUserOrgs200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organizations with roles |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_org_member**
> remove_org_member(org_id, user_id)

Remove Member from Organization

Removes a user from an organization by removing them from all teams in that organization. Requires Org Admin privileges.

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
    api_instance = px0.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove Member from Organization
        api_instance.remove_org_member(org_id, user_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->remove_org_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 

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
**204** | User successfully removed from the organization |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org**
> CreateOrg201Response update_org(id, update_org_request)

Update Organization

Updates an existing organization's metadata. Requires admin privileges.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_org201_response import CreateOrg201Response
from px0.models.update_org_request import UpdateOrgRequest
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
    api_instance = px0.OrganizationsApi(api_client)
    id = 'id_example' # str | 
    update_org_request = px0.UpdateOrgRequest() # UpdateOrgRequest | 

    try:
        # Update Organization
        api_response = api_instance.update_org(id, update_org_request)
        print("The response of OrganizationsApi->update_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_org_request** | [**UpdateOrgRequest**](UpdateOrgRequest.md)|  | 

### Return type

[**CreateOrg201Response**](CreateOrg201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

