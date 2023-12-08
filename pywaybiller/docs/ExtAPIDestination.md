# ExtAPIDestination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**address** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**raw_data** | [**ExternalAPIRawSerializer**](ExternalAPIRawSerializer.md) |  | [optional] 
**owner_name** | **str** |  | [optional] [readonly] 
**owner_reg_code** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.ext_api_destination import ExtAPIDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ExtAPIDestination from a JSON string
ext_api_destination_instance = ExtAPIDestination.from_json(json)
# print the JSON string representation of the object
print ExtAPIDestination.to_json()

# convert the object into a dict
ext_api_destination_dict = ext_api_destination_instance.to_dict()
# create an instance of ExtAPIDestination from a dict
ext_api_destination_form_dict = ext_api_destination.from_dict(ext_api_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


