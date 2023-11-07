# ExternalAPIVehicleLocationDataRawData

The IDs of the Waybiller internal objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waybill_id** | **int** | The ID of the waybill. | 
**destination_id** | **int** | The ID of the destination. | 
**origin_id** | **int** | The ID of the origin. | 
**truck_id** | **int** | The ID of the truck. | 

## Example

```python
from openapi_client.models.external_api_vehicle_location_data_raw_data import ExternalAPIVehicleLocationDataRawData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIVehicleLocationDataRawData from a JSON string
external_api_vehicle_location_data_raw_data_instance = ExternalAPIVehicleLocationDataRawData.from_json(json)
# print the JSON string representation of the object
print ExternalAPIVehicleLocationDataRawData.to_json()

# convert the object into a dict
external_api_vehicle_location_data_raw_data_dict = external_api_vehicle_location_data_raw_data_instance.to_dict()
# create an instance of ExternalAPIVehicleLocationDataRawData from a dict
external_api_vehicle_location_data_raw_data_form_dict = external_api_vehicle_location_data_raw_data.from_dict(external_api_vehicle_location_data_raw_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


