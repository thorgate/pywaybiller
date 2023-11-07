# openapi_client.DestinationsApi

All URIs are relative to *https://staging.app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destinations_list**](DestinationsApi.md#destinations_list) | **GET** /destinations/ | Querying of destinations


# **destinations_list**
> DestinationsList200Response destinations_list(name=name, name__iexact=name__iexact, name__contains=name__contains, name__icontains=name__icontains, location__address=location__address, location__address__iexact=location__address__iexact, location__address__contains=location__address__contains, location__address__icontains=location__address__icontains, company__reg_code=company__reg_code, company__reg_code__iexact=company__reg_code__iexact, company__reg_code__contains=company__reg_code__contains, company__reg_code__icontains=company__reg_code__icontains, limit=limit, offset=offset, explicitly_viewable=explicitly_viewable)

Querying of destinations

Returns all destinations associated with your company, according to the specified filters.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.destinations_list200_response import DestinationsList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.app.waybiller.com/external-api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.app.waybiller.com/external-api"
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
    api_instance = openapi_client.DestinationsApi(api_client)
    name = 'name_example' # str | Filters destinations with specified name (case sensitive). (optional)
    name__iexact = 'name__iexact_example' # str | Filters destinations with specified name (case insensitive). (optional)
    name__contains = 'name__contains_example' # str | Filters destinations of which names contain this keyword (case sensitive). (optional)
    name__icontains = 'name__icontains_example' # str | Filters destinations of which names contain this keyword (case insensitive). (optional)
    location__address = 'location__address_example' # str | Filters destinations with specified address (case sensitive). (optional)
    location__address__iexact = 'location__address__iexact_example' # str | Filters destinations with specified address (case insensitive). (optional)
    location__address__contains = 'location__address__contains_example' # str | Filters destinations of which addresses contain this keyword (case sensitive). (optional)
    location__address__icontains = 'location__address__icontains_example' # str | Filters destinations of which addresses contain this keyword (case insensitive). (optional)
    company__reg_code = 'company__reg_code_example' # str | Filters destinations belonging to the company with the specified register code (case sensitive). (optional)
    company__reg_code__iexact = 'company__reg_code__iexact_example' # str | Filters destinations belonging to the company with the specified register code (case insensitive). (optional)
    company__reg_code__contains = 'company__reg_code__contains_example' # str | Filters destinations belonging to the company of which register codes contain this keyword (case sensitive). (optional)
    company__reg_code__icontains = 'company__reg_code__icontains_example' # str | Filters destinations belonging to the company of which register codes contain this keyword (case insensitive). (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    explicitly_viewable = True # bool | Filters destinations that belong to your company or where your company was added as a partner. (optional)

    try:
        # Querying of destinations
        api_response = api_instance.destinations_list(name=name, name__iexact=name__iexact, name__contains=name__contains, name__icontains=name__icontains, location__address=location__address, location__address__iexact=location__address__iexact, location__address__contains=location__address__contains, location__address__icontains=location__address__icontains, company__reg_code=company__reg_code, company__reg_code__iexact=company__reg_code__iexact, company__reg_code__contains=company__reg_code__contains, company__reg_code__icontains=company__reg_code__icontains, limit=limit, offset=offset, explicitly_viewable=explicitly_viewable)
        print("The response of DestinationsApi->destinations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->destinations_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filters destinations with specified name (case sensitive). | [optional] 
 **name__iexact** | **str**| Filters destinations with specified name (case insensitive). | [optional] 
 **name__contains** | **str**| Filters destinations of which names contain this keyword (case sensitive). | [optional] 
 **name__icontains** | **str**| Filters destinations of which names contain this keyword (case insensitive). | [optional] 
 **location__address** | **str**| Filters destinations with specified address (case sensitive). | [optional] 
 **location__address__iexact** | **str**| Filters destinations with specified address (case insensitive). | [optional] 
 **location__address__contains** | **str**| Filters destinations of which addresses contain this keyword (case sensitive). | [optional] 
 **location__address__icontains** | **str**| Filters destinations of which addresses contain this keyword (case insensitive). | [optional] 
 **company__reg_code** | **str**| Filters destinations belonging to the company with the specified register code (case sensitive). | [optional] 
 **company__reg_code__iexact** | **str**| Filters destinations belonging to the company with the specified register code (case insensitive). | [optional] 
 **company__reg_code__contains** | **str**| Filters destinations belonging to the company of which register codes contain this keyword (case sensitive). | [optional] 
 **company__reg_code__icontains** | **str**| Filters destinations belonging to the company of which register codes contain this keyword (case insensitive). | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **explicitly_viewable** | **bool**| Filters destinations that belong to your company or where your company was added as a partner. | [optional] 

### Return type

[**DestinationsList200Response**](DestinationsList200Response.md)

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

