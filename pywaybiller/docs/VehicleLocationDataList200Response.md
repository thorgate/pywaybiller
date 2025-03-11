# VehicleLocationDataList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExternalAPIVehicleLocationData]**](ExternalAPIVehicleLocationData.md) |  | 

## Example

```python
from openapi_client.models.vehicle_location_data_list200_response import VehicleLocationDataList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleLocationDataList200Response from a JSON string
vehicle_location_data_list200_response_instance = VehicleLocationDataList200Response.from_json(json)
# print the JSON string representation of the object
print VehicleLocationDataList200Response.to_json()

# convert the object into a dict
vehicle_location_data_list200_response_dict = vehicle_location_data_list200_response_instance.to_dict()
# create an instance of VehicleLocationDataList200Response from a dict
vehicle_location_data_list200_response_form_dict = vehicle_location_data_list200_response.from_dict(vehicle_location_data_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


