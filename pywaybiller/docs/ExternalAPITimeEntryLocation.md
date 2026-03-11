# ExternalAPITimeEntryLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the location (&#x60;Origin&#x60; or &#x60;Destination&#x60;) | 
**type** | [**ExternalAPITimeEntryLocationTypeEnum**](ExternalAPITimeEntryLocationTypeEnum.md) | Type of the location | 
**name** | **str** | Name of the location | [readonly] 
**company_name** | **str** | Name of the company owning the location | [readonly] 

## Example

```python
from openapi_client.models.external_api_time_entry_location import ExternalAPITimeEntryLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPITimeEntryLocation from a JSON string
external_api_time_entry_location_instance = ExternalAPITimeEntryLocation.from_json(json)
# print the JSON string representation of the object
print(ExternalAPITimeEntryLocation.to_json())

# convert the object into a dict
external_api_time_entry_location_dict = external_api_time_entry_location_instance.to_dict()
# create an instance of ExternalAPITimeEntryLocation from a dict
external_api_time_entry_location_from_dict = ExternalAPITimeEntryLocation.from_dict(external_api_time_entry_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


