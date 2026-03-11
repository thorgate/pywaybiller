# ExternalAPITransportOrderRowRetrieve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assortment_id** | **str** | Unique identifier of the assortment in your system | [readonly] 
**assortment_name** | **str** | Name of the assortment | [readonly] 
**destination_id** | **str** | Unique identifier of the destination in your system or Waybiller | [readonly] 
**destination_name** | **str** | Name of the destination | [readonly] 
**destination_address** | **str** | Address of the destination | [readonly] 
**destination_latitude** | **float** | Latitude of the destination location | [readonly] 
**destination_longitude** | **float** | Longitude of the destination location | [readonly] 
**amount** | **decimal.Decimal** | Amount of the assortment | [readonly] 

## Example

```python
from openapi_client.models.external_api_transport_order_row_retrieve import ExternalAPITransportOrderRowRetrieve

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPITransportOrderRowRetrieve from a JSON string
external_api_transport_order_row_retrieve_instance = ExternalAPITransportOrderRowRetrieve.from_json(json)
# print the JSON string representation of the object
print(ExternalAPITransportOrderRowRetrieve.to_json())

# convert the object into a dict
external_api_transport_order_row_retrieve_dict = external_api_transport_order_row_retrieve_instance.to_dict()
# create an instance of ExternalAPITransportOrderRowRetrieve from a dict
external_api_transport_order_row_retrieve_from_dict = ExternalAPITransportOrderRowRetrieve.from_dict(external_api_transport_order_row_retrieve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


