# ExternalAPITimeEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **int** | ID of the employee owning the time entry | 
**start** | **datetime** | Start time of the time entry | 
**end** | **datetime** | End time of the time entry | 
**description** | **str** | Description of the time entry | 
**location** | [**ExternalAPITimeEntryLocationRequest**](ExternalAPITimeEntryLocationRequest.md) | Location information (&#x60;Origin&#x60; or &#x60;Destination&#x60;) | [optional] 
**vehicle** | [**ExternalAPITimeEntryVehicleRequest**](ExternalAPITimeEntryVehicleRequest.md) | Vehicle information | [optional] 

## Example

```python
from openapi_client.models.external_api_time_entry_request import ExternalAPITimeEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPITimeEntryRequest from a JSON string
external_api_time_entry_request_instance = ExternalAPITimeEntryRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalAPITimeEntryRequest.to_json())

# convert the object into a dict
external_api_time_entry_request_dict = external_api_time_entry_request_instance.to_dict()
# create an instance of ExternalAPITimeEntryRequest from a dict
external_api_time_entry_request_from_dict = ExternalAPITimeEntryRequest.from_dict(external_api_time_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


