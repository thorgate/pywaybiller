# ExternalAPIOrderRawData

Raw values in Waybiller.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order raw id. | 
**number** | **str** | Order number. | 
**status** | **int** | The number representing the status of the order. 1 - Mustand, 2 - Aktiivne, 3 - Mitteaktiivne, 4 - Arhiveeritud | 
**origins** | **List[int]** | Lähtekohad, mille jaoks see tellimus loodud on. | [optional] [readonly] 
**owner_company_id** | **str** | Owner company raw id. | 
**client_id** | **str** | Client company raw id. | 
**origins_assortment** | **List[int]** | The assortment that can be grabbed by an order&#39;s executor. | [optional] [readonly] 
**transportation_companies** | **List[int]** | Veofirmad, mida tellimuse klient kasutab vedude jaoks lähtekohtadest sihtkohta. | [optional] [readonly] 
**vehicles** | **List[int]** | Veokid, kes võivad selle tellimuse alusel vedusid teostada. | [optional] [readonly] 
**destination** | **int** | Sihtkoht, kuhu selle tellimuse alusel on võimalik vedusid teostada. | [optional] [readonly] 

## Example

```python
from openapi_client.models.external_api_order_raw_data import ExternalAPIOrderRawData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAPIOrderRawData from a JSON string
external_api_order_raw_data_instance = ExternalAPIOrderRawData.from_json(json)
# print the JSON string representation of the object
print ExternalAPIOrderRawData.to_json()

# convert the object into a dict
external_api_order_raw_data_dict = external_api_order_raw_data_instance.to_dict()
# create an instance of ExternalAPIOrderRawData from a dict
external_api_order_raw_data_form_dict = external_api_order_raw_data.from_dict(external_api_order_raw_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


