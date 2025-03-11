# ExternalAPIWaybillComment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_by_user_id** | **int** | The ID of the user that adds the comment to the waybill. Use GET Employments endpoint to query all available employments and get necessary &#x60;user_id&#x60; values. | 
**comment** | **str** | Text of the comment. | 

## Example

```python
from openapi_client.models.external_api_waybill_comment import ExternalAPIWaybillComment

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIWaybillComment from a JSON string
external_api_waybill_comment_instance = ExternalAPIWaybillComment.from_json(json)
# print the JSON string representation of the object
print ExternalAPIWaybillComment.to_json()

# convert the object into a dict
external_api_waybill_comment_dict = external_api_waybill_comment_instance.to_dict()
# create an instance of ExternalAPIWaybillComment from a dict
external_api_waybill_comment_form_dict = external_api_waybill_comment.from_dict(external_api_waybill_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


