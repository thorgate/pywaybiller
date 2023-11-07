# openapi_client.OriginsApi

All URIs are relative to *https://staging.app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**origins_create**](OriginsApi.md#origins_create) | **POST** /origins/ | Creation of origin
[**origins_list**](OriginsApi.md#origins_list) | **GET** /origins/ | Querying of origins
[**origins_read**](OriginsApi.md#origins_read) | **GET** /origins/{id}/ | Querying of a single origin
[**origins_update**](OriginsApi.md#origins_update) | **PUT** /origins/{id}/ | Editing of an origin


# **origins_create**
> ExtAPIOriginCreate origins_create(data)

Creation of origin

Creates a new origin.<br><br>     **NB!** All posted IDs are Waybiller IDs.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.ext_api_origin_create import ExtAPIOriginCreate
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
    api_instance = openapi_client.OriginsApi(api_client)
    data = openapi_client.ExtAPIOriginCreate() # ExtAPIOriginCreate | 

    try:
        # Creation of origin
        api_response = api_instance.origins_create(data)
        print("The response of OriginsApi->origins_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OriginsApi->origins_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ExtAPIOriginCreate**](ExtAPIOriginCreate.md)|  | 

### Return type

[**ExtAPIOriginCreate**](ExtAPIOriginCreate.md)

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

# **origins_list**
> OriginsList200Response origins_list(name=name, name__iexact=name__iexact, name__contains=name__contains, name__icontains=name__icontains, location__address=location__address, location__address__iexact=location__address__iexact, location__address__contains=location__address__contains, location__address__icontains=location__address__icontains, company__reg_code=company__reg_code, company__reg_code__iexact=company__reg_code__iexact, company__reg_code__contains=company__reg_code__contains, company__reg_code__icontains=company__reg_code__icontains, limit=limit, offset=offset, explicitly_viewable=explicitly_viewable)

Querying of origins

Returns all origins associated with your company, according to the specified filters.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.origins_list200_response import OriginsList200Response
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
    api_instance = openapi_client.OriginsApi(api_client)
    name = 'name_example' # str | Filters origins with specified name (case sensitive). (optional)
    name__iexact = 'name__iexact_example' # str | Filters origins with specified name (case insensitive). (optional)
    name__contains = 'name__contains_example' # str | Filters origins of which names contain this keyword (case sensitive). (optional)
    name__icontains = 'name__icontains_example' # str | Filters origins of which names contain this keyword (case insensitive). (optional)
    location__address = 'location__address_example' # str | Filters origins with specified address (case sensitive). (optional)
    location__address__iexact = 'location__address__iexact_example' # str | Filters origins with specified address (case insensitive). (optional)
    location__address__contains = 'location__address__contains_example' # str | Filters origins of which addresses contain this keyword (case sensitive). (optional)
    location__address__icontains = 'location__address__icontains_example' # str | Filters origins of which addresses contain this keyword (case insensitive). (optional)
    company__reg_code = 'company__reg_code_example' # str | Filters origins belonging to the company with the specified register code (case sensitive). (optional)
    company__reg_code__iexact = 'company__reg_code__iexact_example' # str | Filters origins belonging to the company with the specified register code (case insensitive). (optional)
    company__reg_code__contains = 'company__reg_code__contains_example' # str | Filters origins belonging to the company of which register codes contain this keyword (case sensitive). (optional)
    company__reg_code__icontains = 'company__reg_code__icontains_example' # str | Filters origins belonging to the company of which register codes contain this keyword (case insensitive). (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    explicitly_viewable = True # bool | Filters origins that belong to your company or where your company was added as a partner. (optional)

    try:
        # Querying of origins
        api_response = api_instance.origins_list(name=name, name__iexact=name__iexact, name__contains=name__contains, name__icontains=name__icontains, location__address=location__address, location__address__iexact=location__address__iexact, location__address__contains=location__address__contains, location__address__icontains=location__address__icontains, company__reg_code=company__reg_code, company__reg_code__iexact=company__reg_code__iexact, company__reg_code__contains=company__reg_code__contains, company__reg_code__icontains=company__reg_code__icontains, limit=limit, offset=offset, explicitly_viewable=explicitly_viewable)
        print("The response of OriginsApi->origins_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OriginsApi->origins_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filters origins with specified name (case sensitive). | [optional] 
 **name__iexact** | **str**| Filters origins with specified name (case insensitive). | [optional] 
 **name__contains** | **str**| Filters origins of which names contain this keyword (case sensitive). | [optional] 
 **name__icontains** | **str**| Filters origins of which names contain this keyword (case insensitive). | [optional] 
 **location__address** | **str**| Filters origins with specified address (case sensitive). | [optional] 
 **location__address__iexact** | **str**| Filters origins with specified address (case insensitive). | [optional] 
 **location__address__contains** | **str**| Filters origins of which addresses contain this keyword (case sensitive). | [optional] 
 **location__address__icontains** | **str**| Filters origins of which addresses contain this keyword (case insensitive). | [optional] 
 **company__reg_code** | **str**| Filters origins belonging to the company with the specified register code (case sensitive). | [optional] 
 **company__reg_code__iexact** | **str**| Filters origins belonging to the company with the specified register code (case insensitive). | [optional] 
 **company__reg_code__contains** | **str**| Filters origins belonging to the company of which register codes contain this keyword (case sensitive). | [optional] 
 **company__reg_code__icontains** | **str**| Filters origins belonging to the company of which register codes contain this keyword (case insensitive). | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **explicitly_viewable** | **bool**| Filters origins that belong to your company or where your company was added as a partner. | [optional] 

### Return type

[**OriginsList200Response**](OriginsList200Response.md)

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

# **origins_read**
> ExtAPIOriginRead origins_read(id)

Querying of a single origin

Returns an origin with the specified ID. Only owner company and partner companies can query non-public origins.     Public origins are available for everyone.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.ext_api_origin_read import ExtAPIOriginRead
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
    api_instance = openapi_client.OriginsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Querying of a single origin
        api_response = api_instance.origins_read(id)
        print("The response of OriginsApi->origins_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OriginsApi->origins_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ExtAPIOriginRead**](ExtAPIOriginRead.md)

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

# **origins_update**
> ExtAPIOriginUpdate origins_update(id, data)

Editing of an origin

Edits origin. It is allowed to be used by origin's owner company.<br><br>     **NB!** All posted IDs are Waybiller IDs.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.ext_api_origin_update import ExtAPIOriginUpdate
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
    api_instance = openapi_client.OriginsApi(api_client)
    id = 'id_example' # str | 
    data = openapi_client.ExtAPIOriginUpdate() # ExtAPIOriginUpdate | 

    try:
        # Editing of an origin
        api_response = api_instance.origins_update(id, data)
        print("The response of OriginsApi->origins_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OriginsApi->origins_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**ExtAPIOriginUpdate**](ExtAPIOriginUpdate.md)|  | 

### Return type

[**ExtAPIOriginUpdate**](ExtAPIOriginUpdate.md)

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

