# ExternalAPIVehicle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**reg_number** | **str** |  | 
**trailer_reg_number** | **str** |  | 
**inactive** | **bool** | Mitteaktiivseid sõidukeid ei saa kasutada | [optional] [readonly] 
**company_name** | **str** |  | 
**company_reg_code** | **str** |  | 

## Example

```python
from openapi_client.models.external_api_vehicle import ExternalAPIVehicle

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIVehicle from a JSON string
external_api_vehicle_instance = ExternalAPIVehicle.from_json(json)
# print the JSON string representation of the object
print ExternalAPIVehicle.to_json()

# convert the object into a dict
external_api_vehicle_dict = external_api_vehicle_instance.to_dict()
# create an instance of ExternalAPIVehicle from a dict
external_api_vehicle_form_dict = external_api_vehicle.from_dict(external_api_vehicle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


