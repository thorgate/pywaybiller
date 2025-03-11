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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from pywaybiller.openapi_client.models.external_api_raw_serializer import (
    ExternalAPIRawSerializer,
)


class ExtAPIDestination(BaseModel):
    """
    ExtAPIDestination
    """

    id: Optional[constr(strict=True, min_length=1)] = Field(...)
    name: StrictStr = Field(...)
    address: StrictStr = Field(...)
    latitude: Union[StrictFloat, StrictInt] = Field(...)
    longitude: Union[StrictFloat, StrictInt] = Field(...)
    raw_data: Optional[ExternalAPIRawSerializer] = None
    owner_name: Optional[constr(strict=True, min_length=1)] = None
    owner_reg_code: Optional[constr(strict=True, min_length=1)] = None
    __properties = [
        "id",
        "name",
        "address",
        "latitude",
        "longitude",
        "raw_data",
        "owner_name",
        "owner_reg_code",
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
    def from_json(cls, json_str: str) -> ExtAPIDestination:
        """Create an instance of ExtAPIDestination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "owner_name",
                "owner_reg_code",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of raw_data
        if self.raw_data:
            _dict["raw_data"] = self.raw_data.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict["id"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExtAPIDestination:
        """Create an instance of ExtAPIDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExtAPIDestination.parse_obj(obj)

        _obj = ExtAPIDestination.parse_obj(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "address": obj.get("address"),
                "latitude": obj.get("latitude"),
                "longitude": obj.get("longitude"),
                "raw_data": ExternalAPIRawSerializer.from_dict(obj.get("raw_data"))
                if obj.get("raw_data") is not None
                else None,
                "owner_name": obj.get("owner_name"),
                "owner_reg_code": obj.get("owner_reg_code"),
            }
        )
        return _obj
