# ExternalAPITransportOrderRawDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_order_id** | **int** |  | 
**status** | **str** |  | [optional] [readonly] 
**number** | **str** |  | [optional] [readonly] 
**entity_code** | **str** |  | [optional] [readonly] 
**waybills_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.external_api_transport_order_raw_data_list import ExternalAPITransportOrderRawDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPITransportOrderRawDataList from a JSON string
external_api_transport_order_raw_data_list_instance = ExternalAPITransportOrderRawDataList.from_json(json)
# print the JSON string representation of the object
print ExternalAPITransportOrderRawDataList.to_json()

# convert the object into a dict
external_api_transport_order_raw_data_list_dict = external_api_transport_order_raw_data_list_instance.to_dict()
# create an instance of ExternalAPITransportOrderRawDataList from a dict
external_api_transport_order_raw_data_list_form_dict = external_api_transport_order_raw_data_list.from_dict(external_api_transport_order_raw_data_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


