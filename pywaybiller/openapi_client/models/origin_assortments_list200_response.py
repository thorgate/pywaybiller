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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from pywaybiller.openapi_client.models.external_api_origin_assortment import (
    ExternalAPIOriginAssortment,
)


class OriginAssortmentsList200Response(BaseModel):
    """
    OriginAssortmentsList200Response
    """

    count: StrictInt = Field(...)
    next: Optional[StrictStr] = None
    previous: Optional[StrictStr] = None
    results: conlist(ExternalAPIOriginAssortment) = Field(...)
    __properties = ["count", "next", "previous", "results"]

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
    def from_json(cls, json_str: str) -> OriginAssortmentsList200Response:
        """Create an instance of OriginAssortmentsList200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict["results"] = _items
        # set to None if next (nullable) is None
        # and __fields_set__ contains the field
        if self.next is None and "next" in self.__fields_set__:
            _dict["next"] = None

        # set to None if previous (nullable) is None
        # and __fields_set__ contains the field
        if self.previous is None and "previous" in self.__fields_set__:
            _dict["previous"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OriginAssortmentsList200Response:
        """Create an instance of OriginAssortmentsList200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OriginAssortmentsList200Response.parse_obj(obj)

        _obj = OriginAssortmentsList200Response.parse_obj(
            {
                "count": obj.get("count"),
                "next": obj.get("next"),
                "previous": obj.get("previous"),
                "results": [
                    ExternalAPIOriginAssortment.from_dict(_item)
                    for _item in obj.get("results")
                ]
                if obj.get("results") is not None
                else None,
            }
        )
        return _obj
