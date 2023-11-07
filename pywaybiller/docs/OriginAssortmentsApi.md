# openapi_client.OriginAssortmentsApi

All URIs are relative to *https://staging.app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**origin_assortments_list**](OriginAssortmentsApi.md#origin_assortments_list) | **GET** /origin-assortments/ | Querying of origin assortments
[**origin_assortments_read**](OriginAssortmentsApi.md#origin_assortments_read) | **GET** /origin-assortments/{id}/ | Querying of a single origin assortment


# **origin_assortments_list**
> OriginAssortmentsList200Response origin_assortments_list(origin__id__lte=origin__id__lte, origin__id__gte=origin__id__gte, origin__id__lt=origin__id__lt, origin__id__gt=origin__id__gt, origin__id=origin__id, origin__id__in=origin__id__in, origin__name=origin__name, origin__name__iexact=origin__name__iexact, origin__name__contains=origin__name__contains, origin__name__icontains=origin__name__icontains, assortment__name=assortment__name, assortment__name__iexact=assortment__name__iexact, assortment__name__contains=assortment__name__contains, assortment__name__icontains=assortment__name__icontains, subset_type__name=subset_type__name, subset_type__name__iexact=subset_type__name__iexact, subset_type__name__contains=subset_type__name__contains, subset_type__name__icontains=subset_type__name__icontains, subset__value=subset__value, subset__value__iexact=subset__value__iexact, subset__value__contains=subset__value__contains, subset__value__icontains=subset__value__icontains, limit=limit, offset=offset)

Querying of origin assortments

Returns all origin assortments (according to specified filters) that are associated with your company:     <ul>     <li>your company's origin assortments</li>     <li>your partner company's origin assortments</li>     <li>public origin assortments</li>     <ul>

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.origin_assortments_list200_response import OriginAssortmentsList200Response
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
    api_instance = openapi_client.OriginAssortmentsApi(api_client)
    origin__id__lte = 3.4 # float | Filters origin assortments with specified origin id (less than or equal to). (optional)
    origin__id__gte = 3.4 # float | Filters origin assortments with specified origin id (greater than or equal to). (optional)
    origin__id__lt = 3.4 # float | Filters origin assortments with specified origin id (less than). (optional)
    origin__id__gt = 3.4 # float | Filters origin assortments with specified origin id (greater than). (optional)
    origin__id = 3.4 # float | Filters origin assortments with specified origin id (exact). (optional)
    origin__id__in = 3.4 # float | Filters origin assortments with specified list of origin ids. Multiple values may be separated by commas. (optional)
    origin__name = 'origin__name_example' # str | Filters origin assortments with specified origin (case sensitive). (optional)
    origin__name__iexact = 'origin__name__iexact_example' # str | Filters origin assortments with specified origin (case insensitive). (optional)
    origin__name__contains = 'origin__name__contains_example' # str | Filters origin assortments of which origins contain this keyword (case sensitive). (optional)
    origin__name__icontains = 'origin__name__icontains_example' # str | Filters origin assortments of which origins contain this keyword (case insensitive). (optional)
    assortment__name = 'assortment__name_example' # str | Filters origin assortments with specified assortment (case sensitive). (optional)
    assortment__name__iexact = 'assortment__name__iexact_example' # str | Filters origin assortments with specified assortment (case insensitive). (optional)
    assortment__name__contains = 'assortment__name__contains_example' # str | Filters origin assortments of which assortments contain this keyword (case sensitive). (optional)
    assortment__name__icontains = 'assortment__name__icontains_example' # str | Filters origin assortments of which assortments contain this keyword (case insensitive). (optional)
    subset_type__name = 'subset_type__name_example' # str | Filters origin assortments with specified subset type (case sensitive). (optional)
    subset_type__name__iexact = 'subset_type__name__iexact_example' # str | Filters origin assortments with specified subset type (case insensitive). (optional)
    subset_type__name__contains = 'subset_type__name__contains_example' # str | Filters origin assortments of which subset types contain this keyword (case sensitive). (optional)
    subset_type__name__icontains = 'subset_type__name__icontains_example' # str | Filters origin assortments of which subset types contain this keyword (case insensitive). (optional)
    subset__value = 'subset__value_example' # str | Filters origin assortments with specified subset (case sensitive). (optional)
    subset__value__iexact = 'subset__value__iexact_example' # str | Filters origin assortments with specified subset (case insensitive). (optional)
    subset__value__contains = 'subset__value__contains_example' # str | Filters origin assortments of which subsets contain this keyword (case sensitive). (optional)
    subset__value__icontains = 'subset__value__icontains_example' # str | Filters origin assortments of which subsets contain this keyword (case insensitive). (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        # Querying of origin assortments
        api_response = api_instance.origin_assortments_list(origin__id__lte=origin__id__lte, origin__id__gte=origin__id__gte, origin__id__lt=origin__id__lt, origin__id__gt=origin__id__gt, origin__id=origin__id, origin__id__in=origin__id__in, origin__name=origin__name, origin__name__iexact=origin__name__iexact, origin__name__contains=origin__name__contains, origin__name__icontains=origin__name__icontains, assortment__name=assortment__name, assortment__name__iexact=assortment__name__iexact, assortment__name__contains=assortment__name__contains, assortment__name__icontains=assortment__name__icontains, subset_type__name=subset_type__name, subset_type__name__iexact=subset_type__name__iexact, subset_type__name__contains=subset_type__name__contains, subset_type__name__icontains=subset_type__name__icontains, subset__value=subset__value, subset__value__iexact=subset__value__iexact, subset__value__contains=subset__value__contains, subset__value__icontains=subset__value__icontains, limit=limit, offset=offset)
        print("The response of OriginAssortmentsApi->origin_assortments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OriginAssortmentsApi->origin_assortments_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin__id__lte** | **float**| Filters origin assortments with specified origin id (less than or equal to). | [optional] 
 **origin__id__gte** | **float**| Filters origin assortments with specified origin id (greater than or equal to). | [optional] 
 **origin__id__lt** | **float**| Filters origin assortments with specified origin id (less than). | [optional] 
 **origin__id__gt** | **float**| Filters origin assortments with specified origin id (greater than). | [optional] 
 **origin__id** | **float**| Filters origin assortments with specified origin id (exact). | [optional] 
 **origin__id__in** | **float**| Filters origin assortments with specified list of origin ids. Multiple values may be separated by commas. | [optional] 
 **origin__name** | **str**| Filters origin assortments with specified origin (case sensitive). | [optional] 
 **origin__name__iexact** | **str**| Filters origin assortments with specified origin (case insensitive). | [optional] 
 **origin__name__contains** | **str**| Filters origin assortments of which origins contain this keyword (case sensitive). | [optional] 
 **origin__name__icontains** | **str**| Filters origin assortments of which origins contain this keyword (case insensitive). | [optional] 
 **assortment__name** | **str**| Filters origin assortments with specified assortment (case sensitive). | [optional] 
 **assortment__name__iexact** | **str**| Filters origin assortments with specified assortment (case insensitive). | [optional] 
 **assortment__name__contains** | **str**| Filters origin assortments of which assortments contain this keyword (case sensitive). | [optional] 
 **assortment__name__icontains** | **str**| Filters origin assortments of which assortments contain this keyword (case insensitive). | [optional] 
 **subset_type__name** | **str**| Filters origin assortments with specified subset type (case sensitive). | [optional] 
 **subset_type__name__iexact** | **str**| Filters origin assortments with specified subset type (case insensitive). | [optional] 
 **subset_type__name__contains** | **str**| Filters origin assortments of which subset types contain this keyword (case sensitive). | [optional] 
 **subset_type__name__icontains** | **str**| Filters origin assortments of which subset types contain this keyword (case insensitive). | [optional] 
 **subset__value** | **str**| Filters origin assortments with specified subset (case sensitive). | [optional] 
 **subset__value__iexact** | **str**| Filters origin assortments with specified subset (case insensitive). | [optional] 
 **subset__value__contains** | **str**| Filters origin assortments of which subsets contain this keyword (case sensitive). | [optional] 
 **subset__value__icontains** | **str**| Filters origin assortments of which subsets contain this keyword (case insensitive). | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**OriginAssortmentsList200Response**](OriginAssortmentsList200Response.md)

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

# **origin_assortments_read**
> ExternalAPIOriginAssortment origin_assortments_read(id)

Querying of a single origin assortment

Returns an origin assortment with the specified ID. It is possible to query only the origin assortment that     your company has access to:     <ul>     <li>your company's origin assortments</li>     <li>your partner company's origin assortments</li>     <li>public origin assortments</li>     <ul>

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_origin_assortment import ExternalAPIOriginAssortment
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
    api_instance = openapi_client.OriginAssortmentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Querying of a single origin assortment
        api_response = api_instance.origin_assortments_read(id)
        print("The response of OriginAssortmentsApi->origin_assortments_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OriginAssortmentsApi->origin_assortments_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ExternalAPIOriginAssortment**](ExternalAPIOriginAssortment.md)

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

