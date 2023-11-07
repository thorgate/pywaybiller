# openapi_client.VehicleLocationDataApi

All URIs are relative to *https://app.waybiller.com/external-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vehicle_location_data_list**](VehicleLocationDataApi.md#vehicle_location_data_list) | **GET** /vehicle-location-data/ | Querying of vehicle location data


# **vehicle_location_data_list**
> VehicleLocationDataList200Response vehicle_location_data_list(dispatcher_timestamp__lte=dispatcher_timestamp__lte, dispatcher_timestamp__gte=dispatcher_timestamp__gte, dispatcher_timestamp__lt=dispatcher_timestamp__lt, dispatcher_timestamp__gt=dispatcher_timestamp__gt, dispatcher_timestamp=dispatcher_timestamp, dispatcher_timestamp__isnull=dispatcher_timestamp__isnull, driver_timestamp__lte=driver_timestamp__lte, driver_timestamp__gte=driver_timestamp__gte, driver_timestamp__lt=driver_timestamp__lt, driver_timestamp__gt=driver_timestamp__gt, driver_timestamp=driver_timestamp, driver_timestamp__isnull=driver_timestamp__isnull, confirmed_timestamp__lte=confirmed_timestamp__lte, confirmed_timestamp__gte=confirmed_timestamp__gte, confirmed_timestamp__lt=confirmed_timestamp__lt, confirmed_timestamp__gt=confirmed_timestamp__gt, confirmed_timestamp=confirmed_timestamp, confirmed_timestamp__isnull=confirmed_timestamp__isnull, cancelled_timestamp__lte=cancelled_timestamp__lte, cancelled_timestamp__gte=cancelled_timestamp__gte, cancelled_timestamp__lt=cancelled_timestamp__lt, cancelled_timestamp__gt=cancelled_timestamp__gt, cancelled_timestamp=cancelled_timestamp, cancelled_timestamp__isnull=cancelled_timestamp__isnull, limit=limit, offset=offset, waybill_number=waybill_number, truck_reg_number=truck_reg_number, waybill_status=waybill_status, destination_id=destination_id)

Querying of vehicle location data

Returns all vehicle location data for waybills associated with your company, according to the specified filters.

### Example

