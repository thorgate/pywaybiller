# TransportOrdersList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExternalAPITransportOrderList]**](ExternalAPITransportOrderList.md) |  | 

## Example

```python
from openapi_client.models.transport_orders_list200_response import TransportOrdersList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrdersList200Response from a JSON string
transport_orders_list200_response_instance = TransportOrdersList200Response.from_json(json)
# print the JSON string representation of the object
print TransportOrdersList200Response.to_json()

# convert the object into a dict
transport_orders_list200_response_dict = transport_orders_list200_response_instance.to_dict()
# create an instance of TransportOrdersList200Response from a dict
transport_orders_list200_response_form_dict = transport_orders_list200_response.from_dict(transport_orders_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


