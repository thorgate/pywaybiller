# Changelog

## Unreleased
* **Breaking** Use refactored waybiller external API schema (exported via DRF-spectacular). Drop all previous schema
patches and start from scratch.

## Version 0.2.2
* Do not require organizer_user_id for creating transport orders, as it may not bre required if default is configured on the server

## Version 0.2.1
* Update Waybiller schema

## Version 0.2.0

* **Breaking** Use new Waybiller schema - some classes get renamed because of this change
* **Breaking** Drop support for Python 3.8
* Update to use newer openapi generator (pydantic 2)
* Ensure read-only fields are serialized correctly when saving data locally
* Fix set sanitization in sanitize_for_serialization

## Version 0.1.0

* Generate initial version of the client
* Add schema patch to correctly handle waybill list view filters
