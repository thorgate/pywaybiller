# ExternalAPITimeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the time entry | [readonly] 
**owner** | **int** | ID of the employee owning the time entry | 
**start** | **datetime** | Start time of the time entry | 
**end** | **datetime** | End time of the time entry | 
**description** | **str** | Description of the time entry | 
**location** | [**ExternalAPITimeEntryLocation**](ExternalAPITimeEntryLocation.md) | Location information (&#x60;Origin&#x60; or &#x60;Destination&#x60;) | [optional] 
**vehicle** | [**ExternalAPITimeEntryVehicle**](ExternalAPITimeEntryVehicle.md) | Vehicle information | [optional] 
**confirmed** | **bool** | Whether the time entry has been confirmed | [readonly] 
**confirmed_by** | **int** | ID of the user who confirmed the time entry | [readonly] 
**confirmed_by_name** | **str** | Full name of the user who confirmed the time entry | [readonly] 

## Example

```python
from openapi_client.models.external_api_time_entry import ExternalAPITimeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPITimeEntry from a JSON string
external_api_time_entry_instance = ExternalAPITimeEntry.from_json(json)
# print the JSON string representation of the object
print(ExternalAPITimeEntry.to_json())

# convert the object into a dict
external_api_time_entry_dict = external_api_time_entry_instance.to_dict()
# create an instance of ExternalAPITimeEntry from a dict
external_api_time_entry_from_dict = ExternalAPITimeEntry.from_dict(external_api_time_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


