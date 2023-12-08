# ExternalAPIVehicleLocationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**truck_reg_number** | **str** | The registration number of the vehicle. | [optional] [readonly] 
**waybill_number** | **str** | The waybill number. | [optional] [readonly] 
**transportation_company_name** | **str** | The name of the transportation company. | [optional] [readonly] 
**receiver_company_name** | **str** | The name of the receiving company. | [optional] [readonly] 
**origin_company_name** | **str** | The name of the origin company. | [optional] [readonly] 
**origin_name** | **str** |  | 
**destination_name** | **str** | The name of the destination. | [optional] [readonly] 
**raw_data** | [**ExternalAPIVehicleLocationDataRawData**](ExternalAPIVehicleLocationDataRawData.md) |  | [optional] 
**vehicle_location_data** | **str** | The vehicle location data. | [optional] [readonly] 

## Example

```python
from openapi_client.models.external_api_vehicle_location_data import ExternalAPIVehicleLocationData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIVehicleLocationData from a JSON string
external_api_vehicle_location_data_instance = ExternalAPIVehicleLocationData.from_json(json)
# print the JSON string representation of the object
print ExternalAPIVehicleLocationData.to_json()

# convert the object into a dict
external_api_vehicle_location_data_dict = external_api_vehicle_location_data_instance.to_dict()
# create an instance of ExternalAPIVehicleLocationData from a dict
external_api_vehicle_location_data_form_dict = external_api_vehicle_location_data.from_dict(external_api_vehicle_location_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


