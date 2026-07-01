# px0.PromptVersionsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_version**](PromptVersionsApi.md#archive_version) | **POST** /v1/prompts/{id}/versions/{version}/archive | Archive Prompt Version
[**create_version**](PromptVersionsApi.md#create_version) | **POST** /v1/prompts/{id}/versions | Create a Prompt Version
[**delete_prompt_version**](PromptVersionsApi.md#delete_prompt_version) | **DELETE** /v1/prompts/{id}/versions/{version} | Delete Prompt Version Draft
[**demote_version**](PromptVersionsApi.md#demote_version) | **POST** /v1/prompts/{id}/versions/{version}/demote | Demote Prompt Version
[**diff_versions**](PromptVersionsApi.md#diff_versions) | **GET** /v1/prompts/{id}/versions/diff | Diff Prompt Versions
[**duplicate_version**](PromptVersionsApi.md#duplicate_version) | **POST** /v1/prompts/{id}/versions/{version}/duplicate | Duplicate Prompt Version
[**get_version**](PromptVersionsApi.md#get_version) | **GET** /v1/prompts/{id}/versions/{version} | Get Prompt Version
[**list_version_tags**](PromptVersionsApi.md#list_version_tags) | **GET** /v1/prompts/{id}/tags | List Prompt Version Tags
[**list_versions**](PromptVersionsApi.md#list_versions) | **GET** /v1/prompts/{id}/versions | List Prompt Versions
[**promote_version**](PromptVersionsApi.md#promote_version) | **POST** /v1/prompts/{id}/versions/{version}/promote | Promote Prompt Version
[**remove_version_tag**](PromptVersionsApi.md#remove_version_tag) | **DELETE** /v1/prompts/{id}/tags/{tag} | Remove Version Tag
[**set_version_tag**](PromptVersionsApi.md#set_version_tag) | **POST** /v1/prompts/{id}/versions/{version}/tags | Attach/Set Version Tag
[**update_version**](PromptVersionsApi.md#update_version) | **PUT** /v1/prompts/{id}/versions/{version} | Update Prompt Version Draft


# **archive_version**
> CreateVersion201Response archive_version(id, version)

Archive Prompt Version

Archives a prompt version, marking its status as archived.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to archive.

    try:
        # Archive Prompt Version
        api_response = api_instance.archive_version(id, version)
        print("The response of PromptVersionsApi->archive_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->archive_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to archive. | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version archived successfully |  -  |
**400** | Bad parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Version not found |  -  |
**422** | Archiving error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version**
> CreateVersion201Response create_version(id, create_version_request)

Create a Prompt Version

Creates a new version of the prompt template in 'draft' state.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
from px0.models.create_version_request import CreateVersionRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    create_version_request = px0.CreateVersionRequest() # CreateVersionRequest | 

    try:
        # Create a Prompt Version
        api_response = api_instance.create_version(id, create_version_request)
        print("The response of PromptVersionsApi->create_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->create_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **create_version_request** | [**CreateVersionRequest**](CreateVersionRequest.md)|  | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Version created successfully |  -  |
**400** | Invalid template or syntax error |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt not found |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prompt_version**
> delete_prompt_version(id, version)

Delete Prompt Version Draft

Deletes a specific prompt template version. Only versions currently in the 'draft' status may be deleted. 

### Example

* Api Key Authentication (ApiKeyAuth):
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to delete.

    try:
        # Delete Prompt Version Draft
        api_instance.delete_prompt_version(id, version)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->delete_prompt_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to delete. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Version deleted successfully |  -  |
**400** | Invalid path formatting |  -  |
**401** | Unauthorized |  -  |
**404** | Version not found |  -  |
**422** | Only draft versions can be deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **demote_version**
> CreateVersion201Response demote_version(id, version)

Demote Prompt Version

Demotes a live prompt version to stable (making it inactive but remaining read-only).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to demote.

    try:
        # Demote Prompt Version
        api_response = api_instance.demote_version(id, version)
        print("The response of PromptVersionsApi->demote_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->demote_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to demote. | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version demoted successfully |  -  |
**400** | Bad parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Version not found |  -  |
**422** | Demotion error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diff_versions**
> DiffVersions200Response diff_versions(id, var_from, to)

Diff Prompt Versions

Compares the templates of two prompt versions side-by-side and returns a unified diff. Requires read access to the prompt.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.diff_versions200_response import DiffVersions200Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | 
    var_from = 56 # int | The source version number to compare from.
    to = 56 # int | The target version number to compare to.

    try:
        # Diff Prompt Versions
        api_response = api_instance.diff_versions(id, var_from, to)
        print("The response of PromptVersionsApi->diff_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->diff_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **var_from** | **int**| The source version number to compare from. | 
 **to** | **int**| The target version number to compare to. | 

### Return type

[**DiffVersions200Response**](DiffVersions200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Versions compared successfully |  -  |
**400** | Missing or invalid parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt or version not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_version**
> CreateVersion201Response duplicate_version(id, version)

Duplicate Prompt Version

Copies the specified prompt version's template to create a new prompt version in draft state. This operation does not copy any associated payloads, only the prompt template and other metadata. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to duplicate from.

    try:
        # Duplicate Prompt Version
        api_response = api_instance.duplicate_version(id, version)
        print("The response of PromptVersionsApi->duplicate_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->duplicate_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to duplicate from. | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Prompt version duplicated and new draft version created successfully |  -  |
**400** | Bad parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Version or prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> CreateVersion201Response get_version(id, version)

Get Prompt Version

Retrieves details of a specific prompt template version by version number.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string).

    try:
        # Get Prompt Version
        api_response = api_instance.get_version(id, version)
        print("The response of PromptVersionsApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->get_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string). | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt version details |  -  |
**400** | Invalid path formatting |  -  |
**401** | Unauthorized |  -  |
**404** | Version not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version_tags**
> ListVersionTags200Response list_version_tags(id)

List Prompt Version Tags

Lists all tags associated with versions of this prompt.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_version_tags200_response import ListVersionTags200Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.

    try:
        # List Prompt Version Tags
        api_response = api_instance.list_version_tags(id)
        print("The response of PromptVersionsApi->list_version_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->list_version_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 

### Return type

[**ListVersionTags200Response**](ListVersionTags200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of prompt tags |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> ListVersions200Response list_versions(id, tags=tags, status=status)

List Prompt Versions

Lists all template versions associated with a prompt container.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_versions200_response import ListVersions200Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    tags = 'tags_example' # str | Optional comma-separated list of tags to filter prompt versions. (optional)
    status = 'status_example' # str | Optional status to filter prompt versions by (draft, live, archived). (optional)

    try:
        # List Prompt Versions
        api_response = api_instance.list_versions(id, tags=tags, status=status)
        print("The response of PromptVersionsApi->list_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->list_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **tags** | **str**| Optional comma-separated list of tags to filter prompt versions. | [optional] 
 **status** | **str**| Optional status to filter prompt versions by (draft, live, archived). | [optional] 

### Return type

[**ListVersions200Response**](ListVersions200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of versions |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_version**
> CreateVersion201Response promote_version(id, version)

Promote Prompt Version

Promotes a version of the prompt template along the lifecycle: draft -> stable -> live. Promoting from draft makes it stable (read-only). Promoting from stable makes it live. When promoting a version to live, any previous live version is demoted to stable. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to promote.

    try:
        # Promote Prompt Version
        api_response = api_instance.promote_version(id, version)
        print("The response of PromptVersionsApi->promote_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->promote_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to promote. | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version promoted successfully |  -  |
**400** | Bad parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Version not found |  -  |
**422** | Promotion error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_version_tag**
> remove_version_tag(id, tag)

Remove Version Tag

Removes/deletes the specified version tag from the prompt.

### Example

* Api Key Authentication (ApiKeyAuth):
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    tag = 'tag_example' # str | Tag string to remove.

    try:
        # Remove Version Tag
        api_instance.remove_version_tag(id, tag)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->remove_version_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **tag** | **str**| Tag string to remove. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Tag removed successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Prompt or tag not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_version_tag**
> CreateVersion201Response set_version_tag(id, version, set_version_tag_request)

Attach/Set Version Tag

Attaches a unique string tag (e.g. 'prod') to the specified prompt version, replacing the tag on any other version of this prompt if it was already assigned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
from px0.models.set_version_tag_request import SetVersionTagRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to tag.
    set_version_tag_request = px0.SetVersionTagRequest() # SetVersionTagRequest | 

    try:
        # Attach/Set Version Tag
        api_response = api_instance.set_version_tag(id, version, set_version_tag_request)
        print("The response of PromptVersionsApi->set_version_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->set_version_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to tag. | 
 **set_version_tag_request** | [**SetVersionTagRequest**](SetVersionTagRequest.md)|  | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag attached successfully. Returns the updated version. |  -  |
**400** | Invalid request or tag format |  -  |
**403** | Forbidden |  -  |
**404** | Prompt or version not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> CreateVersion201Response update_version(id, version, update_version_request)

Update Prompt Version Draft

Updates the draft template code of a specific version. Only versions currently in the 'draft' status may be modified. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_version201_response import CreateVersion201Response
from px0.models.update_version_request import UpdateVersionRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = px0.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.PromptVersionsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to update.
    update_version_request = px0.UpdateVersionRequest() # UpdateVersionRequest | 

    try:
        # Update Prompt Version Draft
        api_response = api_instance.update_version(id, version, update_version_request)
        print("The response of PromptVersionsApi->update_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptVersionsApi->update_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to update. | 
 **update_version_request** | [**UpdateVersionRequest**](UpdateVersionRequest.md)|  | 

### Return type

[**CreateVersion201Response**](CreateVersion201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version updated successfully |  -  |
**400** | Invalid syntax or missing template |  -  |
**401** | Unauthorized |  -  |
**404** | Version not found |  -  |
**422** | Only draft versions can be modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

