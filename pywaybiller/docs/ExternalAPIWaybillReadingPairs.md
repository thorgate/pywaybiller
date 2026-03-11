# ExternalAPIWaybillReadingPairs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the reading pair. | [readonly] 
**weighing_flow** | [**WeighingFlowEnum**](WeighingFlowEnum.md) |  | [readonly] 
**tare_reading** | [**ScaleReadingInReadingPair**](ScaleReadingInReadingPair.md) | Information about the tare reading. | [readonly] 
**gross_reading** | [**ScaleReadingInReadingPair**](ScaleReadingInReadingPair.md) | Information about the gross reading. | [readonly] 

## Example

```python
from openapi_client.models.external_api_waybill_reading_pairs import ExternalAPIWaybillReadingPairs

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillReadingPairs from a JSON string
external_api_waybill_reading_pairs_instance = ExternalAPIWaybillReadingPairs.from_json(json)
# print the JSON string representation of the object
print(ExternalAPIWaybillReadingPairs.to_json())

# convert the object into a dict
external_api_waybill_reading_pairs_dict = external_api_waybill_reading_pairs_instance.to_dict()
# create an instance of ExternalAPIWaybillReadingPairs from a dict
external_api_waybill_reading_pairs_from_dict = ExternalAPIWaybillReadingPairs.from_dict(external_api_waybill_reading_pairs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


