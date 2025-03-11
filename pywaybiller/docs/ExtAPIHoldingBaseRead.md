# ExtAPIHoldingBaseRead

Holding base data is provided as is, in internal WB format. It may change at any time without warning and may have a different schema for old and new origins

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**contract_number** | **str** |  | [optional] 
**contract_date** | **str** |  | [optional] 
**previous_owner** | [**ExtAPIHoldingBasePreviousOwner**](ExtAPIHoldingBasePreviousOwner.md) |  | [optional] 

## Example

```python
from openapi_client.models.ext_api_holding_base_read import ExtAPIHoldingBaseRead

# TODO update the JSON string below
json = "{}"
# create an instance of ExtAPIHoldingBaseRead from a JSON string
ext_api_holding_base_read_instance = ExtAPIHoldingBaseRead.from_json(json)
# print the JSON string representation of the object
print ExtAPIHoldingBaseRead.to_json()

# convert the object into a dict
ext_api_holding_base_read_dict = ext_api_holding_base_read_instance.to_dict()
# create an instance of ExtAPIHoldingBaseRead from a dict
ext_api_holding_base_read_form_dict = ext_api_holding_base_read.from_dict(ext_api_holding_base_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


