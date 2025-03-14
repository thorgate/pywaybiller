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
from pydantic import BaseModel, Field, constr
from pywaybiller.openapi_client.models.ext_api_holding_base_previous_owner import (
    ExtAPIHoldingBasePreviousOwner,
)


class ExtAPIHoldingBaseRead(BaseModel):
    """
    Holding base data is provided as is, in internal WB format. It may change at any time without warning and may have a different schema for old and new origins  # noqa: E501
    """

    type: Optional[constr(strict=True, min_length=1)] = None
    contract_number: Optional[constr(strict=True, max_length=32, min_length=1)] = Field(
        None, alias="contractNumber"
    )
    contract_date: Optional[constr(strict=True, max_length=32, min_length=1)] = Field(
        None, alias="contractDate"
    )
    previous_owner: Optional[ExtAPIHoldingBasePreviousOwner] = Field(
        None, alias="previousOwner"
    )
    __properties = ["type", "contractNumber", "contractDate", "previousOwner"]

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
    def from_json(cls, json_str: str) -> ExtAPIHoldingBaseRead:
        """Create an instance of ExtAPIHoldingBaseRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of previous_owner
        if self.previous_owner:
            _dict["previousOwner"] = self.previous_owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExtAPIHoldingBaseRead:
        """Create an instance of ExtAPIHoldingBaseRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExtAPIHoldingBaseRead.parse_obj(obj)

        _obj = ExtAPIHoldingBaseRead.parse_obj(
            {
                "type": obj.get("type"),
                "contract_number": obj.get("contractNumber"),
                "contract_date": obj.get("contractDate"),
                "previous_owner": ExtAPIHoldingBasePreviousOwner.from_dict(
                    obj.get("previousOwner")
                )
                if obj.get("previousOwner") is not None
                else None,
            }
        )
        return _obj
