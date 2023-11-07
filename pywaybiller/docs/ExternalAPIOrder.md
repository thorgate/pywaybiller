# ExternalAPIOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Order number. | [optional] [readonly] 
**status** | **str** | The status of the order. | [optional] [readonly] 
**order_id** | **str** | Order id (in your system). | 
**order_raw_id** | **str** | Order raw id. | [optional] [readonly] 
**period** | **List[date]** | The date range when the order is active. | 
**owner_raw_id** | **str** | Raw id of the owner company. | [optional] [readonly] 
**owner_company_name** | **str** | Name of the company who owns the order. | [optional] [readonly] 
**client_id** | **str** | The company id (in your system) for whom the order is created for. | [optional] 
**client_company_reg_code** | **str** | The company reg code for whom the order is created for. Used as raw id to match the company, if it exists. | [optional] 
**client_company_name** | **str** | Name of the company for whom the order is created for. | [optional] 
**destination_raw_id** | **str** | Destination raw id. | [optional] 
**destination_id** | **int** | Destination id (in your system). | [optional] 
**destination_name** | **str** | Destination name. | [optional] 
**destination_address** | **str** | Destination address. | [optional] 
**destination_latitude** | **float** | Destination location - latitude. | [optional] 
**destination_longitude** | **float** | Destination location - longitude. | [optional] 
**origins** | [**List[ExternalAPIOrderOrigin]**](ExternalAPIOrderOrigin.md) | The origins for which the order is created for. | [optional] 
**total_allowed_amount** | **decimal.Decimal** | Total allowed amount in tonnes. | [optional] 
**rows** | [**List[ExternalAPIOrderOriginsAssortments]**](ExternalAPIOrderOriginsAssortments.md) | Origin&#39;s assortments. | [optional] 
**transportation_companies** | [**List[ExternalAPIOrderTransportCompanies]**](ExternalAPIOrderTransportCompanies.md) | The transportation companies the client is using for transporting assortments from origins to destination. | [optional] 
**client_can_edit_transportation_values** | **bool** | Client can edit transportation values. | [optional] 
**vehicles** | [**List[ExternalAPIOrderVehicles]**](ExternalAPIOrderVehicles.md) | The vehicles that the transportation companies are allowed to use for this order. | [optional] 
**extra_information** | **str** | Extra information. | [optional] 
**user_id** | **int** | User who created this order. | 
**raw_data** | [**ExternalAPIOrderRawData**](ExternalAPIOrderRawData.md) |  | [optional] 

## Example

```python
from openapi_client.models.external_api_order import ExternalAPIOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIOrder from a JSON string
external_api_order_instance = ExternalAPIOrder.from_json(json)
# print the JSON string representation of the object
print ExternalAPIOrder.to_json()

# convert the object into a dict
external_api_order_dict = external_api_order_instance.to_dict()
# create an instance of ExternalAPIOrder from a dict
external_api_order_form_dict = external_api_order.from_dict(external_api_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


