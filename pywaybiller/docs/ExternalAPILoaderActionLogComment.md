# ExternalAPILoaderActionLogComment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_name** | **str** |  | 
**author_company_name** | **str** |  | 
**comment** | **str** |  | 
**created_timestamp** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.external_api_loader_action_log_comment import ExternalAPILoaderActionLogComment

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPILoaderActionLogComment from a JSON string
external_api_loader_action_log_comment_instance = ExternalAPILoaderActionLogComment.from_json(json)
# print the JSON string representation of the object
print ExternalAPILoaderActionLogComment.to_json()

# convert the object into a dict
external_api_loader_action_log_comment_dict = external_api_loader_action_log_comment_instance.to_dict()
# create an instance of ExternalAPILoaderActionLogComment from a dict
external_api_loader_action_log_comment_form_dict = external_api_loader_action_log_comment.from_dict(external_api_loader_action_log_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


