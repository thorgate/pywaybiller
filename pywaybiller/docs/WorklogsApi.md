# openapi_client.WorklogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**worklogs_create**](WorklogsApi.md#worklogs_create) | **POST** /external-api/worklogs/ | Creation of a time entry
[**worklogs_list**](WorklogsApi.md#worklogs_list) | **GET** /external-api/worklogs/ | Querying time entries


# **worklogs_create**
> ExternalAPITimeEntry worklogs_create(external_api_time_entry_request)

Creation of a time entry

Creates a new time entry associated with your company.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.external_api_time_entry import ExternalAPITimeEntry
from openapi_client.models.external_api_time_entry_request import ExternalAPITimeEntryRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WorklogsApi(api_client)
    external_api_time_entry_request = openapi_client.ExternalAPITimeEntryRequest() # ExternalAPITimeEntryRequest | 

    try:
        # Creation of a time entry
        api_response = api_instance.worklogs_create(external_api_time_entry_request)
        print("The response of WorklogsApi->worklogs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorklogsApi->worklogs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_api_time_entry_request** | [**ExternalAPITimeEntryRequest**](ExternalAPITimeEntryRequest.md)|  | 

### Return type

[**ExternalAPITimeEntry**](ExternalAPITimeEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worklogs_list**
> PaginatedExternalAPITimeEntryList worklogs_list(limit=limit, offset=offset)

Querying time entries

Returns all time entries associated with your company.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.paginated_external_api_time_entry_list import PaginatedExternalAPITimeEntryList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WorklogsApi(api_client)
    limit = 30 # int | Maximum number of objects to return per page (optional) (default to 30)
    offset = 0 # int | The initial index from which to return the results (optional) (default to 0)

    try:
        # Querying time entries
        api_response = api_instance.worklogs_list(limit=limit, offset=offset)
        print("The response of WorklogsApi->worklogs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorklogsApi->worklogs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of objects to return per page | [optional] [default to 30]
 **offset** | **int**| The initial index from which to return the results | [optional] [default to 0]

### Return type

[**PaginatedExternalAPITimeEntryList**](PaginatedExternalAPITimeEntryList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

