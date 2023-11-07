# ExtAPIOriginList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**address** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**raw_data** | [**ExternalAPIRawSerializer**](ExternalAPIRawSerializer.md) |  | [optional] 

## Example

```python
from openapi_client.models.ext_api_origin_list import ExtAPIOriginList

# TODO update the JSON string below
json = "{}"
# create an instance of ExtAPIOriginList from a JSON string
ext_api_origin_list_instance = ExtAPIOriginList.from_json(json)
# print the JSON string representation of the object
print ExtAPIOriginList.to_json()

# convert the object into a dict
ext_api_origin_list_dict = ext_api_origin_list_instance.to_dict()
# create an instance of ExtAPIOriginList from a dict
ext_api_origin_list_form_dict = ext_api_origin_list.from_dict(ext_api_origin_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


