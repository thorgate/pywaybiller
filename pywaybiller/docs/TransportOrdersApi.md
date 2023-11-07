# openapi_client.TransportOrdersApi

All URIs are relative to *https://staging.app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transport_orders_cancel**](TransportOrdersApi.md#transport_orders_cancel) | **POST** /transport-orders/{id}/cancel/ | Cancellation of a transport order
[**transport_orders_create**](TransportOrdersApi.md#transport_orders_create) | **POST** /transport-orders/ | Creation of a transport order
[**transport_orders_list**](TransportOrdersApi.md#transport_orders_list) | **GET** /transport-orders/ | Querying of transport orders
[**transport_orders_read**](TransportOrdersApi.md#transport_orders_read) | **GET** /transport-orders/{id}/ | Querying of a single transport order
[**transport_orders_update**](TransportOrdersApi.md#transport_orders_update) | **PUT** /transport-orders/{id}/ | Editing of a transport order


# **transport_orders_cancel**
> ExternalAPITransportOrderCancel transport_orders_cancel(id, data)

Cancellation of a transport order

Cancels transport order

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_transport_order_cancel import ExternalAPITransportOrderCancel
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
    api_instance = openapi_client.TransportOrdersApi(api_client)
    id = 'id_example' # str | 
    data = openapi_client.ExternalAPITransportOrderCancel() # ExternalAPITransportOrderCancel | 

    try:
        # Cancellation of a transport order
        api_response = api_instance.transport_orders_cancel(id, data)
        print("The response of TransportOrdersApi->transport_orders_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportOrdersApi->transport_orders_cancel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**ExternalAPITransportOrderCancel**](ExternalAPITransportOrderCancel.md)|  | 

### Return type

[**ExternalAPITransportOrderCancel**](ExternalAPITransportOrderCancel.md)

### Authorization

[API key](../README.md#API key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transport_orders_create**
> ExternalAPITransportOrder transport_orders_create(data)

Creation of a transport order

Creates a new transport order.<br><br>     **NB!** All posted IDs are IDs in your system and these are used to match objects in your     system with objects in Waybiller.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_transport_order import ExternalAPITransportOrder
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
    api_instance = openapi_client.TransportOrdersApi(api_client)
    data = openapi_client.ExternalAPITransportOrder() # ExternalAPITransportOrder | 

    try:
        # Creation of a transport order
        api_response = api_instance.transport_orders_create(data)
        print("The response of TransportOrdersApi->transport_orders_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportOrdersApi->transport_orders_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ExternalAPITransportOrder**](ExternalAPITransportOrder.md)|  | 

### Return type

[**ExternalAPITransportOrder**](ExternalAPITransportOrder.md)

### Authorization

[API key](../README.md#API key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transport_orders_list**
> TransportOrdersList200Response transport_orders_list(number=number, number__iexact=number__iexact, number__contains=number__contains, number__icontains=number__icontains, number__in=number__in, status=status, status__iexact=status__iexact, status__contains=status__contains, status__icontains=status__icontains, status__in=status__in, truck__truck__reg_number=truck__truck__reg_number, truck__truck__reg_number__iexact=truck__truck__reg_number__iexact, truck__truck__reg_number__contains=truck__truck__reg_number__contains, truck__truck__reg_number__icontains=truck__truck__reg_number__icontains, truck__truck__reg_number__in=truck__truck__reg_number__in, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

Querying of transport orders

Returns all transport orders associated with your company, according to the specified filters.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.transport_orders_list200_response import TransportOrdersList200Response
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
    api_instance = openapi_client.TransportOrdersApi(api_client)
    number = 'number_example' # str | Filters transport orders with specified number (case sensitive). (optional)
    number__iexact = 'number__iexact_example' # str | Filters transport orders with specified number (case insensitive). (optional)
    number__contains = 'number__contains_example' # str | Filters transport orders of which numbers contain this keyword (case sensitive). (optional)
    number__icontains = 'number__icontains_example' # str | Filters transport orders of which numbers contain this keyword (case insensitive). (optional)
    number__in = 'number__in_example' # str | Filters transport orders with specified list of transport order numbers. Multiple values may be separated by commas. (optional)
    status = 'status_example' # str | Filters transport orders with specified status (case sensitive). (optional)
    status__iexact = 'status__iexact_example' # str | Filters transport orders with specified status (case insensitive). (optional)
    status__contains = 'status__contains_example' # str | Filters transport orders of which statuses contain this keyword (case sensitive). (optional)
    status__icontains = 'status__icontains_example' # str | Filters transport orders of which statuses contain this keyword (case insensitive). (optional)
    status__in = 'status__in_example' # str | Filters transport orders with specified list of transport order statuses. Multiple values may be separated by commas. (optional)
    truck__truck__reg_number = 'truck__truck__reg_number_example' # str | Filters transport orders with specified truck reg number (case sensitive). (optional)
    truck__truck__reg_number__iexact = 'truck__truck__reg_number__iexact_example' # str | Filters transport orders with specified truck reg number (case insensitive). (optional)
    truck__truck__reg_number__contains = 'truck__truck__reg_number__contains_example' # str | Filters transport orders of which truck reg numbers contain this keyword (case sensitive). (optional)
    truck__truck__reg_number__icontains = 'truck__truck__reg_number__icontains_example' # str | Filters transport orders of which truck reg numbers contain this keyword (case insensitive). (optional)
    truck__truck__reg_number__in = 'truck__truck__reg_number__in_example' # str | Filters transport orders with specified list of transport order truck reg numbers. Multiple values may be separated by commas. (optional)
    start_date = 'start_date_example' # str | start_date (optional)
    end_date = 'end_date_example' # str | end_date (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        # Querying of transport orders
        api_response = api_instance.transport_orders_list(number=number, number__iexact=number__iexact, number__contains=number__contains, number__icontains=number__icontains, number__in=number__in, status=status, status__iexact=status__iexact, status__contains=status__contains, status__icontains=status__icontains, status__in=status__in, truck__truck__reg_number=truck__truck__reg_number, truck__truck__reg_number__iexact=truck__truck__reg_number__iexact, truck__truck__reg_number__contains=truck__truck__reg_number__contains, truck__truck__reg_number__icontains=truck__truck__reg_number__icontains, truck__truck__reg_number__in=truck__truck__reg_number__in, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of TransportOrdersApi->transport_orders_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportOrdersApi->transport_orders_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Filters transport orders with specified number (case sensitive). | [optional] 
 **number__iexact** | **str**| Filters transport orders with specified number (case insensitive). | [optional] 
 **number__contains** | **str**| Filters transport orders of which numbers contain this keyword (case sensitive). | [optional] 
 **number__icontains** | **str**| Filters transport orders of which numbers contain this keyword (case insensitive). | [optional] 
 **number__in** | **str**| Filters transport orders with specified list of transport order numbers. Multiple values may be separated by commas. | [optional] 
 **status** | **str**| Filters transport orders with specified status (case sensitive). | [optional] 
 **status__iexact** | **str**| Filters transport orders with specified status (case insensitive). | [optional] 
 **status__contains** | **str**| Filters transport orders of which statuses contain this keyword (case sensitive). | [optional] 
 **status__icontains** | **str**| Filters transport orders of which statuses contain this keyword (case insensitive). | [optional] 
 **status__in** | **str**| Filters transport orders with specified list of transport order statuses. Multiple values may be separated by commas. | [optional] 
 **truck__truck__reg_number** | **str**| Filters transport orders with specified truck reg number (case sensitive). | [optional] 
 **truck__truck__reg_number__iexact** | **str**| Filters transport orders with specified truck reg number (case insensitive). | [optional] 
 **truck__truck__reg_number__contains** | **str**| Filters transport orders of which truck reg numbers contain this keyword (case sensitive). | [optional] 
 **truck__truck__reg_number__icontains** | **str**| Filters transport orders of which truck reg numbers contain this keyword (case insensitive). | [optional] 
 **truck__truck__reg_number__in** | **str**| Filters transport orders with specified list of transport order truck reg numbers. Multiple values may be separated by commas. | [optional] 
 **start_date** | **str**| start_date | [optional] 
 **end_date** | **str**| end_date | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**TransportOrdersList200Response**](TransportOrdersList200Response.md)

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

# **transport_orders_read**
> ExternalAPITransportOrder transport_orders_read(id)

Querying of a single transport order

Returns a transport order with the specified ID. Only companies associated with the transport order can query     it.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_transport_order import ExternalAPITransportOrder
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
    api_instance = openapi_client.TransportOrdersApi(api_client)
    id = 'id_example' # str | The ID of the transport order queried.

    try:
        # Querying of a single transport order
        api_response = api_instance.transport_orders_read(id)
        print("The response of TransportOrdersApi->transport_orders_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportOrdersApi->transport_orders_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transport order queried. | 

### Return type

[**ExternalAPITransportOrder**](ExternalAPITransportOrder.md)

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

# **transport_orders_update**
> ExternalAPITransportOrderUpdate transport_orders_update(id, data)

Editing of a transport order

Edits transport order

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_transport_order_update import ExternalAPITransportOrderUpdate
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
    api_instance = openapi_client.TransportOrdersApi(api_client)
    id = 'id_example' # str | 
    data = openapi_client.ExternalAPITransportOrderUpdate() # ExternalAPITransportOrderUpdate | 

    try:
        # Editing of a transport order
        api_response = api_instance.transport_orders_update(id, data)
        print("The response of TransportOrdersApi->transport_orders_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportOrdersApi->transport_orders_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**ExternalAPITransportOrderUpdate**](ExternalAPITransportOrderUpdate.md)|  | 

### Return type

[**ExternalAPITransportOrderUpdate**](ExternalAPITransportOrderUpdate.md)

### Authorization

[API key](../README.md#API key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

