# ExternalAPIWaybillRefuse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for refusal. | 
**destination_raw_id** | **str** | The ID of the new destination. | [optional] 

## Example

```python
from openapi_client.models.external_api_waybill_refuse import ExternalAPIWaybillRefuse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillRefuse from a JSON string
external_api_waybill_refuse_instance = ExternalAPIWaybillRefuse.from_json(json)
# print the JSON string representation of the object
print ExternalAPIWaybillRefuse.to_json()

# convert the object into a dict
external_api_waybill_refuse_dict = external_api_waybill_refuse_instance.to_dict()
# create an instance of ExternalAPIWaybillRefuse from a dict
external_api_waybill_refuse_form_dict = external_api_waybill_refuse.from_dict(external_api_waybill_refuse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


