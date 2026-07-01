# px0.PromptPayloadsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_prompt_payload**](PromptPayloadsApi.md#create_prompt_payload) | **POST** /v1/prompts/{id}/payloads | Create a Prompt Payload
[**delete_prompt_payload**](PromptPayloadsApi.md#delete_prompt_payload) | **DELETE** /v1/prompts/{id}/payloads/{payloadID} | Delete a Prompt Payload
[**get_prompt_payload**](PromptPayloadsApi.md#get_prompt_payload) | **GET** /v1/prompts/{id}/payloads/{payloadID} | Get a Prompt Payload
[**list_prompt_payloads**](PromptPayloadsApi.md#list_prompt_payloads) | **GET** /v1/prompts/{id}/payloads | List Prompt Payloads
[**update_prompt_payload**](PromptPayloadsApi.md#update_prompt_payload) | **PUT** /v1/prompts/{id}/payloads/{payloadID} | Update a Prompt Payload


# **create_prompt_payload**
> CreatePromptPayload201Response create_prompt_payload(id, create_prompt_payload_request)

Create a Prompt Payload

Creates a new sample payload for the specified prompt. Only editors of the team can create.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt_payload201_response import CreatePromptPayload201Response
from px0.models.create_prompt_payload_request import CreatePromptPayloadRequest
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
    api_instance = px0.PromptPayloadsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    create_prompt_payload_request = px0.CreatePromptPayloadRequest() # CreatePromptPayloadRequest | 

    try:
        # Create a Prompt Payload
        api_response = api_instance.create_prompt_payload(id, create_prompt_payload_request)
        print("The response of PromptPayloadsApi->create_prompt_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptPayloadsApi->create_prompt_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **create_prompt_payload_request** | [**CreatePromptPayloadRequest**](CreatePromptPayloadRequest.md)|  | 

### Return type

[**CreatePromptPayload201Response**](CreatePromptPayload201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Prompt payload created successfully |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prompt_payload**
> delete_prompt_payload(id, payload_id)

Delete a Prompt Payload

Deletes a specific sample payload. Only editors can delete.

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
    api_instance = px0.PromptPayloadsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    payload_id = 'payload_id_example' # str | Unique payload UUID.

    try:
        # Delete a Prompt Payload
        api_instance.delete_prompt_payload(id, payload_id)
    except Exception as e:
        print("Exception when calling PromptPayloadsApi->delete_prompt_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **payload_id** | **str**| Unique payload UUID. | 

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
**204** | Prompt payload deleted successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Prompt or payload not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prompt_payload**
> CreatePromptPayload201Response get_prompt_payload(id, payload_id)

Get a Prompt Payload

Retrieves a specific sample payload by its ID and prompt ID.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt_payload201_response import CreatePromptPayload201Response
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
    api_instance = px0.PromptPayloadsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    payload_id = 'payload_id_example' # str | Unique payload UUID.

    try:
        # Get a Prompt Payload
        api_response = api_instance.get_prompt_payload(id, payload_id)
        print("The response of PromptPayloadsApi->get_prompt_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptPayloadsApi->get_prompt_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **payload_id** | **str**| Unique payload UUID. | 

### Return type

[**CreatePromptPayload201Response**](CreatePromptPayload201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt payload details |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt or payload not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prompt_payloads**
> ListPromptPayloads200Response list_prompt_payloads(id)

List Prompt Payloads

Lists all sample payloads associated with the specified prompt.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.list_prompt_payloads200_response import ListPromptPayloads200Response
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
    api_instance = px0.PromptPayloadsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.

    try:
        # List Prompt Payloads
        api_response = api_instance.list_prompt_payloads(id)
        print("The response of PromptPayloadsApi->list_prompt_payloads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptPayloadsApi->list_prompt_payloads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 

### Return type

[**ListPromptPayloads200Response**](ListPromptPayloads200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of prompt payloads |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prompt_payload**
> CreatePromptPayload201Response update_prompt_payload(id, payload_id, update_prompt_payload_request)

Update a Prompt Payload

Updates an existing sample payload's variables and/or optional name. Only editors can update.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.create_prompt_payload201_response import CreatePromptPayload201Response
from px0.models.update_prompt_payload_request import UpdatePromptPayloadRequest
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
    api_instance = px0.PromptPayloadsApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    payload_id = 'payload_id_example' # str | Unique payload UUID.
    update_prompt_payload_request = px0.UpdatePromptPayloadRequest() # UpdatePromptPayloadRequest | 

    try:
        # Update a Prompt Payload
        api_response = api_instance.update_prompt_payload(id, payload_id, update_prompt_payload_request)
        print("The response of PromptPayloadsApi->update_prompt_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptPayloadsApi->update_prompt_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **payload_id** | **str**| Unique payload UUID. | 
 **update_prompt_payload_request** | [**UpdatePromptPayloadRequest**](UpdatePromptPayloadRequest.md)|  | 

### Return type

[**CreatePromptPayload201Response**](CreatePromptPayload201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt payload updated successfully |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Prompt or payload not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

