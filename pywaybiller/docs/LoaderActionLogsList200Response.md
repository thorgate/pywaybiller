# LoaderActionLogsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExternalAPILoaderActionLog]**](ExternalAPILoaderActionLog.md) |  | 

## Example

```python
from openapi_client.models.loader_action_logs_list200_response import LoaderActionLogsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LoaderActionLogsList200Response from a JSON string
loader_action_logs_list200_response_instance = LoaderActionLogsList200Response.from_json(json)
# print the JSON string representation of the object
print LoaderActionLogsList200Response.to_json()

# convert the object into a dict
loader_action_logs_list200_response_dict = loader_action_logs_list200_response_instance.to_dict()
# create an instance of LoaderActionLogsList200Response from a dict
loader_action_logs_list200_response_form_dict = loader_action_logs_list200_response.from_dict(loader_action_logs_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


