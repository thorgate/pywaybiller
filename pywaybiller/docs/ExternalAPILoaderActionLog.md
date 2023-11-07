# ExternalAPILoaderActionLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_timestamp** | **datetime** |  | [optional] [readonly] 
**log_description** | **str** |  | [optional] [readonly] 
**loader_operator_user_name** | **str** |  | [optional] [readonly] 
**action_name** | **str** |  | [optional] [readonly] 
**origin_name** | **str** |  | [optional] [readonly] 
**order_number** | **str** |  | [optional] [readonly] 
**vehicle_reg_number** | **str** |  | [optional] [readonly] 
**trailer_reg_number** | **str** |  | [optional] [readonly] 
**waybill_number** | **str** |  | [optional] [readonly] 
**loader_unit_name** | **str** |  | [optional] [readonly] 
**assortment_name** | **str** |  | [optional] [readonly] 
**subset_name** | **str** |  | [optional] [readonly] 
**weight** | **str** |  | [optional] [readonly] 
**log_comments** | [**List[ExternalAPILoaderActionLogComment]**](ExternalAPILoaderActionLogComment.md) |  | [optional] [readonly] 
**raw_data** | [**ExternalAPILoaderActionLogRawData**](ExternalAPILoaderActionLogRawData.md) |  | [optional] 

## Example

```python
from openapi_client.models.external_api_loader_action_log import ExternalAPILoaderActionLog

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPILoaderActionLog from a JSON string
external_api_loader_action_log_instance = ExternalAPILoaderActionLog.from_json(json)
# print the JSON string representation of the object
print ExternalAPILoaderActionLog.to_json()

# convert the object into a dict
external_api_loader_action_log_dict = external_api_loader_action_log_instance.to_dict()
# create an instance of ExternalAPILoaderActionLog from a dict
external_api_loader_action_log_form_dict = external_api_loader_action_log.from_dict(external_api_loader_action_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


