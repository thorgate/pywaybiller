# coding: utf-8

"""
    Waybiller External API

     **Waybiller** external API is a feature that allows companies to access **Waybiller** data as JSON objects and create **Waybiller** instances out of their own data.  To make integration easier for the companies, external API features mapping support - it is possible to create company specific mappings for object identifiers (such as destination and origin).  These mappings will be used for representing companies data from external API, and for converting the values during creation of **Waybiller** instances (such as transport orders and waybills).  Most of the API responses contain mapped values, that may be null if company doesn't have mapping for this object.  **Waybiller** unique identifiers and values can be accessed through `raw_data` key.  API is HTTPS and JSON based.  # Pagination  By default, results of list endpoints are presented with pages of 30 items.  It is possible to control the page size with `limit` parameter: `/external-api/<some-list-endpoint>/?limit=<number>` where `<number>` is an integer between 1 and 1000. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictInt, StrictStr

from typing import Optional

from pywaybiller.openapi_client.models.destinations_list200_response import (
    DestinationsList200Response,
)

from pywaybiller.openapi_client.api_client import ApiClient
from pywaybiller.openapi_client.api_response import ApiResponse
from pywaybiller.openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class DestinationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def destinations_list(
        self,
        name: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified name (case sensitive)."
            ),
        ] = None,
        name__iexact: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified name (case insensitive)."
            ),
        ] = None,
        name__contains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which names contain this keyword (case sensitive)."
            ),
        ] = None,
        name__icontains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which names contain this keyword (case insensitive)."
            ),
        ] = None,
        location__address: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified address (case sensitive)."
            ),
        ] = None,
        location__address__iexact: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified address (case insensitive)."
            ),
        ] = None,
        location__address__contains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which addresses contain this keyword (case sensitive)."
            ),
        ] = None,
        location__address__icontains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which addresses contain this keyword (case insensitive)."
            ),
        ] = None,
        company__reg_code: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company with the specified register code (case sensitive)."
            ),
        ] = None,
        company__reg_code__iexact: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company with the specified register code (case insensitive)."
            ),
        ] = None,
        company__reg_code__contains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company of which register codes contain this keyword (case sensitive)."
            ),
        ] = None,
        company__reg_code__icontains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company of which register codes contain this keyword (case insensitive)."
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(description="Number of results to return per page."),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(description="The initial index from which to return the results."),
        ] = None,
        explicitly_viewable: Annotated[
            Optional[StrictBool],
            Field(
                description="Filters destinations that belong to your company or where your company was added as a partner."
            ),
        ] = None,
        **kwargs
    ) -> DestinationsList200Response:  # noqa: E501
        """Querying of destinations  # noqa: E501

        Returns all destinations associated with your company, according to the specified filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.destinations_list(name, name__iexact, name__contains, name__icontains, location__address, location__address__iexact, location__address__contains, location__address__icontains, company__reg_code, company__reg_code__iexact, company__reg_code__contains, company__reg_code__icontains, limit, offset, explicitly_viewable, async_req=True)
        >>> result = thread.get()

        :param name: Filters destinations with specified name (case sensitive).
        :type name: str
        :param name__iexact: Filters destinations with specified name (case insensitive).
        :type name__iexact: str
        :param name__contains: Filters destinations of which names contain this keyword (case sensitive).
        :type name__contains: str
        :param name__icontains: Filters destinations of which names contain this keyword (case insensitive).
        :type name__icontains: str
        :param location__address: Filters destinations with specified address (case sensitive).
        :type location__address: str
        :param location__address__iexact: Filters destinations with specified address (case insensitive).
        :type location__address__iexact: str
        :param location__address__contains: Filters destinations of which addresses contain this keyword (case sensitive).
        :type location__address__contains: str
        :param location__address__icontains: Filters destinations of which addresses contain this keyword (case insensitive).
        :type location__address__icontains: str
        :param company__reg_code: Filters destinations belonging to the company with the specified register code (case sensitive).
        :type company__reg_code: str
        :param company__reg_code__iexact: Filters destinations belonging to the company with the specified register code (case insensitive).
        :type company__reg_code__iexact: str
        :param company__reg_code__contains: Filters destinations belonging to the company of which register codes contain this keyword (case sensitive).
        :type company__reg_code__contains: str
        :param company__reg_code__icontains: Filters destinations belonging to the company of which register codes contain this keyword (case insensitive).
        :type company__reg_code__icontains: str
        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param explicitly_viewable: Filters destinations that belong to your company or where your company was added as a partner.
        :type explicitly_viewable: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DestinationsList200Response
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the destinations_list_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.destinations_list_with_http_info(
            name,
            name__iexact,
            name__contains,
            name__icontains,
            location__address,
            location__address__iexact,
            location__address__contains,
            location__address__icontains,
            company__reg_code,
            company__reg_code__iexact,
            company__reg_code__contains,
            company__reg_code__icontains,
            limit,
            offset,
            explicitly_viewable,
            **kwargs
        )  # noqa: E501

    @validate_arguments
    def destinations_list_with_http_info(
        self,
        name: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified name (case sensitive)."
            ),
        ] = None,
        name__iexact: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified name (case insensitive)."
            ),
        ] = None,
        name__contains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which names contain this keyword (case sensitive)."
            ),
        ] = None,
        name__icontains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which names contain this keyword (case insensitive)."
            ),
        ] = None,
        location__address: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified address (case sensitive)."
            ),
        ] = None,
        location__address__iexact: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations with specified address (case insensitive)."
            ),
        ] = None,
        location__address__contains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which addresses contain this keyword (case sensitive)."
            ),
        ] = None,
        location__address__icontains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations of which addresses contain this keyword (case insensitive)."
            ),
        ] = None,
        company__reg_code: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company with the specified register code (case sensitive)."
            ),
        ] = None,
        company__reg_code__iexact: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company with the specified register code (case insensitive)."
            ),
        ] = None,
        company__reg_code__contains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company of which register codes contain this keyword (case sensitive)."
            ),
        ] = None,
        company__reg_code__icontains: Annotated[
            Optional[StrictStr],
            Field(
                description="Filters destinations belonging to the company of which register codes contain this keyword (case insensitive)."
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(description="Number of results to return per page."),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(description="The initial index from which to return the results."),
        ] = None,
        explicitly_viewable: Annotated[
            Optional[StrictBool],
            Field(
                description="Filters destinations that belong to your company or where your company was added as a partner."
            ),
        ] = None,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Querying of destinations  # noqa: E501

        Returns all destinations associated with your company, according to the specified filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.destinations_list_with_http_info(name, name__iexact, name__contains, name__icontains, location__address, location__address__iexact, location__address__contains, location__address__icontains, company__reg_code, company__reg_code__iexact, company__reg_code__contains, company__reg_code__icontains, limit, offset, explicitly_viewable, async_req=True)
        >>> result = thread.get()

        :param name: Filters destinations with specified name (case sensitive).
        :type name: str
        :param name__iexact: Filters destinations with specified name (case insensitive).
        :type name__iexact: str
        :param name__contains: Filters destinations of which names contain this keyword (case sensitive).
        :type name__contains: str
        :param name__icontains: Filters destinations of which names contain this keyword (case insensitive).
        :type name__icontains: str
        :param location__address: Filters destinations with specified address (case sensitive).
        :type location__address: str
        :param location__address__iexact: Filters destinations with specified address (case insensitive).
        :type location__address__iexact: str
        :param location__address__contains: Filters destinations of which addresses contain this keyword (case sensitive).
        :type location__address__contains: str
        :param location__address__icontains: Filters destinations of which addresses contain this keyword (case insensitive).
        :type location__address__icontains: str
        :param company__reg_code: Filters destinations belonging to the company with the specified register code (case sensitive).
        :type company__reg_code: str
        :param company__reg_code__iexact: Filters destinations belonging to the company with the specified register code (case insensitive).
        :type company__reg_code__iexact: str
        :param company__reg_code__contains: Filters destinations belonging to the company of which register codes contain this keyword (case sensitive).
        :type company__reg_code__contains: str
        :param company__reg_code__icontains: Filters destinations belonging to the company of which register codes contain this keyword (case insensitive).
        :type company__reg_code__icontains: str
        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param explicitly_viewable: Filters destinations that belong to your company or where your company was added as a partner.
        :type explicitly_viewable: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DestinationsList200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            "name",
            "name__iexact",
            "name__contains",
            "name__icontains",
            "location__address",
            "location__address__iexact",
            "location__address__contains",
            "location__address__icontains",
            "company__reg_code",
            "company__reg_code__iexact",
            "company__reg_code__contains",
            "company__reg_code__icontains",
            "limit",
            "offset",
            "explicitly_viewable",
        ]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destinations_list" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("name") is not None:  # noqa: E501
            _query_params.append(("name", _params["name"]))

        if _params.get("name__iexact") is not None:  # noqa: E501
            _query_params.append(("name__iexact", _params["name__iexact"]))

        if _params.get("name__contains") is not None:  # noqa: E501
            _query_params.append(("name__contains", _params["name__contains"]))

        if _params.get("name__icontains") is not None:  # noqa: E501
            _query_params.append(("name__icontains", _params["name__icontains"]))

        if _params.get("location__address") is not None:  # noqa: E501
            _query_params.append(("location__address", _params["location__address"]))

        if _params.get("location__address__iexact") is not None:  # noqa: E501
            _query_params.append(
                ("location__address__iexact", _params["location__address__iexact"])
            )

        if _params.get("location__address__contains") is not None:  # noqa: E501
            _query_params.append(
                ("location__address__contains", _params["location__address__contains"])
            )

        if _params.get("location__address__icontains") is not None:  # noqa: E501
            _query_params.append(
                (
                    "location__address__icontains",
                    _params["location__address__icontains"],
                )
            )

        if _params.get("company__reg_code") is not None:  # noqa: E501
            _query_params.append(("company__reg_code", _params["company__reg_code"]))

        if _params.get("company__reg_code__iexact") is not None:  # noqa: E501
            _query_params.append(
                ("company__reg_code__iexact", _params["company__reg_code__iexact"])
            )

        if _params.get("company__reg_code__contains") is not None:  # noqa: E501
            _query_params.append(
                ("company__reg_code__contains", _params["company__reg_code__contains"])
            )

        if _params.get("company__reg_code__icontains") is not None:  # noqa: E501
            _query_params.append(
                (
                    "company__reg_code__icontains",
                    _params["company__reg_code__icontains"],
                )
            )

        if _params.get("limit") is not None:  # noqa: E501
            _query_params.append(("limit", _params["limit"]))

        if _params.get("offset") is not None:  # noqa: E501
            _query_params.append(("offset", _params["offset"]))

        if _params.get("explicitly_viewable") is not None:  # noqa: E501
            _query_params.append(
                ("explicitly_viewable", _params["explicitly_viewable"])
            )

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["API key"]  # noqa: E501

        _response_types_map = {
            "200": "DestinationsList200Response",
        }

        return self.api_client.call_api(
            "/destinations/",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
