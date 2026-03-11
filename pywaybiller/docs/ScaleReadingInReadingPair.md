# ScaleReadingInReadingPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**value** | **decimal.Decimal** |  | [optional] 
**measurement_timestamp** | **datetime** |  | [optional] 
**source** | [**ScaleReadingInReadingPairSource**](ScaleReadingInReadingPairSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.scale_reading_in_reading_pair import ScaleReadingInReadingPair

# TODO update the JSON string below
json = "{}"
# create an instance of ScaleReadingInReadingPair from a JSON string
scale_reading_in_reading_pair_instance = ScaleReadingInReadingPair.from_json(json)
# print the JSON string representation of the object
print(ScaleReadingInReadingPair.to_json())

# convert the object into a dict
scale_reading_in_reading_pair_dict = scale_reading_in_reading_pair_instance.to_dict()
# create an instance of ScaleReadingInReadingPair from a dict
scale_reading_in_reading_pair_from_dict = ScaleReadingInReadingPair.from_dict(scale_reading_in_reading_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


