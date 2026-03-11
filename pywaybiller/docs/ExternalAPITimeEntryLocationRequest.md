# ExternalAPITimeEntryLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the location (&#x60;Origin&#x60; or &#x60;Destination&#x60;) | 
**type** | [**ExternalAPITimeEntryLocationTypeEnum**](ExternalAPITimeEntryLocationTypeEnum.md) | Type of the location | 

## Example

```python
from openapi_client.models.external_api_time_entry_location_request import ExternalAPITimeEntryLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPITimeEntryLocationRequest from a JSON string
external_api_time_entry_location_request_instance = ExternalAPITimeEntryLocationRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalAPITimeEntryLocationRequest.to_json())

# convert the object into a dict
external_api_time_entry_location_request_dict = external_api_time_entry_location_request_instance.to_dict()
# create an instance of ExternalAPITimeEntryLocationRequest from a dict
external_api_time_entry_location_request_from_dict = ExternalAPITimeEntryLocationRequest.from_dict(external_api_time_entry_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


