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
from pydantic import BaseModel, Field, StrictInt, conlist


class ExtAPIOriginAssortment(BaseModel):
    """
    ExtAPIOriginAssortment
    """

    id: StrictInt = Field(..., description="Assortment ID")
    subsets: Optional[conlist(StrictInt, unique_items=True)] = Field(
        None, description="List of subset IDs"
    )
    __properties = ["id", "subsets"]

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
    def from_json(cls, json_str: str) -> ExtAPIOriginAssortment:
        """Create an instance of ExtAPIOriginAssortment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExtAPIOriginAssortment:
        """Create an instance of ExtAPIOriginAssortment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExtAPIOriginAssortment.parse_obj(obj)

        _obj = ExtAPIOriginAssortment.parse_obj(
            {"id": obj.get("id"), "subsets": obj.get("subsets")}
        )
        return _obj
