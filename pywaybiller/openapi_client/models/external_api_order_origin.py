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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, constr


class ExternalAPIOrderOrigin(BaseModel):
    """
    The origins for which the order is created for.  # noqa: E501
    """

    origin_raw_id: Optional[constr(strict=True, min_length=1)] = Field(
        None, description="Origin raw id."
    )
    origin_name: Optional[constr(strict=True, max_length=255, min_length=1)] = Field(
        None, description="Origin name."
    )
    origin_address: Optional[constr(strict=True, max_length=255, min_length=1)] = Field(
        None, description="Origin address."
    )
    origin_latitude: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="Origin location - latitude."
    )
    origin_longitude: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="Origin location - longitude."
    )
    shipper_company_name: Optional[
        constr(strict=True, max_length=64, min_length=1)
    ] = Field(None, description="Origin company name.")
    shipper_company_reg_code: Optional[
        constr(strict=True, max_length=16, min_length=1)
    ] = Field(None, description="Origin company reg code.")
    __properties = [
        "origin_raw_id",
        "origin_name",
        "origin_address",
        "origin_latitude",
        "origin_longitude",
        "shipper_company_name",
        "shipper_company_reg_code",
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
    def from_json(cls, json_str: str) -> ExternalAPIOrderOrigin:
        """Create an instance of ExternalAPIOrderOrigin from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalAPIOrderOrigin:
        """Create an instance of ExternalAPIOrderOrigin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalAPIOrderOrigin.parse_obj(obj)

        _obj = ExternalAPIOrderOrigin.parse_obj(
            {
                "origin_raw_id": obj.get("origin_raw_id"),
                "origin_name": obj.get("origin_name"),
                "origin_address": obj.get("origin_address"),
                "origin_latitude": obj.get("origin_latitude"),
                "origin_longitude": obj.get("origin_longitude"),
                "shipper_company_name": obj.get("shipper_company_name"),
                "shipper_company_reg_code": obj.get("shipper_company_reg_code"),
            }
        )
        return _obj
