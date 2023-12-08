# ExternalAPIEmployment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**email** | **str** |  | 
**user_id** | **str** |  | 
**role** | **str** |  | [optional] [readonly] 
**obsolete** | **bool** |  | [optional] [readonly] 
**company_name** | **str** |  | 
**company_reg_code** | **str** |  | 
**subcontractor_company_name** | **str** |  | 
**subcontractor_company_reg_code** | **str** |  | 

## Example

```python
from openapi_client.models.external_api_employment import ExternalAPIEmployment

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIEmployment from a JSON string
external_api_employment_instance = ExternalAPIEmployment.from_json(json)
# print the JSON string representation of the object
print ExternalAPIEmployment.to_json()

# convert the object into a dict
external_api_employment_dict = external_api_employment_instance.to_dict()
# create an instance of ExternalAPIEmployment from a dict
external_api_employment_form_dict = external_api_employment.from_dict(external_api_employment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


