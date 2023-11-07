# ExtAPIOriginRead


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**location** | [**GeoLocation**](GeoLocation.md) |  | 
**assortments** | [**List[ExtAPIOriginAssortment]**](ExtAPIOriginAssortment.md) |  | 
**partner_companies** | **List[str]** | List of registry codes of partner companies. | [optional] 
**public** | **bool** |  | [optional] [default to False]
**active** | **bool** |  | [optional] [default to True]
**holding_base** | [**ExtAPIHoldingBaseRead**](ExtAPIHoldingBaseRead.md) |  | [optional] 
**cadaster_number** | **str** | Cadaster number of the Origin in free form. Required if holding base is sent. | [optional] 
**extra_information** | **str** |  | [optional] 
**representative_name** | **str** |  | [optional] 
**representative_phone** | **str** |  | [optional] 
**waybill_created_emails** | **List[str]** | E-mail addresses, where you want to receive notification when waybill is created. | [optional] 
**waybill_accepted_emails** | **List[str]** | E-mail addresses, where you want to receive notification when waybill is accepted. | [optional] 
**waybill_reached_destination_emails** | **List[str]** | E-mail addresses, where you want to receive notification when waybill has arrived at destination. | [optional] 
**waybill_created_emails_language** | **str** |  | [optional] [default to '']
**waybill_accepted_emails_language** | **str** |  | [optional] [default to '']
**waybill_reached_destination_emails_language** | **str** |  | [optional] [default to '']
**feature_single_transport_order_per_truck** | **bool** | Managers are not allowed to create transport orders for a vehicle if there is an active transport order for the vehicle from this origin | [optional] [default to False]
**feature_waybill_dispatched_amounts_changing_disabled** | **bool** | Drivers and receivers are not allowed to change dispatched amounts for waybills from this origin | [optional] [default to False]
**feature_waybill_destination_changing_disabled_for_drivers** | **bool** | Drivers are not allowed to change the destination of waybills from this origin | [optional] [default to False]
**company** | **str** | Registry code of the owner company. By default, API KEY company is used. Note, origin company can not be changed | [optional] 

## Example

```python
from openapi_client.models.ext_api_origin_read import ExtAPIOriginRead

# TODO update the JSON string below
json = "{}"
# create an instance of ExtAPIOriginRead from a JSON string
ext_api_origin_read_instance = ExtAPIOriginRead.from_json(json)
# print the JSON string representation of the object
print ExtAPIOriginRead.to_json()

# convert the object into a dict
ext_api_origin_read_dict = ext_api_origin_read_instance.to_dict()
# create an instance of ExtAPIOriginRead from a dict
ext_api_origin_read_form_dict = ext_api_origin_read.from_dict(ext_api_origin_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


