# openapi_client.LoaderActionLogsApi

All URIs are relative to *https://app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loader_action_logs_list**](LoaderActionLogsApi.md#loader_action_logs_list) | **GET** /loader-action-logs/ | Querying of loader action log data


# **loader_action_logs_list**
> LoaderActionLogsList200Response loader_action_logs_list(timestamp__lte=timestamp__lte, timestamp__gte=timestamp__gte, timestamp__lt=timestamp__lt, timestamp__gt=timestamp__gt, timestamp=timestamp, timestamp__isnull=timestamp__isnull, loader_unit_id=loader_unit_id, limit=limit, offset=offset)

Querying of loader action log data

Returns all loader action logs your company created, according to the specified filters.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.loader_action_logs_list200_response import LoaderActionLogsList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.waybiller.com/external-api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.waybiller.com/external-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API key
configuration.api_key['API key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LoaderActionLogsApi(api_client)
    timestamp__lte = 'timestamp__lte_example' # str | Filters loader action logs for your company within specified time period (less than or equal). (optional)
    timestamp__gte = 'timestamp__gte_example' # str | Filters loader action logs for your company within specified time period (greater than or equal). (optional)
    timestamp__lt = 'timestamp__lt_example' # str | Filters loader action logs for your company within specified time period (less than). (optional)
    timestamp__gt = 'timestamp__gt_example' # str | Filters loader action logs for your company within specified time period (greater than). (optional)
    timestamp = 'timestamp_example' # str | Filters loader action logs for your company within specified time period (exact). (optional)
    timestamp__isnull = 'timestamp__isnull_example' # str | Filters loader action logs for your company with timestamp null. (optional)
    loader_unit_id = 56 # int | Filters loader action logs for your company with specified loader unit id. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        # Querying of loader action log data
        api_response = api_instance.loader_action_logs_list(timestamp__lte=timestamp__lte, timestamp__gte=timestamp__gte, timestamp__lt=timestamp__lt, timestamp__gt=timestamp__gt, timestamp=timestamp, timestamp__isnull=timestamp__isnull, loader_unit_id=loader_unit_id, limit=limit, offset=offset)
        print("The response of LoaderActionLogsApi->loader_action_logs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoaderActionLogsApi->loader_action_logs_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp__lte** | **str**| Filters loader action logs for your company within specified time period (less than or equal). | [optional] 
 **timestamp__gte** | **str**| Filters loader action logs for your company within specified time period (greater than or equal). | [optional] 
 **timestamp__lt** | **str**| Filters loader action logs for your company within specified time period (less than). | [optional] 
 **timestamp__gt** | **str**| Filters loader action logs for your company within specified time period (greater than). | [optional] 
 **timestamp** | **str**| Filters loader action logs for your company within specified time period (exact). | [optional] 
 **timestamp__isnull** | **str**| Filters loader action logs for your company with timestamp null. | [optional] 
 **loader_unit_id** | **int**| Filters loader action logs for your company with specified loader unit id. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**LoaderActionLogsList200Response**](LoaderActionLogsList200Response.md)

### Authorization

[API key](../README.md#API key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

