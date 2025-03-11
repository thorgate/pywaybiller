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
from enum import Enum

from typing_extensions import Self


class LanguageEnum(str, Enum):
    """
    * `` -  * `et` - Eesti * `ru` - Русский * `en` - English * `us` - English (US) * `lv` - Latviski * `fi` - Suomi * `nb` - Norsk * `pl` - Polski
    """

    """
    allowed enum values
    """
    ET = "et"
    RU = "ru"
    EN = "en"
    US = "us"
    LV = "lv"
    FI = "fi"
    NB = "nb"
    PL = "pl"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LanguageEnum from a JSON string"""
        return cls(json.loads(json_str))
