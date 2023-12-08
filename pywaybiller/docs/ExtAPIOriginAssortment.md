# ExtAPIOriginAssortment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Assortment ID | 
**subsets** | **List[int]** | List of subset IDs | [optional] 

## Example

```python
from openapi_client.models.ext_api_origin_assortment import ExtAPIOriginAssortment

# TODO update the JSON string below
json = "{}"
# create an instance of ExtAPIOriginAssortment from a JSON string
ext_api_origin_assortment_instance = ExtAPIOriginAssortment.from_json(json)
# print the JSON string representation of the object
print ExtAPIOriginAssortment.to_json()

# convert the object into a dict
ext_api_origin_assortment_dict = ext_api_origin_assortment_instance.to_dict()
# create an instance of ExtAPIOriginAssortment from a dict
ext_api_origin_assortment_form_dict = ext_api_origin_assortment.from_dict(ext_api_origin_assortment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


