# OriginsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ExtAPIOriginList]**](ExtAPIOriginList.md) |  | 

## Example

```python
from openapi_client.models.origins_list200_response import OriginsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OriginsList200Response from a JSON string
origins_list200_response_instance = OriginsList200Response.from_json(json)
# print the JSON string representation of the object
print OriginsList200Response.to_json()

# convert the object into a dict
origins_list200_response_dict = origins_list200_response_instance.to_dict()
# create an instance of OriginsList200Response from a dict
origins_list200_response_form_dict = origins_list200_response.from_dict(origins_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


