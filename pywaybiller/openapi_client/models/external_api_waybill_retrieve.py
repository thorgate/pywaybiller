# coding: utf-8

"""
    Waybiller External API

     **Waybiller** external API is a feature that allows companies to access **Waybiller** data as JSON objects and create **Waybiller** instances out of their own data.  To make integration easier for the companies, external API features mapping support - it is possible to create company specific mappings for object identifiers (such as destination and origin).  These mappings will be used for representing companies data from external API, and for converting the values during creation of **Waybiller** instances (such as transport orders and waybills).  Most of the API responses contain mapped values, that may be null if company doesn't have mapping for this object.  **Waybiller** unique identifiers and values can be accessed through `raw_data` key.  API is HTTPS and JSON based.  # Pagination  By default, results of list endpoints are presented with pages of 30 items.  It is possible to control the page size with `limit` parameter: `/external-api/<some-list-endpoint>/?limit=<number>` where `<number>` is an integer between 1 and 1000. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional, Union
from pydantic import (
    BaseModel,
    Field,
    StrictFloat,
    StrictInt,
    StrictStr,
    conlist,
    constr,
)
from pywaybiller.openapi_client.models.external_api_waybill_raw_data import (
    ExternalAPIWaybillRawData,
)
from pywaybiller.openapi_client.models.external_api_waybill_row import (
    ExternalAPIWaybillRow,
)


class ExternalAPIWaybillRetrieve(BaseModel):
    """
    ExternalAPIWaybillRetrieve
    """

    waybill_id: Optional[constr(strict=True, min_length=1)] = Field(
        None,
        description="The external ID of the waybill. Usually `null` if waybill was created in Waybiller UI and not over Waybiller External API.",
    )
    number: Optional[constr(strict=True, min_length=1)] = None
    status: Optional[StrictInt] = None
    status_description: Optional[
        constr(strict=True, max_length=255, min_length=1)
    ] = Field(
        None,
        description="Human readable status description (`Created`, `In progress`, `At destination`, `Confirmed` or `Cancelled`).",
    )
    rows: conlist(ExternalAPIWaybillRow) = Field(..., description="Waybill rows.")
    destination_raw_id: Optional[constr(strict=True, min_length=1)] = Field(
        None, description="The ID of the destination."
    )
    destination_id: Optional[StrictStr] = Field(
        None,
        description="The external ID of the destination. Usually `null` if waybill was created in Waybiller UI and not over Waybiller External API.",
    )
    destination_name: Optional[StrictStr] = Field(
        None, description="The name of the destination."
    )
    destination_address: Optional[StrictStr] = Field(
        None, description="The address of the destination."
    )
    destination_latitude: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="The latitude of the destination."
    )
    destination_longitude: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="The longitude of the destination."
    )
    destination_company_name: Optional[constr(strict=True, min_length=1)] = Field(
        None,
        description="The name of the receiving company. Usually the owner company of the destination.",
    )
    destination_company_reg_code: Optional[constr(strict=True, min_length=1)] = Field(
        None,
        description="The registry code of the receiving company. Usually the owner company of the destination.",
    )
    destination_waybill_reached_destination_emails: Optional[
        conlist(constr(strict=True, max_length=254))
    ] = Field(
        None,
        description="Comma separated list of e-mail addresses to whom send an e-mail when waybill reaches destination.",
    )
    destination_waybill_accepted_emails: Optional[
        conlist(constr(strict=True, max_length=254))
    ] = Field(
        None,
        description="Comma separated list of e-mail addresses to whom send an e-mail when waybill is accepted.",
    )
    receiver_company_name: Optional[StrictStr] = Field(
        None, description="The name of the receiving company."
    )
    receiver_company_reg_code: Optional[constr(strict=True, min_length=1)] = Field(
        None, description="The registry code of the receiving company."
    )
    origin_raw_id: Optional[constr(strict=True, min_length=1)] = Field(
        None, description="The ID of the origin."
    )
    origin_id: Optional[StrictInt] = Field(
        None,
        description="The external ID of the origin. Usually `null` if waybill was created in Waybiller UI and not over Waybiller External API.",
    )
    origin_name: Optional[constr(strict=True, min_length=1)] = Field(
        None, description="The name of the origin."
    )
    origin_address: Optional[constr(strict=True, min_length=1)] = Field(
        None, description="The address of the origin."
    )
    origin_latitude: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="The latitude of the origin."
    )
    origin_longitude: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="The longitude of the origin."
    )
    origin_waybill_reached_destination_emails: Optional[
        conlist(constr(strict=True, max_length=254))
    ] = Field(
        None,
        description="Comma separated list of e-mail addresses to whom send an e-mail when waybill reaches destination.",
    )
    origin_waybill_accepted_emails: Optional[
        conlist(constr(strict=True, max_length=254))
    ] = Field(
        None,
        description="Comma separated list of e-mail addresses to whom send an e-mail when waybill is accepted.",
    )
    cadaster_number: Optional[constr(strict=True, max_length=500)] = Field(
        None, description="Cadaster number."
    )
    dispatcher_name: Optional[StrictStr] = None
    dispatcher_phone: Optional[StrictStr] = None
    shipper_company_name: Optional[constr(strict=True, max_length=64)] = Field(
        None, description="The name of the shipper company."
    )
    shipper_company_reg_code: Optional[constr(strict=True, max_length=16)] = Field(
        None, description="The registry code of the shipper company."
    )
    transportation_company_name: Optional[constr(strict=True, max_length=64)] = Field(
        None, description="The name of the transportation company."
    )
    transportation_company_reg_code: Optional[
        constr(strict=True, max_length=16)
    ] = Field(None, description="The registry code of the transportation company.")
    truck_reg_number: constr(strict=True, min_length=1) = Field(
        ..., description="The registration number of the vehicle."
    )
    trailer_reg_number: Optional[StrictStr] = Field(
        None, description="The registration number of the trailer."
    )
    driver_email: Optional[constr(strict=True, max_length=254)] = Field(
        None, description="The e-mail address of the driver user."
    )
    driver_name: Optional[constr(strict=True, max_length=255)] = Field(
        None, description="The name of the driver."
    )
    driver_phone: Optional[constr(strict=True, max_length=128)] = Field(
        None, description="The phone number of the driver."
    )
    driver_personal_code: Optional[constr(strict=True, max_length=24)] = Field(
        None, description="The personal code of the driver."
    )
    mileage: Optional[StrictInt] = Field(
        None,
        description="The mileage can be calculated using a map or can be taken from Distance object if exist",
    )
    mileage_by_driver: Optional[StrictInt] = None
    confirmed_by_email: Optional[
        constr(strict=True, max_length=255, min_length=1)
    ] = Field(
        None, description="The e-mail address of the user that accepted the waybill."
    )
    confirmed_by_name: Optional[StrictStr] = None
    confirmed_by_phone: Optional[StrictStr] = None
    cancelled_by_email: Optional[
        constr(strict=True, max_length=255, min_length=1)
    ] = Field(
        None, description="The e-mail address of the user that cancelled the waybill."
    )
    cancelled_by_name: Optional[StrictStr] = None
    cancelled_by_phone: Optional[StrictStr] = None
    cancelling_reason: Optional[StrictStr] = None
    dispatcher_timestamp: Optional[datetime] = Field(
        None, description="Veoselehe loomise aeg"
    )
    driver_timestamp: Optional[datetime] = Field(
        None, description="Hetk millal autojuht alustas sõitu"
    )
    destination_timestamp: Optional[datetime] = Field(
        None, description="Time when waybill reached destination."
    )
    confirmed_timestamp: Optional[datetime] = Field(
        None, description="Sihtkohas kinnitamise aeg"
    )
    cancelled_timestamp: Optional[datetime] = Field(
        None, description="Veoselehe tühistamise aeg"
    )
    pdf_url: Optional[StrictStr] = None
    navision_bin_code: Optional[StrictStr] = Field(None, description="Bin code.")
    evr_waybill_number: Optional[StrictStr] = Field(
        None, description="EVR waybill number."
    )
    raw_data: Optional[ExternalAPIWaybillRawData] = None
    __properties = [
        "waybill_id",
        "number",
        "status",
        "status_description",
        "rows",
        "destination_raw_id",
        "destination_id",
        "destination_name",
        "destination_address",
        "destination_latitude",
        "destination_longitude",
        "destination_company_name",
        "destination_company_reg_code",
        "destination_waybill_reached_destination_emails",
        "destination_waybill_accepted_emails",
        "receiver_company_name",
        "receiver_company_reg_code",
        "origin_raw_id",
        "origin_id",
        "origin_name",
        "origin_address",
        "origin_latitude",
        "origin_longitude",
        "origin_waybill_reached_destination_emails",
        "origin_waybill_accepted_emails",
        "cadaster_number",
        "dispatcher_name",
        "dispatcher_phone",
        "shipper_company_name",
        "shipper_company_reg_code",
        "transportation_company_name",
        "transportation_company_reg_code",
        "truck_reg_number",
        "trailer_reg_number",
        "driver_email",
        "driver_name",
        "driver_phone",
        "driver_personal_code",
        "mileage",
        "mileage_by_driver",
        "confirmed_by_email",
        "confirmed_by_name",
        "confirmed_by_phone",
        "cancelled_by_email",
        "cancelled_by_name",
        "cancelled_by_phone",
        "cancelling_reason",
        "dispatcher_timestamp",
        "driver_timestamp",
        "destination_timestamp",
        "confirmed_timestamp",
        "cancelled_timestamp",
        "pdf_url",
        "navision_bin_code",
        "evr_waybill_number",
        "raw_data",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ExternalAPIWaybillRetrieve:
        """Create an instance of ExternalAPIWaybillRetrieve from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "waybill_id",
                "number",
                "status",
                "destination_id",
                "destination_name",
                "destination_address",
                "destination_waybill_reached_destination_emails",
                "destination_waybill_accepted_emails",
                "receiver_company_name",
                "receiver_company_reg_code",
                "origin_waybill_reached_destination_emails",
                "origin_waybill_accepted_emails",
                "cadaster_number",
                "dispatcher_name",
                "dispatcher_phone",
                "shipper_company_name",
                "shipper_company_reg_code",
                "transportation_company_name",
                "transportation_company_reg_code",
                "mileage",
                "mileage_by_driver",
                "confirmed_by_name",
                "confirmed_by_phone",
                "cancelled_by_name",
                "cancelled_by_phone",
                "cancelling_reason",
                "dispatcher_timestamp",
                "driver_timestamp",
                "destination_timestamp",
                "confirmed_timestamp",
                "cancelled_timestamp",
                "pdf_url",
                "navision_bin_code",
                "evr_waybill_number",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in rows (list)
        _items = []
        if self.rows:
            for _item in self.rows:
                if _item:
                    _items.append(_item.to_dict())
            _dict["rows"] = _items
        # override the default output from pydantic by calling `to_dict()` of raw_data
        if self.raw_data:
            _dict["raw_data"] = self.raw_data.to_dict()
        # set to None if waybill_id (nullable) is None
        # and __fields_set__ contains the field
        if self.waybill_id is None and "waybill_id" in self.__fields_set__:
            _dict["waybill_id"] = None

        # set to None if destination_id (nullable) is None
        # and __fields_set__ contains the field
        if self.destination_id is None and "destination_id" in self.__fields_set__:
            _dict["destination_id"] = None

        # set to None if destination_waybill_reached_destination_emails (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.destination_waybill_reached_destination_emails is None
            and "destination_waybill_reached_destination_emails" in self.__fields_set__
        ):
            _dict["destination_waybill_reached_destination_emails"] = None

        # set to None if destination_waybill_accepted_emails (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.destination_waybill_accepted_emails is None
            and "destination_waybill_accepted_emails" in self.__fields_set__
        ):
            _dict["destination_waybill_accepted_emails"] = None

        # set to None if origin_waybill_reached_destination_emails (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.origin_waybill_reached_destination_emails is None
            and "origin_waybill_reached_destination_emails" in self.__fields_set__
        ):
            _dict["origin_waybill_reached_destination_emails"] = None

        # set to None if origin_waybill_accepted_emails (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.origin_waybill_accepted_emails is None
            and "origin_waybill_accepted_emails" in self.__fields_set__
        ):
            _dict["origin_waybill_accepted_emails"] = None

        # set to None if mileage (nullable) is None
        # and __fields_set__ contains the field
        if self.mileage is None and "mileage" in self.__fields_set__:
            _dict["mileage"] = None

        # set to None if mileage_by_driver (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.mileage_by_driver is None
            and "mileage_by_driver" in self.__fields_set__
        ):
            _dict["mileage_by_driver"] = None

        # set to None if confirmed_by_email (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.confirmed_by_email is None
            and "confirmed_by_email" in self.__fields_set__
        ):
            _dict["confirmed_by_email"] = None

        # set to None if cancelled_by_email (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.cancelled_by_email is None
            and "cancelled_by_email" in self.__fields_set__
        ):
            _dict["cancelled_by_email"] = None

        # set to None if driver_timestamp (nullable) is None
        # and __fields_set__ contains the field
        if self.driver_timestamp is None and "driver_timestamp" in self.__fields_set__:
            _dict["driver_timestamp"] = None

        # set to None if confirmed_timestamp (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.confirmed_timestamp is None
            and "confirmed_timestamp" in self.__fields_set__
        ):
            _dict["confirmed_timestamp"] = None

        # set to None if cancelled_timestamp (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.cancelled_timestamp is None
            and "cancelled_timestamp" in self.__fields_set__
        ):
            _dict["cancelled_timestamp"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalAPIWaybillRetrieve:
        """Create an instance of ExternalAPIWaybillRetrieve from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalAPIWaybillRetrieve.parse_obj(obj)

        _obj = ExternalAPIWaybillRetrieve.parse_obj(
            {
                "waybill_id": obj.get("waybill_id"),
                "number": obj.get("number"),
                "status": obj.get("status"),
                "status_description": obj.get("status_description"),
                "rows": [
                    ExternalAPIWaybillRow.from_dict(_item) for _item in obj.get("rows")
                ]
                if obj.get("rows") is not None
                else None,
                "destination_raw_id": obj.get("destination_raw_id"),
                "destination_id": obj.get("destination_id"),
                "destination_name": obj.get("destination_name"),
                "destination_address": obj.get("destination_address"),
                "destination_latitude": obj.get("destination_latitude"),
                "destination_longitude": obj.get("destination_longitude"),
                "destination_company_name": obj.get("destination_company_name"),
                "destination_company_reg_code": obj.get("destination_company_reg_code"),
                "destination_waybill_reached_destination_emails": obj.get(
                    "destination_waybill_reached_destination_emails"
                ),
                "destination_waybill_accepted_emails": obj.get(
                    "destination_waybill_accepted_emails"
                ),
                "receiver_company_name": obj.get("receiver_company_name"),
                "receiver_company_reg_code": obj.get("receiver_company_reg_code"),
                "origin_raw_id": obj.get("origin_raw_id"),
                "origin_id": obj.get("origin_id"),
                "origin_name": obj.get("origin_name"),
                "origin_address": obj.get("origin_address"),
                "origin_latitude": obj.get("origin_latitude"),
                "origin_longitude": obj.get("origin_longitude"),
                "origin_waybill_reached_destination_emails": obj.get(
                    "origin_waybill_reached_destination_emails"
                ),
                "origin_waybill_accepted_emails": obj.get(
                    "origin_waybill_accepted_emails"
                ),
                "cadaster_number": obj.get("cadaster_number"),
                "dispatcher_name": obj.get("dispatcher_name"),
                "dispatcher_phone": obj.get("dispatcher_phone"),
                "shipper_company_name": obj.get("shipper_company_name"),
                "shipper_company_reg_code": obj.get("shipper_company_reg_code"),
                "transportation_company_name": obj.get("transportation_company_name"),
                "transportation_company_reg_code": obj.get(
                    "transportation_company_reg_code"
                ),
                "truck_reg_number": obj.get("truck_reg_number"),
                "trailer_reg_number": obj.get("trailer_reg_number"),
                "driver_email": obj.get("driver_email"),
                "driver_name": obj.get("driver_name"),
                "driver_phone": obj.get("driver_phone"),
                "driver_personal_code": obj.get("driver_personal_code"),
                "mileage": obj.get("mileage"),
                "mileage_by_driver": obj.get("mileage_by_driver"),
                "confirmed_by_email": obj.get("confirmed_by_email"),
                "confirmed_by_name": obj.get("confirmed_by_name"),
                "confirmed_by_phone": obj.get("confirmed_by_phone"),
                "cancelled_by_email": obj.get("cancelled_by_email"),
                "cancelled_by_name": obj.get("cancelled_by_name"),
                "cancelled_by_phone": obj.get("cancelled_by_phone"),
                "cancelling_reason": obj.get("cancelling_reason"),
                "dispatcher_timestamp": obj.get("dispatcher_timestamp"),
                "driver_timestamp": obj.get("driver_timestamp"),
                "destination_timestamp": obj.get("destination_timestamp"),
                "confirmed_timestamp": obj.get("confirmed_timestamp"),
                "cancelled_timestamp": obj.get("cancelled_timestamp"),
                "pdf_url": obj.get("pdf_url"),
                "navision_bin_code": obj.get("navision_bin_code"),
                "evr_waybill_number": obj.get("evr_waybill_number"),
                "raw_data": ExternalAPIWaybillRawData.from_dict(obj.get("raw_data"))
                if obj.get("raw_data") is not None
                else None,
            }
        )
        return _obj
