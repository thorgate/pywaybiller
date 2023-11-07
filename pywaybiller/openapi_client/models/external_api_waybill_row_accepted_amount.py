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
from pydantic import BaseModel, Field, StrictStr, conlist


class ExternalAPIWaybillRowAcceptedAmount(BaseModel):
    """
    Accepted amounts  # noqa: E501
    """

    assortment_id: StrictStr = Field(
        ...,
        description="The ID of the accepted assortment (eg 1). Use Querying of a single waybill endpoint to see the available assortments inside rows field using the assortment_raw_id value.",
    )
    assortment_ids: Optional[conlist(StrictStr)] = Field(
        None,
        description="The external IDs of the assortment. Usually `null` if waybill was created in Waybiller UI and not over Waybiller External API.",
    )
    accepted_gross_weight: Optional[StrictStr] = Field(
        None, description="The accepted gross weight in tonnes."
    )
    accepted_tare_weight: Optional[StrictStr] = Field(
        None, description="The accepted tare weight in tonnes."
    )
    accepted_amount: Optional[StrictStr] = Field(
        None,
        description="The accepted amount in the unit that is attached to the assortment.",
    )
    __properties = [
        "assortment_id",
        "assortment_ids",
        "accepted_gross_weight",
        "accepted_tare_weight",
        "accepted_amount",
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
    def from_json(cls, json_str: str) -> ExternalAPIWaybillRowAcceptedAmount:
        """Create an instance of ExternalAPIWaybillRowAcceptedAmount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "assortment_ids",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalAPIWaybillRowAcceptedAmount:
        """Create an instance of ExternalAPIWaybillRowAcceptedAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalAPIWaybillRowAcceptedAmount.parse_obj(obj)

        _obj = ExternalAPIWaybillRowAcceptedAmount.parse_obj(
            {
                "assortment_id": obj.get("assortment_id"),
                "assortment_ids": obj.get("assortment_ids"),
                "accepted_gross_weight": obj.get("accepted_gross_weight"),
                "accepted_tare_weight": obj.get("accepted_tare_weight"),
                "accepted_amount": obj.get("accepted_amount"),
            }
        )
        return _obj
