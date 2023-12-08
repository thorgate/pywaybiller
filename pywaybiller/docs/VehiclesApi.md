# openapi_client.VehiclesApi

All URIs are relative to *https://app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vehicles_list**](VehiclesApi.md#vehicles_list) | **GET** /vehicles/ | Querying of vehicles


# **vehicles_list**
> VehiclesList200Response vehicles_list(limit=limit, offset=offset)

Querying of vehicles

Returns all vehicles associated with your company and with your subcontractors.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.vehicles_list200_response import VehiclesList200Response
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
    api_instance = openapi_client.VehiclesApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        # Querying of vehicles
        api_response = api_instance.vehicles_list(limit=limit, offset=offset)
        print("The response of VehiclesApi->vehicles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VehiclesApi->vehicles_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**VehiclesList200Response**](VehiclesList200Response.md)

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

