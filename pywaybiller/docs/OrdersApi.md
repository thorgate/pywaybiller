# openapi_client.OrdersApi

All URIs are relative to *https://staging.app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_create**](OrdersApi.md#orders_create) | **POST** /orders/ | Creation of an order
[**orders_list**](OrdersApi.md#orders_list) | **GET** /orders/ | Querying of orders
[**orders_read**](OrdersApi.md#orders_read) | **GET** /orders/{id}/ | Querying of a single order
[**orders_transportation**](OrdersApi.md#orders_transportation) | **PUT** /orders/{id}/transportation/ | Editing of an order transportation companies and vehicles.
[**orders_update**](OrdersApi.md#orders_update) | **PUT** /orders/{id}/ | Editing of an order


# **orders_create**
> ExternalAPIOrderCreate orders_create(data)

Creation of an order

Creates a new order.<br><br>     **NB!** All posted IDs are IDs in your system and these are used to match objects in your     system with objects in Waybiller.     It is also possible to use the Waybiller IDs (`_raw_id`)     (if you have received it via GET endpoints (e.g. Destinations, Origin assortments).     Exception is `client`, where the `reg_code` is used as raw id.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_order_create import ExternalAPIOrderCreate
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
    api_instance = openapi_client.OrdersApi(api_client)
    data = openapi_client.ExternalAPIOrderCreate() # ExternalAPIOrderCreate | 

    try:
        # Creation of an order
        api_response = api_instance.orders_create(data)
        print("The response of OrdersApi->orders_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ExternalAPIOrderCreate**](ExternalAPIOrderCreate.md)|  | 

### Return type

[**ExternalAPIOrderCreate**](ExternalAPIOrderCreate.md)

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

# **orders_list**
> OrdersList200Response orders_list(limit=limit, offset=offset)

Querying of orders

Returns all orders associated with your company.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.orders_list200_response import OrdersList200Response
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
    api_instance = openapi_client.OrdersApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        # Querying of orders
        api_response = api_instance.orders_list(limit=limit, offset=offset)
        print("The response of OrdersApi->orders_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**OrdersList200Response**](OrdersList200Response.md)

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

# **orders_read**
> ExternalAPIOrder orders_read(id)

Querying of a single order

Returns an order with the specified ID. Only companies associated with the order can query it.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_order import ExternalAPIOrder
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 'id_example' # str | The ID of the order queried.

    try:
        # Querying of a single order
        api_response = api_instance.orders_read(id)
        print("The response of OrdersApi->orders_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the order queried. | 

### Return type

[**ExternalAPIOrder**](ExternalAPIOrder.md)

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

# **orders_transportation**
> ExternalAPIPartialOrderUpdate orders_transportation(id, data)

Editing of an order transportation companies and vehicles.

Edits order transportation companies and vehicles data. It is allowed to be used by order's client company

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_partial_order_update import ExternalAPIPartialOrderUpdate
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 'id_example' # str | 
    data = openapi_client.ExternalAPIPartialOrderUpdate() # ExternalAPIPartialOrderUpdate | 

    try:
        # Editing of an order transportation companies and vehicles.
        api_response = api_instance.orders_transportation(id, data)
        print("The response of OrdersApi->orders_transportation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_transportation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**ExternalAPIPartialOrderUpdate**](ExternalAPIPartialOrderUpdate.md)|  | 

### Return type

[**ExternalAPIPartialOrderUpdate**](ExternalAPIPartialOrderUpdate.md)

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

# **orders_update**
> ExternalAPIOrderUpdate orders_update(id, data)

Editing of an order

Edits order. It is allowed to be used by order's owner company

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_order_update import ExternalAPIOrderUpdate
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 'id_example' # str | 
    data = openapi_client.ExternalAPIOrderUpdate() # ExternalAPIOrderUpdate | 

    try:
        # Editing of an order
        api_response = api_instance.orders_update(id, data)
        print("The response of OrdersApi->orders_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**ExternalAPIOrderUpdate**](ExternalAPIOrderUpdate.md)|  | 

### Return type

[**ExternalAPIOrderUpdate**](ExternalAPIOrderUpdate.md)

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

