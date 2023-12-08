# ExternalAPIWaybillRow

Waybill rows.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assortment_id** | **str** | The external ID of the assortment. Usually &#x60;null&#x60; if waybill was created in Waybiller UI and not over Waybiller External API. | [optional] 
**assortment_ids** | **List[str]** | The external IDs of the assortment. Usually &#x60;null&#x60; if waybill was created in Waybiller UI and not over Waybiller External API. | [optional] [readonly] 
**assortment_raw_id** | **int** | The ID of the assortment. | [optional] 
**assortment_name** | **str** | The name of the assortment. | [optional] 
**dispatched_amount** | **decimal.Decimal** | Saadetud materjali kogus | [optional] 
**accepted_amount** | **decimal.Decimal** |  | [optional] [readonly] 
**subset_type_name** | **str** | Subset type (eg fraction). | [optional] [readonly] 
**subset_object_raw_id** | **int** | The ID of the subset of the assortment. | [optional] 
**subset_object_name** | **str** | Subset object (eg 0-32mm). | [optional] [readonly] 
**extra_information_long** | **str** |  | [optional] 
**extra_information_short** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.external_api_waybill_row import ExternalAPIWaybillRow

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillRow from a JSON string
external_api_waybill_row_instance = ExternalAPIWaybillRow.from_json(json)
# print the JSON string representation of the object
print ExternalAPIWaybillRow.to_json()

# convert the object into a dict
external_api_waybill_row_dict = external_api_waybill_row_instance.to_dict()
# create an instance of ExternalAPIWaybillRow from a dict
external_api_waybill_row_form_dict = external_api_waybill_row.from_dict(external_api_waybill_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


