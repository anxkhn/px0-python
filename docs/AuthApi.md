# px0.AuthApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](AuthApi.md#change_password) | **POST** /v1/auth/me/change-password | Change Password
[**delete_me**](AuthApi.md#delete_me) | **DELETE** /v1/auth/me | Delete Me
[**login**](AuthApi.md#login) | **POST** /v1/auth/login | Login
[**logout**](AuthApi.md#logout) | **DELETE** /v1/auth/session | Logout
[**me**](AuthApi.md#me) | **GET** /v1/auth/me | Me
[**register**](AuthApi.md#register) | **POST** /v1/auth/register | Register a new user
[**reset_password**](AuthApi.md#reset_password) | **POST** /v1/auth/password-reset/reset | Reset Password
[**trigger_password_reset**](AuthApi.md#trigger_password_reset) | **POST** /v1/auth/password-reset/trigger | Trigger Password Reset
[**trigger_verification_email**](AuthApi.md#trigger_verification_email) | **GET** /v1/auth/verify-email | Trigger Verification Email
[**update_me**](AuthApi.md#update_me) | **PUT** /v1/auth/me | Update Me
[**verify_email**](AuthApi.md#verify_email) | **POST** /v1/auth/verify-email | Verify User Email


# **change_password**
> ChangePassword200Response change_password(change_password_request)

Change Password

Changes the currently logged-in user's password.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.change_password200_response import ChangePassword200Response
from px0.models.change_password_request import ChangePasswordRequest
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
    api_instance = px0.AuthApi(api_client)
    change_password_request = px0.ChangePasswordRequest() # ChangePasswordRequest | 

    try:
        # Change Password
        api_response = api_instance.change_password(change_password_request)
        print("The response of AuthApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password changed successfully |  -  |
**400** | Password too short or too weak |  -  |
**401** | Unauthorized or invalid current password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_me**
> delete_me()

Delete Me

Deletes the currently logged-in user's account.

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
    api_instance = px0.AuthApi(api_client)

    try:
        # Delete Me
        api_instance.delete_me()
    except Exception as e:
        print("Exception when calling AuthApi->delete_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Account deleted successfully |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> Login200Response login(login_request)

Login

Authenticates a user and creates a new access token.

### Example


```python
import px0
from px0.models.login200_response import Login200Response
from px0.models.login_request import LoginRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.AuthApi(api_client)
    login_request = px0.LoginRequest() # LoginRequest | 

    try:
        # Login
        api_response = api_instance.login(login_request)
        print("The response of AuthApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**Login200Response**](Login200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login successful |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid credentials |  -  |
**403** | User is not verified |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout

Destroys the active access token, logging the user out.

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
    api_instance = px0.AuthApi(api_client)

    try:
        # Logout
        api_instance.logout()
    except Exception as e:
        print("Exception when calling AuthApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Logged out successfully (No content) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> Register201Response me()

Me

Returns the profile of the currently logged-in user.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.register201_response import Register201Response
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
    api_instance = px0.AuthApi(api_client)

    try:
        # Me
        api_response = api_instance.me()
        print("The response of AuthApi->me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Register201Response**](Register201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User profile |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> Register201Response register(register_request)

Register a new user

Registers a new user with an email and password. This endpoint can be called unauthenticated to register a new admin, or authenticated (as an admin) to register a standard user into a specific team.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.register201_response import Register201Response
from px0.models.register_request import RegisterRequest
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
    api_instance = px0.AuthApi(api_client)
    register_request = px0.RegisterRequest() # RegisterRequest | 

    try:
        # Register a new user
        api_response = api_instance.register(register_request)
        print("The response of AuthApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**Register201Response**](Register201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User registered successfully |  -  |
**400** | Invalid inputs |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Team Not Found |  -  |
**409** | Conflict (Email registered) |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> ResetPassword200Response reset_password(reset_password_request)

Reset Password

Resets a user's password using a valid reset code and a new password, deriving the user from the code in the database.

### Example


```python
import px0
from px0.models.reset_password200_response import ResetPassword200Response
from px0.models.reset_password_request import ResetPasswordRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.AuthApi(api_client)
    reset_password_request = px0.ResetPasswordRequest() # ResetPasswordRequest | 

    try:
        # Reset Password
        api_response = api_instance.reset_password(reset_password_request)
        print("The response of AuthApi->reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | 

### Return type

[**ResetPassword200Response**](ResetPassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password reset successfully |  -  |
**400** | Invalid input or invalid/expired code |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_password_reset**
> TriggerPasswordReset200Response trigger_password_reset(trigger_password_reset_request)

Trigger Password Reset

Generates a password reset code and sends it via email to the user.

### Example


```python
import px0
from px0.models.trigger_password_reset200_response import TriggerPasswordReset200Response
from px0.models.trigger_password_reset_request import TriggerPasswordResetRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.AuthApi(api_client)
    trigger_password_reset_request = px0.TriggerPasswordResetRequest() # TriggerPasswordResetRequest | 

    try:
        # Trigger Password Reset
        api_response = api_instance.trigger_password_reset(trigger_password_reset_request)
        print("The response of AuthApi->trigger_password_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->trigger_password_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_password_reset_request** | [**TriggerPasswordResetRequest**](TriggerPasswordResetRequest.md)|  | 

### Return type

[**TriggerPasswordReset200Response**](TriggerPasswordReset200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password reset email sent successfully |  -  |
**400** | Missing email |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_verification_email**
> TriggerVerificationEmail200Response trigger_verification_email(email)

Trigger Verification Email

Triggers a new email verification code and sends it to the user's email.

### Example


```python
import px0
from px0.models.trigger_verification_email200_response import TriggerVerificationEmail200Response
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.AuthApi(api_client)
    email = 'email_example' # str | The user's email address to trigger verification for.

    try:
        # Trigger Verification Email
        api_response = api_instance.trigger_verification_email(email)
        print("The response of AuthApi->trigger_verification_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->trigger_verification_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The user&#39;s email address to trigger verification for. | 

### Return type

[**TriggerVerificationEmail200Response**](TriggerVerificationEmail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification email sent successfully |  -  |
**400** | Missing email, invalid email, or user already verified |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_me**
> Register201Response update_me(update_me_request)

Update Me

Updates the profile of the currently logged-in user.

### Example

* Bearer Authentication (BearerAuth):

```python
import px0
from px0.models.register201_response import Register201Response
from px0.models.update_me_request import UpdateMeRequest
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
    api_instance = px0.AuthApi(api_client)
    update_me_request = px0.UpdateMeRequest() # UpdateMeRequest | 

    try:
        # Update Me
        api_response = api_instance.update_me(update_me_request)
        print("The response of AuthApi->update_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->update_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_me_request** | [**UpdateMeRequest**](UpdateMeRequest.md)|  | 

### Return type

[**Register201Response**](Register201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User profile updated successfully |  -  |
**400** | Invalid email format or missing fields |  -  |
**401** | Unauthorized |  -  |
**409** | Email already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email**
> VerifyEmail200Response verify_email(verify_request)

Verify User Email

Verifies a user's email address using a numeric code sent via email.

### Example


```python
import px0
from px0.models.verify_email200_response import VerifyEmail200Response
from px0.models.verify_request import VerifyRequest
from px0.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = px0.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with px0.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = px0.AuthApi(api_client)
    verify_request = px0.VerifyRequest() # VerifyRequest | 

    try:
        # Verify User Email
        api_response = api_instance.verify_email(verify_request)
        print("The response of AuthApi->verify_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->verify_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_request** | [**VerifyRequest**](VerifyRequest.md)|  | 

### Return type

[**VerifyEmail200Response**](VerifyEmail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email verified successfully |  -  |
**400** | Invalid code or expired code |  -  |
**401** | User not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

