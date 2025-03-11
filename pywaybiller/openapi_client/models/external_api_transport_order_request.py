# coding: utf-8

"""
Waybiller External API - with fixes

The **Waybiller External API** is a feature that allows companies to access **Waybiller** data as JSON objects and create **Waybiller** instances out of their own data.  To make integration easier for the companies, the external API provides mapping support - it is possible to create company-specific mappings for object identifiers (such as destination and origin).  These mappings will be used for representing companies data from external API, and for converting the values during the creation of **Waybiller** instances (such as transport orders and waybills).  Most of the API responses contain mapped values, which may be null if the company doesn't have a mapping for this object.  Unique **Waybiller** identifiers and values can be accessed via the `raw_data` key.  The API is HTTPS and JSON based.  ### Pagination  By default, list endpoint responses are presented in pages of 30 items.  It is possible to control the page size using the `limit` parameter: `/external-api/<some-list-endpoint>/?limit=<number>`, where `<number>` is an integer between 1 and 1000.

The version of the OpenAPI document: v1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import date
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing_extensions import Annotated, Self

from pywaybiller.openapi_client.models.external_api_transport_order_row_request import (
    ExternalAPITransportOrderRowRequest,
)


class ExternalAPITransportOrderRequest(BaseModel):
    """
    ExternalAPITransportOrderRequest
    """  # noqa: E501

    transport_order_id: Annotated[str, Field(min_length=1, strict=True)]
    order_raw_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    order_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    rows: List[ExternalAPITransportOrderRowRequest]
    organizer_user_id: StrictInt
    destination_raw_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = (
        None
    )
    destination_id: Optional[StrictInt] = None
    destination_name: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    ] = None
    destination_address: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    ] = None
    destination_latitude: Optional[Union[StrictFloat, StrictInt]] = None
    destination_longitude: Optional[Union[StrictFloat, StrictInt]] = None
    destination_waybill_created_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    destination_waybill_reached_destination_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    destination_waybill_accepted_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    destination_transport_order_created_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    receiver_company_name: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=64)]
    ] = None
    receiver_company_reg_code: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=16)]
    ] = None
    origin_raw_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    origin_id: Optional[StrictInt] = None
    origin_name: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    ] = None
    origin_address: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    ] = None
    origin_latitude: Optional[Union[StrictFloat, StrictInt]] = None
    origin_longitude: Optional[Union[StrictFloat, StrictInt]] = None
    origin_waybill_created_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    origin_waybill_reached_destination_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    origin_waybill_accepted_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    origin_transport_order_created_emails: Optional[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=254)]]
    ] = None
    shipper_company_name: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=64)]
    ] = None
    shipper_company_reg_code: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=16)]
    ] = None
    transportation_company_name: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=64)]
    ] = None
    transportation_company_reg_code: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=16)]
    ] = None
    truck_reg_number: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=16)]
    ] = None
    trailer_reg_number: Optional[Annotated[str, Field(strict=True, max_length=16)]] = (
        None
    )
    driver_email: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=254)]
    ] = None
    driver_personal_code: Optional[
        Annotated[str, Field(strict=True, max_length=24)]
    ] = None
    driver_name: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    ] = None
    driver_phone: Optional[Annotated[str, Field(strict=True, max_length=128)]] = ""
    transport_date: date
    transport_time: Optional[StrictStr] = None
    additional_info: Optional[StrictStr] = None
    pallets_number: Optional[Annotated[int, Field(le=32767, strict=True, ge=0)]] = None
    __properties: ClassVar[List[str]] = [
        "transport_order_id",
        "order_raw_id",
        "order_id",
        "rows",
        "organizer_user_id",
        "destination_raw_id",
        "destination_id",
        "destination_name",
        "destination_address",
        "destination_latitude",
        "destination_longitude",
        "destination_waybill_created_emails",
        "destination_waybill_reached_destination_emails",
        "destination_waybill_accepted_emails",
        "destination_transport_order_created_emails",
        "receiver_company_name",
        "receiver_company_reg_code",
        "origin_raw_id",
        "origin_id",
        "origin_name",
        "origin_address",
        "origin_latitude",
        "origin_longitude",
        "origin_waybill_created_emails",
        "origin_waybill_reached_destination_emails",
        "origin_waybill_accepted_emails",
        "origin_transport_order_created_emails",
        "shipper_company_name",
        "shipper_company_reg_code",
        "transportation_company_name",
        "transportation_company_reg_code",
        "truck_reg_number",
        "trailer_reg_number",
        "driver_email",
        "driver_personal_code",
        "driver_name",
        "driver_phone",
        "transport_date",
        "transport_time",
        "additional_info",
        "pallets_number",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ExternalAPITransportOrderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in rows (list)
        _items = []
        if self.rows:
            for _item_rows in self.rows:
                if _item_rows:
                    _items.append(_item_rows.to_dict())
            _dict["rows"] = _items
        # set to None if destination_waybill_created_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.destination_waybill_created_emails is None
            and "destination_waybill_created_emails" in self.model_fields_set
        ):
            _dict["destination_waybill_created_emails"] = None

        # set to None if destination_waybill_reached_destination_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.destination_waybill_reached_destination_emails is None
            and "destination_waybill_reached_destination_emails"
            in self.model_fields_set
        ):
            _dict["destination_waybill_reached_destination_emails"] = None

        # set to None if destination_waybill_accepted_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.destination_waybill_accepted_emails is None
            and "destination_waybill_accepted_emails" in self.model_fields_set
        ):
            _dict["destination_waybill_accepted_emails"] = None

        # set to None if destination_transport_order_created_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.destination_transport_order_created_emails is None
            and "destination_transport_order_created_emails" in self.model_fields_set
        ):
            _dict["destination_transport_order_created_emails"] = None

        # set to None if origin_waybill_created_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.origin_waybill_created_emails is None
            and "origin_waybill_created_emails" in self.model_fields_set
        ):
            _dict["origin_waybill_created_emails"] = None

        # set to None if origin_waybill_reached_destination_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.origin_waybill_reached_destination_emails is None
            and "origin_waybill_reached_destination_emails" in self.model_fields_set
        ):
            _dict["origin_waybill_reached_destination_emails"] = None

        # set to None if origin_waybill_accepted_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.origin_waybill_accepted_emails is None
            and "origin_waybill_accepted_emails" in self.model_fields_set
        ):
            _dict["origin_waybill_accepted_emails"] = None

        # set to None if origin_transport_order_created_emails (nullable) is None
        # and model_fields_set contains the field
        if (
            self.origin_transport_order_created_emails is None
            and "origin_transport_order_created_emails" in self.model_fields_set
        ):
            _dict["origin_transport_order_created_emails"] = None

        # set to None if transport_time (nullable) is None
        # and model_fields_set contains the field
        if self.transport_time is None and "transport_time" in self.model_fields_set:
            _dict["transport_time"] = None

        # set to None if pallets_number (nullable) is None
        # and model_fields_set contains the field
        if self.pallets_number is None and "pallets_number" in self.model_fields_set:
            _dict["pallets_number"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalAPITransportOrderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "transport_order_id": obj.get("transport_order_id"),
                "order_raw_id": obj.get("order_raw_id"),
                "order_id": obj.get("order_id"),
                "rows": [
                    ExternalAPITransportOrderRowRequest.from_dict(_item)
                    for _item in obj["rows"]
                ]
                if obj.get("rows") is not None
                else None,
                "organizer_user_id": obj.get("organizer_user_id"),
                "destination_raw_id": obj.get("destination_raw_id"),
                "destination_id": obj.get("destination_id"),
                "destination_name": obj.get("destination_name"),
                "destination_address": obj.get("destination_address"),
                "destination_latitude": obj.get("destination_latitude"),
                "destination_longitude": obj.get("destination_longitude"),
                "destination_waybill_created_emails": obj.get(
                    "destination_waybill_created_emails"
                ),
                "destination_waybill_reached_destination_emails": obj.get(
                    "destination_waybill_reached_destination_emails"
                ),
                "destination_waybill_accepted_emails": obj.get(
                    "destination_waybill_accepted_emails"
                ),
                "destination_transport_order_created_emails": obj.get(
                    "destination_transport_order_created_emails"
                ),
                "receiver_company_name": obj.get("receiver_company_name"),
                "receiver_company_reg_code": obj.get("receiver_company_reg_code"),
                "origin_raw_id": obj.get("origin_raw_id"),
                "origin_id": obj.get("origin_id"),
                "origin_name": obj.get("origin_name"),
                "origin_address": obj.get("origin_address"),
                "origin_latitude": obj.get("origin_latitude"),
                "origin_longitude": obj.get("origin_longitude"),
                "origin_waybill_created_emails": obj.get(
                    "origin_waybill_created_emails"
                ),
                "origin_waybill_reached_destination_emails": obj.get(
                    "origin_waybill_reached_destination_emails"
                ),
                "origin_waybill_accepted_emails": obj.get(
                    "origin_waybill_accepted_emails"
                ),
                "origin_transport_order_created_emails": obj.get(
                    "origin_transport_order_created_emails"
                ),
                "shipper_company_name": obj.get("shipper_company_name"),
                "shipper_company_reg_code": obj.get("shipper_company_reg_code"),
                "transportation_company_name": obj.get("transportation_company_name"),
                "transportation_company_reg_code": obj.get(
                    "transportation_company_reg_code"
                ),
                "truck_reg_number": obj.get("truck_reg_number"),
                "trailer_reg_number": obj.get("trailer_reg_number"),
                "driver_email": obj.get("driver_email"),
                "driver_personal_code": obj.get("driver_personal_code"),
                "driver_name": obj.get("driver_name"),
                "driver_phone": obj.get("driver_phone")
                if obj.get("driver_phone") is not None
                else "",
                "transport_date": obj.get("transport_date"),
                "transport_time": obj.get("transport_time"),
                "additional_info": obj.get("additional_info"),
                "pallets_number": obj.get("pallets_number"),
            }
        )
        return _obj
