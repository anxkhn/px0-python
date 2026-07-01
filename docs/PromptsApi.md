# px0.PromptsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_prompt**](PromptsApi.md#archive_prompt) | **POST** /v1/prompts/{id}/archive | Archive a Prompt
[**create_prompt**](PromptsApi.md#create_prompt) | **POST** /v1/teams/{teamID}/prompts | Create a Prompt
[**get_prompt**](PromptsApi.md#get_prompt) | **GET** /v1/prompts/{id} | Get a Prompt
[**list_all_prompts**](PromptsApi.md#list_all_prompts) | **GET** /v1/prompts | List all prompts with team filter
[**list_prompts**](PromptsApi.md#list_prompts) | **GET** /v1/teams/{teamID}/prompts | List Prompts
[**move_prompt**](PromptsApi.md#move_prompt) | **POST** /v1/prompts/{id}/move | Move a Prompt
[**restore_prompt**](PromptsApi.md#restore_prompt) | **POST** /v1/prompts/{id}/restore | Restore a Prompt
[**update_prompt**](PromptsApi.md#update_prompt) | **PUT** /v1/prompts/{id} | Update a Prompt


# **archive_prompt**
> CreatePrompt201Response archive_prompt(id)

Archive a Prompt

Archives a specific prompt container, setting `status` to 'archived'. The prompt still exists in the system and people can call it and use it, so a prompt is never deleted. Requires Org Admin or Team Admin privileges (GitHub repo owner model). Team Editors and Team Members are not authorized to archive prompts.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt201_response import CreatePrompt201Response
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
    api_instance = px0.PromptsApi(api_client)
    id = 'id_example' # str | The unique UUID of the prompt to archive.

    try:
        # Archive a Prompt
        api_response = api_instance.archive_prompt(id)
        print("The response of PromptsApi->archive_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->archive_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique UUID of the prompt to archive. | 

### Return type

[**CreatePrompt201Response**](CreatePrompt201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt successfully archived |  -  |
**400** | Invalid UUID format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Prompt not found |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prompt**
> CreatePrompt201Response create_prompt(team_id, create_prompt_request)

Create a Prompt

Creates a new prompt container.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt201_response import CreatePrompt201Response
from px0.models.create_prompt_request import CreatePromptRequest
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
    api_instance = px0.PromptsApi(api_client)
    team_id = 'team_id_example' # str | The ID of the team.
    create_prompt_request = px0.CreatePromptRequest() # CreatePromptRequest | 

    try:
        # Create a Prompt
        api_response = api_instance.create_prompt(team_id, create_prompt_request)
        print("The response of PromptsApi->create_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->create_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The ID of the team. | 
 **create_prompt_request** | [**CreatePromptRequest**](CreatePromptRequest.md)|  | 

### Return type

[**CreatePrompt201Response**](CreatePrompt201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Prompt created successfully |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prompt**
> CreatePrompt201Response get_prompt(id)

Get a Prompt

Returns details of a specific prompt container by its unique UUID.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt201_response import CreatePrompt201Response
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
    api_instance = px0.PromptsApi(api_client)
    id = 'id_example' # str | The unique UUID of the prompt.

    try:
        # Get a Prompt
        api_response = api_instance.get_prompt(id)
        print("The response of PromptsApi->get_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique UUID of the prompt. | 

### Return type

[**CreatePrompt201Response**](CreatePrompt201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt details |  -  |
**400** | Invalid UUID format |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt not found |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_prompts**
> ListAllPrompts200Response list_all_prompts(team_id=team_id, team=team, archived=archived)

List all prompts with team filter

Returns a list of prompts. If team_id query parameter is not provided, returns an empty list by default. Users can filter by a team they are a member of.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_all_prompts200_response import ListAllPrompts200Response
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
    api_instance = px0.PromptsApi(api_client)
    team_id = 'team_id_example' # str | Optional UUID of the team to filter prompts (alias of team). (optional)
    team = 'team_example' # str | Optional UUID of the team to filter prompts (alias of team_id). (optional)
    archived = True # bool | Optional boolean to filter prompts by archive state. (optional)

    try:
        # List all prompts with team filter
        api_response = api_instance.list_all_prompts(team_id=team_id, team=team, archived=archived)
        print("The response of PromptsApi->list_all_prompts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->list_all_prompts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Optional UUID of the team to filter prompts (alias of team). | [optional] 
 **team** | **str**| Optional UUID of the team to filter prompts (alias of team_id). | [optional] 
 **archived** | **bool**| Optional boolean to filter prompts by archive state. | [optional] 

### Return type

[**ListAllPrompts200Response**](ListAllPrompts200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of prompts |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prompts**
> ListPrompts200Response list_prompts(team_id, archived=archived)

List Prompts

Lists all available prompt containers.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_prompts200_response import ListPrompts200Response
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
    api_instance = px0.PromptsApi(api_client)
    team_id = 'team_id_example' # str | The ID of the team.
    archived = True # bool | Optional boolean to filter prompts by archive state. (optional)

    try:
        # List Prompts
        api_response = api_instance.list_prompts(team_id, archived=archived)
        print("The response of PromptsApi->list_prompts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->list_prompts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The ID of the team. | 
 **archived** | **bool**| Optional boolean to filter prompts by archive state. | [optional] 

### Return type

[**ListPrompts200Response**](ListPrompts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of prompts |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_prompt**
> CreatePrompt201Response move_prompt(id, move_prompt_request)

Move a Prompt

Moves a prompt from its current team to another team. Requires admin privileges on both teams.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt201_response import CreatePrompt201Response
from px0.models.move_prompt_request import MovePromptRequest
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
    api_instance = px0.PromptsApi(api_client)
    id = 'id_example' # str | 
    move_prompt_request = px0.MovePromptRequest() # MovePromptRequest | 

    try:
        # Move a Prompt
        api_response = api_instance.move_prompt(id, move_prompt_request)
        print("The response of PromptsApi->move_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->move_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **move_prompt_request** | [**MovePromptRequest**](MovePromptRequest.md)|  | 

### Return type

[**CreatePrompt201Response**](CreatePrompt201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt successfully moved |  -  |
**400** | Invalid UUID format or team_id |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_prompt**
> CreatePrompt201Response restore_prompt(id)

Restore a Prompt

Restores a previously archived prompt setting `status` back to 'active'. Requires Team Admin or Org Admin.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt201_response import CreatePrompt201Response
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
    api_instance = px0.PromptsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore a Prompt
        api_response = api_instance.restore_prompt(id)
        print("The response of PromptsApi->restore_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->restore_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CreatePrompt201Response**](CreatePrompt201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt successfully restored |  -  |
**400** | Invalid UUID format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prompt**
> CreatePrompt201Response update_prompt(id, update_prompt_request)

Update a Prompt

Updates the description of a specific prompt by its unique UUID.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt201_response import CreatePrompt201Response
from px0.models.update_prompt_request import UpdatePromptRequest
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
    api_instance = px0.PromptsApi(api_client)
    id = 'id_example' # str | The unique UUID of the prompt.
    update_prompt_request = px0.UpdatePromptRequest() # UpdatePromptRequest | 

    try:
        # Update a Prompt
        api_response = api_instance.update_prompt(id, update_prompt_request)
        print("The response of PromptsApi->update_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->update_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique UUID of the prompt. | 
 **update_prompt_request** | [**UpdatePromptRequest**](UpdatePromptRequest.md)|  | 

### Return type

[**CreatePrompt201Response**](CreatePrompt201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt updated successfully |  -  |
**400** | Invalid input or invalid UUID format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Viewer or unauthorized team member |  -  |
**404** | Prompt not found |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