* Api Key Authentication (API key):
```python
import time
import os
import openapi_client
from openapi_client.models.vehicle_location_data_list200_response import VehicleLocationDataList200Response
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
    api_instance = openapi_client.VehicleLocationDataApi(api_client)
    dispatcher_timestamp__lte = 'dispatcher_timestamp__lte_example' # str | dispatcher_timestamp__lte (optional)
    dispatcher_timestamp__gte = 'dispatcher_timestamp__gte_example' # str | dispatcher_timestamp__gte (optional)
    dispatcher_timestamp__lt = 'dispatcher_timestamp__lt_example' # str | dispatcher_timestamp__lt (optional)
    dispatcher_timestamp__gt = 'dispatcher_timestamp__gt_example' # str | dispatcher_timestamp__gt (optional)
    dispatcher_timestamp = 'dispatcher_timestamp_example' # str | dispatcher_timestamp (optional)
    dispatcher_timestamp__isnull = 'dispatcher_timestamp__isnull_example' # str | dispatcher_timestamp__isnull (optional)
    driver_timestamp__lte = 'driver_timestamp__lte_example' # str | driver_timestamp__lte (optional)
    driver_timestamp__gte = 'driver_timestamp__gte_example' # str | driver_timestamp__gte (optional)
    driver_timestamp__lt = 'driver_timestamp__lt_example' # str | driver_timestamp__lt (optional)
    driver_timestamp__gt = 'driver_timestamp__gt_example' # str | driver_timestamp__gt (optional)
    driver_timestamp = 'driver_timestamp_example' # str | driver_timestamp (optional)
    driver_timestamp__isnull = 'driver_timestamp__isnull_example' # str | driver_timestamp__isnull (optional)
    confirmed_timestamp__lte = 'confirmed_timestamp__lte_example' # str | confirmed_timestamp__lte (optional)
    confirmed_timestamp__gte = 'confirmed_timestamp__gte_example' # str | confirmed_timestamp__gte (optional)
    confirmed_timestamp__lt = 'confirmed_timestamp__lt_example' # str | confirmed_timestamp__lt (optional)
    confirmed_timestamp__gt = 'confirmed_timestamp__gt_example' # str | confirmed_timestamp__gt (optional)
    confirmed_timestamp = 'confirmed_timestamp_example' # str | confirmed_timestamp (optional)
    confirmed_timestamp__isnull = 'confirmed_timestamp__isnull_example' # str | confirmed_timestamp__isnull (optional)
    cancelled_timestamp__lte = 'cancelled_timestamp__lte_example' # str | cancelled_timestamp__lte (optional)
    cancelled_timestamp__gte = 'cancelled_timestamp__gte_example' # str | cancelled_timestamp__gte (optional)
    cancelled_timestamp__lt = 'cancelled_timestamp__lt_example' # str | cancelled_timestamp__lt (optional)
    cancelled_timestamp__gt = 'cancelled_timestamp__gt_example' # str | cancelled_timestamp__gt (optional)
    cancelled_timestamp = 'cancelled_timestamp_example' # str | cancelled_timestamp (optional)
    cancelled_timestamp__isnull = 'cancelled_timestamp__isnull_example' # str | cancelled_timestamp__isnull (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    waybill_number = 'waybill_number_example' # str | Filters available vehicle location data by waybill number. (optional)
    truck_reg_number = 'truck_reg_number_example' # str | Filters available vehicle location data by truck registration number. (optional)
    waybill_status = 56 # int | Filters available vehicle location data by waybill status. (optional)
    destination_id = 56 # int | Filters available vehicle location data by destination ID. (optional)

    try:
        # Querying of vehicle location data
        api_response = api_instance.vehicle_location_data_list(dispatcher_timestamp__lte=dispatcher_timestamp__lte, dispatcher_timestamp__gte=dispatcher_timestamp__gte, dispatcher_timestamp__lt=dispatcher_timestamp__lt, dispatcher_timestamp__gt=dispatcher_timestamp__gt, dispatcher_timestamp=dispatcher_timestamp, dispatcher_timestamp__isnull=dispatcher_timestamp__isnull, driver_timestamp__lte=driver_timestamp__lte, driver_timestamp__gte=driver_timestamp__gte, driver_timestamp__lt=driver_timestamp__lt, driver_timestamp__gt=driver_timestamp__gt, driver_timestamp=driver_timestamp, driver_timestamp__isnull=driver_timestamp__isnull, confirmed_timestamp__lte=confirmed_timestamp__lte, confirmed_timestamp__gte=confirmed_timestamp__gte, confirmed_timestamp__lt=confirmed_timestamp__lt, confirmed_timestamp__gt=confirmed_timestamp__gt, confirmed_timestamp=confirmed_timestamp, confirmed_timestamp__isnull=confirmed_timestamp__isnull, cancelled_timestamp__lte=cancelled_timestamp__lte, cancelled_timestamp__gte=cancelled_timestamp__gte, cancelled_timestamp__lt=cancelled_timestamp__lt, cancelled_timestamp__gt=cancelled_timestamp__gt, cancelled_timestamp=cancelled_timestamp, cancelled_timestamp__isnull=cancelled_timestamp__isnull, limit=limit, offset=offset, waybill_number=waybill_number, truck_reg_number=truck_reg_number, waybill_status=waybill_status, destination_id=destination_id)
        print("The response of VehicleLocationDataApi->vehicle_location_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VehicleLocationDataApi->vehicle_location_data_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispatcher_timestamp__lte** | **str**| dispatcher_timestamp__lte | [optional] 
 **dispatcher_timestamp__gte** | **str**| dispatcher_timestamp__gte | [optional] 
 **dispatcher_timestamp__lt** | **str**| dispatcher_timestamp__lt | [optional] 
 **dispatcher_timestamp__gt** | **str**| dispatcher_timestamp__gt | [optional] 
 **dispatcher_timestamp** | **str**| dispatcher_timestamp | [optional] 
 **dispatcher_timestamp__isnull** | **str**| dispatcher_timestamp__isnull | [optional] 
 **driver_timestamp__lte** | **str**| driver_timestamp__lte | [optional] 
 **driver_timestamp__gte** | **str**| driver_timestamp__gte | [optional] 
 **driver_timestamp__lt** | **str**| driver_timestamp__lt | [optional] 
 **driver_timestamp__gt** | **str**| driver_timestamp__gt | [optional] 
 **driver_timestamp** | **str**| driver_timestamp | [optional] 
 **driver_timestamp__isnull** | **str**| driver_timestamp__isnull | [optional] 
 **confirmed_timestamp__lte** | **str**| confirmed_timestamp__lte | [optional] 
 **confirmed_timestamp__gte** | **str**| confirmed_timestamp__gte | [optional] 
 **confirmed_timestamp__lt** | **str**| confirmed_timestamp__lt | [optional] 
 **confirmed_timestamp__gt** | **str**| confirmed_timestamp__gt | [optional] 
 **confirmed_timestamp** | **str**| confirmed_timestamp | [optional] 
 **confirmed_timestamp__isnull** | **str**| confirmed_timestamp__isnull | [optional] 
 **cancelled_timestamp__lte** | **str**| cancelled_timestamp__lte | [optional] 
 **cancelled_timestamp__gte** | **str**| cancelled_timestamp__gte | [optional] 
 **cancelled_timestamp__lt** | **str**| cancelled_timestamp__lt | [optional] 
 **cancelled_timestamp__gt** | **str**| cancelled_timestamp__gt | [optional] 
 **cancelled_timestamp** | **str**| cancelled_timestamp | [optional] 
 **cancelled_timestamp__isnull** | **str**| cancelled_timestamp__isnull | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **waybill_number** | **str**| Filters available vehicle location data by waybill number. | [optional] 
 **truck_reg_number** | **str**| Filters available vehicle location data by truck registration number. | [optional] 
 **waybill_status** | **int**| Filters available vehicle location data by waybill status. | [optional] 
 **destination_id** | **int**| Filters available vehicle location data by destination ID. | [optional] 

### Return type

[**VehicleLocationDataList200Response**](VehicleLocationDataList200Response.md)

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

