# PyWaybiller

## Installation

```shell
poetry add pywaybiller
```

## Usage

### Get all waybills

```python
import pywaybiller
import datetime

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=7)


client = pywaybiller.WaybillerClient(
    api_key="xxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    host="https://app.staging.waybiller.com/external-api",
)

for waybill in client.waybills.all(
    dispatcher_timestamp__gt=start_date.strftime("%Y-%m-%dT%H:%M:%S"),
    dispatcher_timestamp__lt=end_date.strftime("%Y-%m-%dT%H:%M:%S"),
):
    print(waybill)
```

All endpoint uses generator. It will load data page by page, querying later pages only if you need them.

## Saving data for later

```python
import pywaybiller
from pywaybiller.openapi_client import ExternalAPIVehicle
from my_project.models import SomeDjangoModel

instance = SomeDjangoModel()
# Sanitize data for serialization for later use
instance.json_field = pywaybiller.WaybillerClient.sanitize_for_serialization(
    ExternalAPIVehicle(
        id=1,
        reg_number="839PVF",
        trailer_reg_number="042TST",
        inactive=False,
        company_name="Test company",
        company_reg_code="10000042"
    )
)

instance.save()
instance.refresh_from_db()

# Rehydrate the data saved earlier
api_model = pywaybiller.WaybillerClient.deserialize_data(
    instance.json_field, ExternalAPIVehicle
)
```

Deserialize data method calls pydantic from_dict internally, but hides implementation details
that may change in future from the code using the API client.

## Credits

This project is generated with help of dockerized openapi generator: https://hub.docker.com/r/openapitools/openapi-generator-cli