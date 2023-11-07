# VehiclesList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExternalAPIVehicle]**](ExternalAPIVehicle.md) |  | 

## Example

```python
from openapi_client.models.vehicles_list200_response import VehiclesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VehiclesList200Response from a JSON string
vehicles_list200_response_instance = VehiclesList200Response.from_json(json)
# print the JSON string representation of the object
print VehiclesList200Response.to_json()

# convert the object into a dict
vehicles_list200_response_dict = vehicles_list200_response_instance.to_dict()
# create an instance of VehiclesList200Response from a dict
vehicles_list200_response_form_dict = vehicles_list200_response.from_dict(vehicles_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


