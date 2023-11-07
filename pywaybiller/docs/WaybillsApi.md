# openapi_client.WaybillsApi

All URIs are relative to *https://staging.app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**waybills_accept**](WaybillsApi.md#waybills_accept) | **PUT** /waybills/{id}/accept/ | Accepting waybill
[**waybills_cancel**](WaybillsApi.md#waybills_cancel) | **PUT** /waybills/{id}/cancel/ | Cancelling waybill
[**waybills_comment**](WaybillsApi.md#waybills_comment) | **POST** /waybills/{id}/comment/ | Commenting waybill
[**waybills_create**](WaybillsApi.md#waybills_create) | **POST** /waybills/ | Creation of a waybill
[**waybills_finish_drive**](WaybillsApi.md#waybills_finish_drive) | **POST** /waybills/{id}/finish_drive/ | Completing driving
[**waybills_list**](WaybillsApi.md#waybills_list) | **GET** /waybills/ | Querying of waybills
[**waybills_read**](WaybillsApi.md#waybills_read) | **GET** /waybills/{id}/ | Querying of a single waybill
[**waybills_refuse**](WaybillsApi.md#waybills_refuse) | **PUT** /waybills/{id}/refuse/ | Refusing waybill
[**waybills_start_drive**](WaybillsApi.md#waybills_start_drive) | **POST** /waybills/{id}/start_drive/ | Starting driving
[**waybills_update_accepted_amounts**](WaybillsApi.md#waybills_update_accepted_amounts) | **PUT** /waybills/{id}/update_accepted_amounts/ | Updating of accepted amounts
[**waybills_update_dispatched_amounts**](WaybillsApi.md#waybills_update_dispatched_amounts) | **PUT** /waybills/{id}/update_dispatched_amounts/ | Updating of dispatched amounts
[**waybills_vehicle_location_data**](WaybillsApi.md#waybills_vehicle_location_data) | **GET** /waybills/{id}/vehicle_location_data/ | Querying of vehicle location data


# **waybills_accept**
> ExternalAPIWaybillAccept waybills_accept(id, data)

Accepting waybill

Sets the status of a waybill to `accepted`. Only the receiving company of the waybill is authorized to accept     the waybill.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_accept import ExternalAPIWaybillAccept
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillAccept() # ExternalAPIWaybillAccept | 

    try:
        # Accepting waybill
        api_response = api_instance.waybills_accept(id, data)
        print("The response of WaybillsApi->waybills_accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_accept: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillAccept**](ExternalAPIWaybillAccept.md)|  | 

### Return type

[**ExternalAPIWaybillAccept**](ExternalAPIWaybillAccept.md)

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

# **waybills_cancel**
> ExternalAPIWaybillCancel waybills_cancel(id, data)

Cancelling waybill

Marks waybill as `cancelled`. Any waybill can be cancelled except waybills with status `accepted`.     Waybill can be cancelled by origin owner, transportation company or receiver company or its representative.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_cancel import ExternalAPIWaybillCancel
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillCancel() # ExternalAPIWaybillCancel | 

    try:
        # Cancelling waybill
        api_response = api_instance.waybills_cancel(id, data)
        print("The response of WaybillsApi->waybills_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_cancel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillCancel**](ExternalAPIWaybillCancel.md)|  | 

### Return type

[**ExternalAPIWaybillCancel**](ExternalAPIWaybillCancel.md)

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

# **waybills_comment**
> ExternalAPIWaybillComment waybills_comment(id, data)

Commenting waybill

Adds a comment to the waybill. Only companies associated with the waybill can add comments to it.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_comment import ExternalAPIWaybillComment
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillComment() # ExternalAPIWaybillComment | 

    try:
        # Commenting waybill
        api_response = api_instance.waybills_comment(id, data)
        print("The response of WaybillsApi->waybills_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillComment**](ExternalAPIWaybillComment.md)|  | 

### Return type

[**ExternalAPIWaybillComment**](ExternalAPIWaybillComment.md)

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

# **waybills_create**
> ExternalAPIWaybillCreate waybills_create(data)

Creation of a waybill

Creates a new waybill.<br><br>     **NB!** In this way posted IDs are IDs in your system and these are used to match objects in     your system with objects in Waybiller.     It is also possible to use the origin or destination ID in Waybiller     (if you have received those via GET Origins or GET Destinations endpoints).

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_create import ExternalAPIWaybillCreate
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
    api_instance = openapi_client.WaybillsApi(api_client)
    data = openapi_client.ExternalAPIWaybillCreate() # ExternalAPIWaybillCreate | 

    try:
        # Creation of a waybill
        api_response = api_instance.waybills_create(data)
        print("The response of WaybillsApi->waybills_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ExternalAPIWaybillCreate**](ExternalAPIWaybillCreate.md)|  | 

### Return type

[**ExternalAPIWaybillCreate**](ExternalAPIWaybillCreate.md)

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

# **waybills_finish_drive**
> ExternalAPIWaybillFinishDrive waybills_finish_drive(id, data)

Completing driving

Sets the status of a waybill to `in destination`. Waybill status has to be `in progress` to use this endpoint.     Only the transportation company or receiving company of the waybill are authorized to move waybill to `in     destination`.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_finish_drive import ExternalAPIWaybillFinishDrive
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillFinishDrive() # ExternalAPIWaybillFinishDrive | 

    try:
        # Completing driving
        api_response = api_instance.waybills_finish_drive(id, data)
        print("The response of WaybillsApi->waybills_finish_drive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_finish_drive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillFinishDrive**](ExternalAPIWaybillFinishDrive.md)|  | 

### Return type

[**ExternalAPIWaybillFinishDrive**](ExternalAPIWaybillFinishDrive.md)

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

# **waybills_list**
> WaybillsList200Response waybills_list(limit=limit, offset=offset, dispatcher_timestamp__gt=dispatcher_timestamp__gt, dispatcher_timestamp__lt=dispatcher_timestamp__lt)

Querying of waybills

Returns all waybills associated with your company, according to the specified filters.<br><br>     **NB!** By default, past 30 days according to the `dispatcher_timestamp` field waybills are returned. Use     `dispatcher_timestamp__lt` and `dispatcher_timestamp__gt` for filtering. Note that the maximum range is 30 days.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.waybills_list200_response import WaybillsList200Response
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
    api_instance = openapi_client.WaybillsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    dispatcher_timestamp__gt = 'dispatcher_timestamp__gt_example' # str |  (optional)
    dispatcher_timestamp__lt = 'dispatcher_timestamp__lt_example' # str |  (optional)

    try:
        # Querying of waybills
        api_response = api_instance.waybills_list(limit=limit, offset=offset, dispatcher_timestamp__gt=dispatcher_timestamp__gt, dispatcher_timestamp__lt=dispatcher_timestamp__lt)
        print("The response of WaybillsApi->waybills_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **dispatcher_timestamp__gt** | **str**|  | [optional] 
 **dispatcher_timestamp__lt** | **str**|  | [optional] 

### Return type

[**WaybillsList200Response**](WaybillsList200Response.md)

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

# **waybills_read**
> ExternalAPIWaybillRetrieve waybills_read(id)

Querying of a single waybill

Returns a waybill with the specified ID. Only companies associated with the waybill can query it.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_retrieve import ExternalAPIWaybillRetrieve
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill queried.

    try:
        # Querying of a single waybill
        api_response = api_instance.waybills_read(id)
        print("The response of WaybillsApi->waybills_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill queried. | 

### Return type

[**ExternalAPIWaybillRetrieve**](ExternalAPIWaybillRetrieve.md)

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

# **waybills_refuse**
> ExternalAPIWaybillRefuse waybills_refuse(id, data)

Refusing waybill

Marks waybill as `refused` in destination and sets the status of waybill to in progress again.     If new destination is provided, then new destination is set for the waybill.     Only the transportation company or receiving company of the waybill are authorized to refuse the waybill.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_refuse import ExternalAPIWaybillRefuse
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillRefuse() # ExternalAPIWaybillRefuse | 

    try:
        # Refusing waybill
        api_response = api_instance.waybills_refuse(id, data)
        print("The response of WaybillsApi->waybills_refuse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_refuse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillRefuse**](ExternalAPIWaybillRefuse.md)|  | 

### Return type

[**ExternalAPIWaybillRefuse**](ExternalAPIWaybillRefuse.md)

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

# **waybills_start_drive**
> ExternalAPIWaybillStartDrive waybills_start_drive(id, data)

Starting driving

Sets the status of a waybill to `in progress`. Waybill status has to be `created` to use this endpoint. Only     the transportation company or receiving company of the waybill are authorized to move waybill to `in     progress`.<br><br>     **NB!** Destination needs to belong to the receiving company in case the origin’s     `feature_waybill_destination_changing_disabled_for_drivers` flag is set to `True`.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_start_drive import ExternalAPIWaybillStartDrive
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillStartDrive() # ExternalAPIWaybillStartDrive | 

    try:
        # Starting driving
        api_response = api_instance.waybills_start_drive(id, data)
        print("The response of WaybillsApi->waybills_start_drive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_start_drive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillStartDrive**](ExternalAPIWaybillStartDrive.md)|  | 

### Return type

[**ExternalAPIWaybillStartDrive**](ExternalAPIWaybillStartDrive.md)

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

# **waybills_update_accepted_amounts**
> ExternalAPIWaybillAcceptedAmounts waybills_update_accepted_amounts(id, data)

Updating of accepted amounts

Sets the accepted amounts for the waybill. Authorized only for the receiving company of the waybill.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_accepted_amounts import ExternalAPIWaybillAcceptedAmounts
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillAcceptedAmounts() # ExternalAPIWaybillAcceptedAmounts | 

    try:
        # Updating of accepted amounts
        api_response = api_instance.waybills_update_accepted_amounts(id, data)
        print("The response of WaybillsApi->waybills_update_accepted_amounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_update_accepted_amounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillAcceptedAmounts**](ExternalAPIWaybillAcceptedAmounts.md)|  | 

### Return type

[**ExternalAPIWaybillAcceptedAmounts**](ExternalAPIWaybillAcceptedAmounts.md)

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

# **waybills_update_dispatched_amounts**
> ExternalAPIWaybillDispatchedAmounts waybills_update_dispatched_amounts(id, data)

Updating of dispatched amounts

Sets the dispatched amounts for the waybill. Authorized only for the origin company of the waybill.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_dispatched_amounts import ExternalAPIWaybillDispatchedAmounts
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.
    data = openapi_client.ExternalAPIWaybillDispatchedAmounts() # ExternalAPIWaybillDispatchedAmounts | 

    try:
        # Updating of dispatched amounts
        api_response = api_instance.waybills_update_dispatched_amounts(id, data)
        print("The response of WaybillsApi->waybills_update_dispatched_amounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_update_dispatched_amounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 
 **data** | [**ExternalAPIWaybillDispatchedAmounts**](ExternalAPIWaybillDispatchedAmounts.md)|  | 

### Return type

[**ExternalAPIWaybillDispatchedAmounts**](ExternalAPIWaybillDispatchedAmounts.md)

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

# **waybills_vehicle_location_data**
> ExternalAPIWaybillVehicleLocation waybills_vehicle_location_data(id)

Querying of vehicle location data

Returns vehicle location data.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.external_api_waybill_vehicle_location import ExternalAPIWaybillVehicleLocation
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
    api_instance = openapi_client.WaybillsApi(api_client)
    id = 'id_example' # str | The ID of the waybill.

    try:
        # Querying of vehicle location data
        api_response = api_instance.waybills_vehicle_location_data(id)
        print("The response of WaybillsApi->waybills_vehicle_location_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillsApi->waybills_vehicle_location_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the waybill. | 

### Return type

[**ExternalAPIWaybillVehicleLocation**](ExternalAPIWaybillVehicleLocation.md)

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

