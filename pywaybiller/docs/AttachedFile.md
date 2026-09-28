# AttachedFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**file** | **str** |  | [readonly] 
**display_name** | **str** |  | [readonly] 
**mime_type** | **str** | &lt;a href&#x3D;\&quot;https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types&lt;/a&gt; | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**created_by** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.attached_file import AttachedFile

# TODO update the JSON string below
json = "{}"
# create an instance of AttachedFile from a JSON string
attached_file_instance = AttachedFile.from_json(json)
# print the JSON string representation of the object
print(AttachedFile.to_json())

# convert the object into a dict
attached_file_dict = attached_file_instance.to_dict()
# create an instance of AttachedFile from a dict
attached_file_from_dict = AttachedFile.from_dict(attached_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


