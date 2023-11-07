# ExternalAPIWaybillRawData

The IDs of the Waybiller internal objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waybill_id** | **int** | The ID of the waybill. | [optional] [readonly] 
**truck_id** | **int** | The ID of the truck. | [optional] [readonly] 
**driver_user_id** | **int** | The ID of the driver. | [optional] [readonly] 
**origin_id** | **int** |  | [optional] [readonly] 
**destination_id** | **int** | The ID of the destination. | [optional] [readonly] 
**rows** | [**List[ExternalAPIWaybillRowRawData]**](ExternalAPIWaybillRowRawData.md) | Waybill rows. | [optional] [readonly] 
**user_defined_fields** | **object** | User defined fields. | [optional] [readonly] 

## Example

```python
from openapi_client.models.external_api_waybill_raw_data import ExternalAPIWaybillRawData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillRawData from a JSON string
external_api_waybill_raw_data_instance = ExternalAPIWaybillRawData.from_json(json)
# print the JSON string representation of the object
print ExternalAPIWaybillRawData.to_json()

# convert the object into a dict
external_api_waybill_raw_data_dict = external_api_waybill_raw_data_instance.to_dict()
# create an instance of ExternalAPIWaybillRawData from a dict
external_api_waybill_raw_data_form_dict = external_api_waybill_raw_data.from_dict(external_api_waybill_raw_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


