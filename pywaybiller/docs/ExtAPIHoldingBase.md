# ExtAPIHoldingBase

Holding base data is provided as is, in internal WB format. It may change at any time without warning and may have a different schema for old and new origins

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**contract_number** | **str** |  | [optional] 
**contract_date** | **str** |  | [optional] 
**previous_owner** | [**ExtAPIHoldingBasePreviousOwner**](ExtAPIHoldingBasePreviousOwner.md) |  | [optional] 

## Example

```python
from openapi_client.models.ext_api_holding_base import ExtAPIHoldingBase

# TODO update the JSON string below
json = "{}"
# create an instance of ExtAPIHoldingBase from a JSON string
ext_api_holding_base_instance = ExtAPIHoldingBase.from_json(json)
# print the JSON string representation of the object
print ExtAPIHoldingBase.to_json()

# convert the object into a dict
ext_api_holding_base_dict = ext_api_holding_base_instance.to_dict()
# create an instance of ExtAPIHoldingBase from a dict
ext_api_holding_base_form_dict = ext_api_holding_base.from_dict(ext_api_holding_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


