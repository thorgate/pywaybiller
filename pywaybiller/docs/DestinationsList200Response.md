# DestinationsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExtAPIDestination]**](ExtAPIDestination.md) |  | 

## Example

```python
from openapi_client.models.destinations_list200_response import DestinationsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationsList200Response from a JSON string
destinations_list200_response_instance = DestinationsList200Response.from_json(json)
# print the JSON string representation of the object
print DestinationsList200Response.to_json()

# convert the object into a dict
destinations_list200_response_dict = destinations_list200_response_instance.to_dict()
# create an instance of DestinationsList200Response from a dict
destinations_list200_response_form_dict = destinations_list200_response.from_dict(destinations_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


