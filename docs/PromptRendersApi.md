# px0.PromptRendersApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**render_live**](PromptRendersApi.md#render_live) | **POST** /v1/prompts/{id}/render | Render Live Prompt Version
[**render_version**](PromptRendersApi.md#render_version) | **POST** /v1/prompts/{id}/versions/{version}/render | Render Specific Prompt Version


# **render_live**
> RenderResponse render_live(id, render_request)

Render Live Prompt Version

Renders the active 'live' template version of a prompt using supplied variables.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.render_request import RenderRequest
from px0.models.render_response import RenderResponse
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
    api_instance = px0.PromptRendersApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    render_request = px0.RenderRequest() # RenderRequest | 

    try:
        # Render Live Prompt Version
        api_response = api_instance.render_live(id, render_request)
        print("The response of PromptRendersApi->render_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptRendersApi->render_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **render_request** | [**RenderRequest**](RenderRequest.md)|  | 

### Return type

[**RenderResponse**](RenderResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rendered template string |  -  |
**400** | Invalid UUID or bad body JSON |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt or live version not found |  -  |
**422** | Render execution failed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_version**
> RenderResponse render_version(id, version, render_request)

Render Specific Prompt Version

Renders a specific template version of a prompt (even draft status) using supplied variables.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.render_request import RenderRequest
from px0.models.render_response import RenderResponse
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
    api_instance = px0.PromptRendersApi(api_client)
    id = 'id_example' # str | Unique prompt UUID.
    version = 'version_example' # str | Version sequence number (integer) or version tag (string) to render.
    render_request = px0.RenderRequest() # RenderRequest | 

    try:
        # Render Specific Prompt Version
        api_response = api_instance.render_version(id, version, render_request)
        print("The response of PromptRendersApi->render_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptRendersApi->render_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique prompt UUID. | 
 **version** | **str**| Version sequence number (integer) or version tag (string) to render. | 
 **render_request** | [**RenderRequest**](RenderRequest.md)|  | 

### Return type

[**RenderResponse**](RenderResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rendered template string |  -  |
**400** | Invalid path formatting |  -  |
**401** | Unauthorized |  -  |
**404** | Prompt or version not found |  -  |
**422** | Execution failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

