import argparse
import json

import json_stream
from pydantic import ValidationError

from pywaybiller import openapi_client
import logging


models = {c.__name__: c for c in [
    openapi_client.ExternalAPIWaybillList,
    openapi_client.ExternalAPIWaybillRetrieve,
    openapi_client.ExtAPIOriginList,
    openapi_client.ExtAPIOriginRead,
    openapi_client.ExtAPIDestination,
]}


def main():
    parser = argparse.ArgumentParser(
        prog='Manual test on waybill dump',
    )
    parser.add_argument('--filename', required=True)
    parser.add_argument('--model', required=True, choices=models.keys())
    parser.add_argument('--skip-lines', type=int, default=0)
    parser.add_argument('--stop-on-error', default=False, action="store_true")
    parser.add_argument('--debug', default=False, action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    model_class = models[args.model]
    count = 0
    error_count = 0

    with open(args.filename) as f:
        if args.skip_lines > 0:
            for _ in range(args.skip_lines):
                f.readline()

        for serialized_model in json_stream.load(f).persistent():
            count += 1
            serialized_model = json_stream.to_standard_types(serialized_model)
            try:
                model = model_class.from_dict(serialized_model)
                logging.debug("Model %s is valid", getattr(model, "number", getattr(model, "id", "??")))

            except ValidationError as e:
                error_count += 1
                logging.exception(
                    "Model %s is invalid\n%s",
                    serialized_model.get("number", serialized_model.get("id", "??")),
                    json.dumps(serialized_model, indent=4)
                )
                if args.stop_on_error:
                    raise e

    logging.info("%s errors out of %s", error_count, count)


if __name__ == "__main__":
    main()
