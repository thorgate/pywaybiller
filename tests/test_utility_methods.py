import json

import pytest
from pywaybiller import WaybillerClient, openapi_client


def test_client_can_deserialize_data():
    # Given valid vehicle data
    data = {
        "id": 1,
        "reg_number": "839PVF",
        "trailer_reg_number": "042TST",
        "inactive": False,
        "company_name": "Test company",
        "company_reg_code": "10000042"
    }

    # When client is used to deserialize the data
    vehicle = WaybillerClient.deserialize_data(data, openapi_client.ExternalAPIVehicle)

    # Then it is usable
    assert isinstance(vehicle, openapi_client.ExternalAPIVehicle)

    # And the data is correct
    assert vehicle.reg_number == "839PVF"


def test_client_can_sanitize_for_serialization():
    # Given valid vehicle model
    vehicle = openapi_client.ExternalAPIVehicle(
        id=1,
        reg_number="839PVF",
        trailer_reg_number="042TST",
        inactive=False,
        company_name="Test company",
        company_reg_code="10000042"
    )

    # When client is used to serialize the data
    vehicle_data = WaybillerClient.sanitize_for_serialization(vehicle)

    # Then the result is JSON-serializable
    serialized_vehicle = json.dumps(vehicle_data)

    # And the data is not mangled
    assert json.loads(serialized_vehicle).get("reg_number", "") == "839PVF", serialized_vehicle
