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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator


class ExternalAPITransportOrderRawDataList(BaseModel):
    """
    ExternalAPITransportOrderRawDataList
    """

    transport_order_id: StrictInt = Field(...)
    status: Optional[StrictStr] = None
    number: Optional[constr(strict=True, min_length=1)] = None
    entity_code: Optional[constr(strict=True, min_length=1)] = None
    waybills_ids: conlist(StrictInt, unique_items=True) = Field(...)
    __properties = [
        "transport_order_id",
        "status",
        "number",
        "entity_code",
        "waybills_ids",
    ]

    @validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "draft",
            "new",
            "approaching_origin",
            "approaching_destination",
            "in_destination",
            "accepted",
            "cancelled",
        ):
            raise ValueError(
                "must be one of enum values ('draft', 'new', 'approaching_origin', 'approaching_destination', 'in_destination', 'accepted', 'cancelled')"
            )
        return value

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
    def from_json(cls, json_str: str) -> ExternalAPITransportOrderRawDataList:
        """Create an instance of ExternalAPITransportOrderRawDataList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "status",
                "number",
                "entity_code",
            },
            exclude_none=True,
        )
        # set to None if number (nullable) is None
        # and __fields_set__ contains the field
        if self.number is None and "number" in self.__fields_set__:
            _dict["number"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalAPITransportOrderRawDataList:
        """Create an instance of ExternalAPITransportOrderRawDataList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalAPITransportOrderRawDataList.parse_obj(obj)

        _obj = ExternalAPITransportOrderRawDataList.parse_obj(
            {
                "transport_order_id": obj.get("transport_order_id"),
                "status": obj.get("status"),
                "number": obj.get("number"),
                "entity_code": obj.get("entity_code"),
                "waybills_ids": obj.get("waybills_ids"),
            }
        )
        return _obj
