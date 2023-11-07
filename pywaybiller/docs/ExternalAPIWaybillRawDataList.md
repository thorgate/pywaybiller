# ExternalAPIWaybillRawDataList

The IDs of the Waybiller internal objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waybill_id** | **int** | The ID of the waybill. | 
**destination_id** | **int** | The ID of the destination. | 

## Example

```python
from openapi_client.models.external_api_waybill_raw_data_list import ExternalAPIWaybillRawDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillRawDataList from a JSON string
external_api_waybill_raw_data_list_instance = ExternalAPIWaybillRawDataList.from_json(json)
# print the JSON string representation of the object
print ExternalAPIWaybillRawDataList.to_json()

# convert the object into a dict
external_api_waybill_raw_data_list_dict = external_api_waybill_raw_data_list_instance.to_dict()
# create an instance of ExternalAPIWaybillRawDataList from a dict
external_api_waybill_raw_data_list_form_dict = external_api_waybill_raw_data_list.from_dict(external_api_waybill_raw_data_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


