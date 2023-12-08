# ExternalAPIWaybillList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waybill_id** | **str** | The external ID of the waybill. Usually &#x60;null&#x60; if waybill was created in Waybiller UI and not over Waybiller External API. | [optional] [readonly] 
**destination_id** | **str** | The external ID of the destination. Usually &#x60;null&#x60; if waybill was created in Waybiller UI and not over Waybiller External API. | [optional] [readonly] 
**dispatcher_timestamp** | **datetime** | Veoselehe loomise aeg | [optional] [readonly] 
**driver_timestamp** | **datetime** | Hetk millal autojuht alustas sõitu | [optional] [readonly] 
**destination_timestamp** | **datetime** |  | [optional] [readonly] 
**confirmed_timestamp** | **datetime** | Sihtkohas kinnitamise aeg | [optional] [readonly] 
**cancelled_timestamp** | **datetime** | Veoselehe tühistamise aeg | [optional] [readonly] 
**status** | **int** |  | [optional] [readonly] 
**number** | **str** |  | [optional] [readonly] 
**navision_bin_code** | **str** | Bin code. | [optional] [readonly] 
**raw_data** | [**ExternalAPIWaybillRawDataList**](ExternalAPIWaybillRawDataList.md) |  | [optional] 
**shipper_company_name** | **str** | The name of the shipper company. | [optional] [readonly] 
**origin_name** | **str** |  | [optional] [readonly] 
**origin_address** | **str** |  | [optional] [readonly] 
**transportation_company_name** | **str** | The name of the transportation company. | [optional] [readonly] 
**truck_reg_number** | **str** | The registration number of the vehicle. | [optional] [readonly] 
**trailer_reg_number** | **str** | The registration number of the trailer. | [optional] [readonly] 
**receiver_company_name** | **str** | The name of the receiving company. | [optional] [readonly] 
**receiver_company_reg_code** | **str** | The registry code of the receiving company. | [optional] [readonly] 
**last_vehicle_location** | **object** |  | [optional] [readonly] 
**destination_name** | **str** | The name of the destination. | [optional] [readonly] 
**destination_address** | **str** | The address of the destination. | [optional] [readonly] 
**dispatched_amount** | **decimal.Decimal** | The total dispatched amount. | [optional] [readonly] 
**rows** | [**List[ExternalAPIWaybillRowList]**](ExternalAPIWaybillRowList.md) | Waybill rows. | [optional] [readonly] 

## Example

```python
from openapi_client.models.external_api_waybill_list import ExternalAPIWaybillList

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillList from a JSON string
external_api_waybill_list_instance = ExternalAPIWaybillList.from_json(json)
# print the JSON string representation of the object
print ExternalAPIWaybillList.to_json()

# convert the object into a dict
external_api_waybill_list_dict = external_api_waybill_list_instance.to_dict()
# create an instance of ExternalAPIWaybillList from a dict
external_api_waybill_list_form_dict = external_api_waybill_list.from_dict(external_api_waybill_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


