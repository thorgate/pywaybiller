# ExternalAPIWaybillRowList

Waybill rows.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assortment_id** | **str** | The ID of the assortment. | [optional] [readonly] 
**assortment_ids** | **List[str]** | The IDs of the assortments. | [optional] [readonly] 
**assortment_name** | **str** | The name of the assortment. | [optional] [readonly] 

## Example

```python
from openapi_client.models.external_api_waybill_row_list import ExternalAPIWaybillRowList

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillRowList from a JSON string
external_api_waybill_row_list_instance = ExternalAPIWaybillRowList.from_json(json)
# print the JSON string representation of the object
print ExternalAPIWaybillRowList.to_json()

# convert the object into a dict
external_api_waybill_row_list_dict = external_api_waybill_row_list_instance.to_dict()
# create an instance of ExternalAPIWaybillRowList from a dict
external_api_waybill_row_list_form_dict = external_api_waybill_row_list.from_dict(external_api_waybill_row_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


