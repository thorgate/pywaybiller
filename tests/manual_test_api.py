import typing as t
import argparse
import json

import json_stream
from pydantic import ValidationError, BaseModel

from pywaybiller import openapi_client, WaybillerClient
import logging


models = {c.__name__: c for c in [
    openapi_client.ExternalAPIWaybillList,
    openapi_client.ExternalAPIWaybillRetrieve,
    openapi_client.ExternalAPIOriginList,
    openapi_client.ExternalAPIOriginRead,
    openapi_client.ExternalAPIDestination,
]}


def main():
    parser = argparse.ArgumentParser(
        prog='Manual test on waybill dump',
    )
    parser.add_argument('--host', required=False, default='https://app.waybiller.com')
    parser.add_argument('--model', required=True, choices=models.keys())
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--stop-on-error', default=False, action="store_true")
    parser.add_argument('--debug', default=False, action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    model_class = models[args.model]
    count = 0
    error_count = 0

    client = WaybillerClient(api_key=args.api_key, host=args.host)

    results: t.Collection[BaseModel] = []
    match model_class:
        case openapi_client.ExternalAPIWaybillList:
            results = client.waybills.all()
        case openapi_client.ExternalAPIWaybillRetrieve:
            waybills = client.waybills.all()
            results = [
                client.waybills.waybills_retrieve(str(waybill.raw_data.waybill_id)) for waybill in waybills
            ]
        case openapi_client.ExternalAPIOriginList:
            results = client.origins.all()
        case openapi_client.ExternalAPIOriginRead:
            origins = client.origins.all()
            results = [
                client.origins.origins_retrieve(origin.raw_data.id) for origin in origins
            ]
        case openapi_client.ExternalAPIDestination:
            results = client.destinations.all()

    for result in results:
        count += 1
        try:
            model_class.from_dict(client.sanitize_for_serialization(result))
        except ValidationError as e:
            error_count += 1
            logging.exception(
                "Model %s is invalid",
                getattr(result, "id", "??"),
            )
            if args.stop_on_error:
                raise e

    logging.info("%s errors out of %s", error_count, count)


if __name__ == "__main__":
    main()
