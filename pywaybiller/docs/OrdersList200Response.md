# OrdersList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExternalAPIOrderList]**](ExternalAPIOrderList.md) |  | 

## Example

```python
from openapi_client.models.orders_list200_response import OrdersList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersList200Response from a JSON string
orders_list200_response_instance = OrdersList200Response.from_json(json)
# print the JSON string representation of the object
print OrdersList200Response.to_json()

# convert the object into a dict
orders_list200_response_dict = orders_list200_response_instance.to_dict()
# create an instance of OrdersList200Response from a dict
orders_list200_response_form_dict = orders_list200_response.from_dict(orders_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


