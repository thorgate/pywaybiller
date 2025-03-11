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
from typing import List, Optional
from pydantic import BaseModel, conlist, constr
from pywaybiller.openapi_client.models.external_api_loader_action_log_comment import (
    ExternalAPILoaderActionLogComment,
)
from pywaybiller.openapi_client.models.external_api_loader_action_log_raw_data import (
    ExternalAPILoaderActionLogRawData,
)


class ExternalAPILoaderActionLog(BaseModel):
    """
    ExternalAPILoaderActionLog
    """

    log_timestamp: Optional[datetime] = None
    log_description: Optional[constr(strict=True, min_length=1)] = None
    loader_operator_user_name: Optional[constr(strict=True, min_length=1)] = None
    action_name: Optional[constr(strict=True, min_length=1)] = None
    origin_name: Optional[constr(strict=True, min_length=1)] = None
    order_number: Optional[constr(strict=True, min_length=1)] = None
    vehicle_reg_number: Optional[constr(strict=True, min_length=1)] = None
    trailer_reg_number: Optional[constr(strict=True, min_length=1)] = None
    waybill_number: Optional[constr(strict=True, min_length=1)] = None
    loader_unit_name: Optional[constr(strict=True, min_length=1)] = None
    assortment_name: Optional[constr(strict=True, min_length=1)] = None
    subset_name: Optional[constr(strict=True, min_length=1)] = None
    weight: Optional[constr(strict=True, min_length=1)] = None
    log_comments: Optional[conlist(ExternalAPILoaderActionLogComment)] = None
    raw_data: Optional[ExternalAPILoaderActionLogRawData] = None
    __properties = [
        "log_timestamp",
        "log_description",
        "loader_operator_user_name",
        "action_name",
        "origin_name",
        "order_number",
        "vehicle_reg_number",
        "trailer_reg_number",
        "waybill_number",
        "loader_unit_name",
        "assortment_name",
        "subset_name",
        "weight",
        "log_comments",
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
    def from_json(cls, json_str: str) -> ExternalAPILoaderActionLog:
        """Create an instance of ExternalAPILoaderActionLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "log_timestamp",
                "log_description",
                "loader_operator_user_name",
                "action_name",
                "origin_name",
                "order_number",
                "vehicle_reg_number",
                "trailer_reg_number",
                "waybill_number",
                "loader_unit_name",
                "assortment_name",
                "subset_name",
                "weight",
                "log_comments",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in log_comments (list)
        _items = []
        if self.log_comments:
            for _item in self.log_comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict["log_comments"] = _items
        # override the default output from pydantic by calling `to_dict()` of raw_data
        if self.raw_data:
            _dict["raw_data"] = self.raw_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalAPILoaderActionLog:
        """Create an instance of ExternalAPILoaderActionLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalAPILoaderActionLog.parse_obj(obj)

        _obj = ExternalAPILoaderActionLog.parse_obj(
            {
                "log_timestamp": obj.get("log_timestamp"),
                "log_description": obj.get("log_description"),
                "loader_operator_user_name": obj.get("loader_operator_user_name"),
                "action_name": obj.get("action_name"),
                "origin_name": obj.get("origin_name"),
                "order_number": obj.get("order_number"),
                "vehicle_reg_number": obj.get("vehicle_reg_number"),
                "trailer_reg_number": obj.get("trailer_reg_number"),
                "waybill_number": obj.get("waybill_number"),
                "loader_unit_name": obj.get("loader_unit_name"),
                "assortment_name": obj.get("assortment_name"),
                "subset_name": obj.get("subset_name"),
                "weight": obj.get("weight"),
                "log_comments": [
                    ExternalAPILoaderActionLogComment.from_dict(_item)
                    for _item in obj.get("log_comments")
                ]
                if obj.get("log_comments") is not None
                else None,
                "raw_data": ExternalAPILoaderActionLogRawData.from_dict(
                    obj.get("raw_data")
                )
                if obj.get("raw_data") is not None
                else None,
            }
        )
        return _obj
