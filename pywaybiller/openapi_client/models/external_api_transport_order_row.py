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
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Annotated, Self


class ExternalAPITransportOrderRow(BaseModel):
    """
    ExternalAPITransportOrderRow
    """  # noqa: E501

    assortment_id: StrictInt
    assortment_name: Optional[StrictStr] = None
    amount: Annotated[str, Field(strict=True)]
    __properties: ClassVar[List[str]] = ["assortment_id", "assortment_name", "amount"]

    @field_validator("amount")
    def amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-?\d{0,5}(?:\.\d{0,3})?$", value):
            raise ValueError(
                r"must validate the regular expression /^-?\d{0,5}(?:\.\d{0,3})?$/"
            )
        return value

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
        """Create an instance of ExternalAPITransportOrderRow from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalAPITransportOrderRow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "assortment_id": obj.get("assortment_id"),
                "assortment_name": obj.get("assortment_name"),
                "amount": obj.get("amount"),
            }
        )
        return _obj
