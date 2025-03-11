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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self

from pywaybiller.openapi_client.models.external_api_holding_base_previous_owner import (
    ExternalAPIHoldingBasePreviousOwner,
)


class ExternalAPIHoldingBaseRead(BaseModel):
    """
    ExternalAPIHoldingBaseRead
    """  # noqa: E501

    type: Optional[StrictStr] = None
    contract_number: Optional[Annotated[str, Field(strict=True, max_length=32)]] = (
        Field(default=None, alias="contractNumber")
    )
    contract_date: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(
        default=None, alias="contractDate"
    )
    previous_owner: Optional[ExternalAPIHoldingBasePreviousOwner] = Field(
        default=None, alias="previousOwner"
    )
    __properties: ClassVar[List[str]] = [
        "type",
        "contractNumber",
        "contractDate",
        "previousOwner",
    ]

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
        """Create an instance of ExternalAPIHoldingBaseRead from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of previous_owner
        if self.previous_owner:
            _dict["previousOwner"] = self.previous_owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalAPIHoldingBaseRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "type": obj.get("type"),
                "contractNumber": obj.get("contractNumber"),
                "contractDate": obj.get("contractDate"),
                "previousOwner": ExternalAPIHoldingBasePreviousOwner.from_dict(
                    obj["previousOwner"]
                )
                if obj.get("previousOwner") is not None
                else None,
            }
        )
        return _obj
