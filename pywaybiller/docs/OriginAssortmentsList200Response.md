# OriginAssortmentsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExternalAPIOriginAssortment]**](ExternalAPIOriginAssortment.md) |  | 

## Example

```python
from openapi_client.models.origin_assortments_list200_response import OriginAssortmentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OriginAssortmentsList200Response from a JSON string
origin_assortments_list200_response_instance = OriginAssortmentsList200Response.from_json(json)
# print the JSON string representation of the object
print OriginAssortmentsList200Response.to_json()

# convert the object into a dict
origin_assortments_list200_response_dict = origin_assortments_list200_response_instance.to_dict()
# create an instance of OriginAssortmentsList200Response from a dict
origin_assortments_list200_response_form_dict = origin_assortments_list200_response.from_dict(origin_assortments_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


