# Changelog

## Version 0.2.0

* **Breaking** Use new Waybiller schema - some classes get renamed because of this change
* **Breaking** Drop support for Python 3.8
* Update to use newer openapi generator (pydantic 2)
* Ensure read-only fields are serialized correctly when saving data locally

## Version 0.1.0

* Generate initial version of the client
* Add schema patch to correctly handle waybill list view filters
