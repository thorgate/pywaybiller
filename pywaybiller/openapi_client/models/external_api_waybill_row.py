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


class ExternalAPIWaybillRow(BaseModel):
    """
    ExternalAPIWaybillRow
    """  # noqa: E501

    assortment_id: Optional[StrictStr] = Field(
        default=None,
        description="The external ID of the assortment. Usually `null` if waybill was created in Waybiller UI and not over Waybiller External API.",
    )
    assortment_ids: Optional[List[StrictStr]] = Field(
        description="The external IDs of the assortment. Usually `null` if waybill was created in Waybiller UI and not over Waybiller External API."
    )
    assortment_raw_id: Optional[StrictInt] = Field(
        default=None, description="The ID of the assortment."
    )
    scale_assortment_raw_id: Optional[StrictInt] = Field(
        description="The ID of the destination scale assortment."
    )
    assortment_name: Optional[StrictStr] = Field(
        default=None, description="The name of the assortment."
    )
    dispatched_amount: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Dispatched material amount"
    )
    accepted_amount: Optional[Annotated[str, Field(strict=True)]]
    subset_type_name: Optional[StrictStr] = Field(
        description="Subset type (eg fraction)."
    )
    subset_object_raw_id: Optional[StrictInt] = Field(
        default=None, description="The ID of the subset of the assortment."
    )
    subset_object_name: Optional[StrictStr] = Field(
        description="Subset object (eg 0-32mm)."
    )
    extra_information_long: Optional[StrictStr] = None
    extra_information_short: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "assortment_id",
        "assortment_ids",
        "assortment_raw_id",
        "scale_assortment_raw_id",
        "assortment_name",
        "dispatched_amount",
        "accepted_amount",
        "subset_type_name",
        "subset_object_raw_id",
        "subset_object_name",
        "extra_information_long",
        "extra_information_short",
    ]

    @field_validator("dispatched_amount")
    def dispatched_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^-?\d{0,5}(?:\.\d{0,3})?$", value):
            raise ValueError(
                r"must validate the regular expression /^-?\d{0,5}(?:\.\d{0,3})?$/"
            )
        return value

    @field_validator("accepted_amount")
    def accepted_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of ExternalAPIWaybillRow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "assortment_ids",
                "scale_assortment_raw_id",
                "accepted_amount",
                "subset_type_name",
                "subset_object_name",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if assortment_id (nullable) is None
        # and model_fields_set contains the field
        if self.assortment_id is None and "assortment_id" in self.model_fields_set:
            _dict["assortment_id"] = None

        # set to None if assortment_ids (nullable) is None
        # and model_fields_set contains the field
        if self.assortment_ids is None and "assortment_ids" in self.model_fields_set:
            _dict["assortment_ids"] = None

        # set to None if scale_assortment_raw_id (nullable) is None
        # and model_fields_set contains the field
        if (
            self.scale_assortment_raw_id is None
            and "scale_assortment_raw_id" in self.model_fields_set
        ):
            _dict["scale_assortment_raw_id"] = None

        # set to None if accepted_amount (nullable) is None
        # and model_fields_set contains the field
        if self.accepted_amount is None and "accepted_amount" in self.model_fields_set:
            _dict["accepted_amount"] = None

        # set to None if subset_type_name (nullable) is None
        # and model_fields_set contains the field
        if (
            self.subset_type_name is None
            and "subset_type_name" in self.model_fields_set
        ):
            _dict["subset_type_name"] = None

        # set to None if subset_object_name (nullable) is None
        # and model_fields_set contains the field
        if (
            self.subset_object_name is None
            and "subset_object_name" in self.model_fields_set
        ):
            _dict["subset_object_name"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalAPIWaybillRow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "assortment_id": obj.get("assortment_id"),
                "assortment_ids": obj.get("assortment_ids"),
                "assortment_raw_id": obj.get("assortment_raw_id"),
                "scale_assortment_raw_id": obj.get("scale_assortment_raw_id"),
                "assortment_name": obj.get("assortment_name"),
                "dispatched_amount": obj.get("dispatched_amount"),
                "accepted_amount": obj.get("accepted_amount"),
                "subset_type_name": obj.get("subset_type_name"),
                "subset_object_raw_id": obj.get("subset_object_raw_id"),
                "subset_object_name": obj.get("subset_object_name"),
                "extra_information_long": obj.get("extra_information_long"),
                "extra_information_short": obj.get("extra_information_short"),
            }
        )
        return _obj
