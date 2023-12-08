# WaybillsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExternalAPIWaybillList]**](ExternalAPIWaybillList.md) |  | 

## Example

```python
from openapi_client.models.waybills_list200_response import WaybillsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsList200Response from a JSON string
waybills_list200_response_instance = WaybillsList200Response.from_json(json)
# print the JSON string representation of the object
print WaybillsList200Response.to_json()

# convert the object into a dict
waybills_list200_response_dict = waybills_list200_response_instance.to_dict()
# create an instance of WaybillsList200Response from a dict
waybills_list200_response_form_dict = waybills_list200_response.from_dict(waybills_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


