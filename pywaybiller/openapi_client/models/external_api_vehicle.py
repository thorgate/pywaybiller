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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, constr


class ExternalAPIVehicle(BaseModel):
    """
    ExternalAPIVehicle
    """

    id: Optional[StrictInt] = None
    reg_number: constr(strict=True, min_length=1) = Field(...)
    trailer_reg_number: constr(strict=True, min_length=1) = Field(...)
    inactive: Optional[StrictBool] = Field(
        None, description="Mitteaktiivseid sõidukeid ei saa kasutada"
    )
    company_name: constr(strict=True, min_length=1) = Field(...)
    company_reg_code: constr(strict=True, min_length=1) = Field(...)
    __properties = [
        "id",
        "reg_number",
        "trailer_reg_number",
        "inactive",
        "company_name",
        "company_reg_code",
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
    def from_json(cls, json_str: str) -> ExternalAPIVehicle:
        """Create an instance of ExternalAPIVehicle from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "id",
                "inactive",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalAPIVehicle:
        """Create an instance of ExternalAPIVehicle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalAPIVehicle.parse_obj(obj)

        _obj = ExternalAPIVehicle.parse_obj(
            {
                "id": obj.get("id"),
                "reg_number": obj.get("reg_number"),
                "trailer_reg_number": obj.get("trailer_reg_number"),
                "inactive": obj.get("inactive"),
                "company_name": obj.get("company_name"),
                "company_reg_code": obj.get("company_reg_code"),
            }
        )
        return _obj
