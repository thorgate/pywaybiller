# ExternalAPIOriginAssortmentRaw

Raw values (ID-s) in Waybiller.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Origin assortment ID. | 
**origin_id** | **int** | Origin ID. | 
**assortment_id** | **int** | Assortment ID. | 
**subset_type_id** | **int** | Subset type ID. | 
**subset_id** | **int** | Subset ID. | 

## Example

```python
from openapi_client.models.external_api_origin_assortment_raw import ExternalAPIOriginAssortmentRaw

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIOriginAssortmentRaw from a JSON string
external_api_origin_assortment_raw_instance = ExternalAPIOriginAssortmentRaw.from_json(json)
# print the JSON string representation of the object
print ExternalAPIOriginAssortmentRaw.to_json()

# convert the object into a dict
external_api_origin_assortment_raw_dict = external_api_origin_assortment_raw_instance.to_dict()
# create an instance of ExternalAPIOriginAssortmentRaw from a dict
external_api_origin_assortment_raw_form_dict = external_api_origin_assortment_raw.from_dict(external_api_origin_assortment_raw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


