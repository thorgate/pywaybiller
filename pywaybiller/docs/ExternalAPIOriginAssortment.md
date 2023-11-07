# ExternalAPIOriginAssortment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Origin assortment id. | 
**origin** | **str** | Origin name. | [optional] 
**assortment** | **str** | Assortment name. | [optional] 
**subset_type** | **str** | Subset type. | [optional] 
**subset** | **str** | Subset value. | [optional] 
**raw_data** | [**ExternalAPIOriginAssortmentRaw**](ExternalAPIOriginAssortmentRaw.md) |  | 

## Example

```python
from openapi_client.models.external_api_origin_assortment import ExternalAPIOriginAssortment

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIOriginAssortment from a JSON string
external_api_origin_assortment_instance = ExternalAPIOriginAssortment.from_json(json)
# print the JSON string representation of the object
print ExternalAPIOriginAssortment.to_json()

# convert the object into a dict
external_api_origin_assortment_dict = external_api_origin_assortment_instance.to_dict()
# create an instance of ExternalAPIOriginAssortment from a dict
external_api_origin_assortment_form_dict = external_api_origin_assortment.from_dict(external_api_origin_assortment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


