# ExternalAPILoaderActionLogRawData

The IDs of the Waybiller internal objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **int** | The ID of the log. | 
**loader_operator_user_id** | **int** | The ID of the loader operator user. | 
**origin_id** | **int** | The ID of the origin. | 
**order_id** | **int** | The ID of the order. | 
**vehicle_id** | **int** | The ID of the vehicle. | 
**loader_unit_id** | **int** | The ID of the loader unit. | 
**assortment_id** | **int** | The ID of the assortment. | 
**subset_id** | **int** | The ID of the subset. | 

## Example

```python
from openapi_client.models.external_api_loader_action_log_raw_data import ExternalAPILoaderActionLogRawData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPILoaderActionLogRawData from a JSON string
external_api_loader_action_log_raw_data_instance = ExternalAPILoaderActionLogRawData.from_json(json)
# print the JSON string representation of the object
print ExternalAPILoaderActionLogRawData.to_json()

# convert the object into a dict
external_api_loader_action_log_raw_data_dict = external_api_loader_action_log_raw_data_instance.to_dict()
# create an instance of ExternalAPILoaderActionLogRawData from a dict
external_api_loader_action_log_raw_data_form_dict = external_api_loader_action_log_raw_data.from_dict(external_api_loader_action_log_raw_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


